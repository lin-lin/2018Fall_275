import numpy as np
import numpy.linalg as la
import scipy.linalg
import MPS

class MatrixProductOperator(object):

    def __init__(self,tensor_list):
        # construct MPO
        # index ordering        0          1         1
        #                       |          |         |
        #                       +--2    0--+--3   0--+
        #                       |          |         |
        #                       1          2         2
        # can only work for nonperiodic case so far

        self.length = len(tensor_list)
        self.tensor_list = tensor_list
        self.in_dims = np.zeros(self.length-1,dtype=np.int)
        self.out_dims = np.zeros(self.length,dtype=np.int)
        self.out_dims[0] = tensor_list[0].shape[0]
        assert len(self.tensor_list[0].shape) == 3
        assert len(self.tensor_list[-1].shape) == 3
        assert self.tensor_list[0].shape[0] == self.tensor_list[0].shape[1]
        self.in_dims[0] = tensor_list[0].shape[2]
        assert self.tensor_list[0].shape[2] == self.tensor_list[1].shape[0]
        for ix in range(1,self.length-1):
            self.in_dims[ix] = tensor_list[ix].shape[3]
            self.out_dims[ix] = tensor_list[ix].shape[1]
            assert tensor_list[ix].shape[1] == self.tensor_list[ix].shape[2]
            assert tensor_list[ix].shape[3] == self.tensor_list[ix+1].shape[0]
        self.out_dims[-1] = tensor_list[-1].shape[1]
        assert tensor_list[-1].shape[1] == tensor_list[-1].shape[2]

    @staticmethod
    def contract_from_left(E,A,W,B):
        #
        #   +--A-    +-     Index ordering of E and E'
        #   |  |     |           1
        #   E--W-  = E'-         E 2
        #   |  |     |           3
        #   +--B-    +-

        T1 = np.einsum("irt,ikj->trkj",A,E)
        T1 = np.einsum("trkj,krsu->tusj",T1,W)
        Enew = np.einsum("tusj,jsv",T1,B)
        return Enew

    @staticmethod
    def contract_from_right(F,A,W,B):
        #
        #  -+     -A--+   Index ordering of F and F'
        #   |      |  |         1
        #  -F' =  -W--F       2 F
        #   |      |  |         3
        #  -+     -B--+

        T = np.einsum("tri,ijk->trjk",A,F)
        T = np.einsum("trjk,ursj->tusk",T,W)
        Fnew = np.einsum("tusk,vsk->tuv",T,B)
        return Fnew

    def contract_from_left_until(self,mps1,mps2,pos):
        T1 = np.einsum("ijk,il->lkj",self.tensor_list[0],np.conj(mps1.tensor_list[0]))
        E = np.einsum("lkj,jm->lkm",T1,mps2.tensor_list[0])
        for ix in range(1,pos):
            E = self.contract_from_left(E,np.conj(mps1.tensor_list[ix]),
                self.tensor_list[ix],mps2.tensor_list[ix])
        return E

    def contract_from_right_until(self,mps1,mps2,pos):
        T1 = np.einsum("il,jlm->ijm",np.conj(mps1.tensor_list[-1]),self.tensor_list[-1])
        F = np.einsum("ijm,km->ijk",T1,mps2.tensor_list[-1])
        for ix in range(self.length-2,pos,-1):
            F = self.contract_from_right(F,np.conj(mps1.tensor_list[ix]),
                self.tensor_list[ix],mps2.tensor_list[ix])
        return F

    def contract_from_right_all(self,mps1,mps2):
        F_list = []
        T1 = np.einsum("il,jlm->ijm",np.conj(mps1.tensor_list[-1]),self.tensor_list[-1])
        F_list.append(np.einsum("ijm,km->ijk",T1,mps2.tensor_list[-1]))
        for ix in range(self.length-2,0,-1):
            F_list.append( self.contract_from_right(F_list[-1],np.conj(mps1.tensor_list[ix]),
                self.tensor_list[ix],mps2.tensor_list[ix]) )
        tT = np.einsum("rsj,ijk->risk",self.tensor_list[0],F_list[-1])
        tT = np.einsum("risk,ri->sk",tT,np.conj(mps1.tensor_list[0]))
        mps_contraction_result = np.einsum("sk,sk",tT,mps2.tensor_list[0])
        return mps_contraction_result, F_list

    def optimize_tensor(self,psi,pos,E,F):  # TODO: DEBUG! NOT TESTED
        if pos == 0:
            Hmat = np.einsum("stk,ikj->sitj",self.tensor_list[0],F)
            Hmat = Hmat.reshape(psi.out_dims[0]*psi.in_dims[0],psi.out_dims[0]*psi.in_dims[0])
            eigval, eigvec = scipy.linalg.eigh(Hmat,eigvals=(0,0))
            psi.tensor_list[0][:] = eigvec.reshape(psi.tensor_list[0].shape)
            return eigval[0]
        if pos == self.length-1:
            Hmat = np.einsum("ikj,kst->isjt",E,self.tensor_list[-1])
            Hmat = Hmat.reshape(psi.in_dims[-1]*psi.out_dims[-1],psi.in_dims[-1]*psi.out_dims[-1])
            # eigvec_test = psi.tensor_list[-1].reshape(psi.in_dims[-1]*psi.out_dims[-1],1)
            eigval, eigvec = scipy.linalg.eigh(Hmat,eigvals=(0,0))
            psi.tensor_list[-1][:] = eigvec.reshape(psi.tensor_list[-1].shape)
            # print(la.norm( Hmat@eigvec_test - eigval[0]*eigvec_test ))
            return eigval[0]
        else:
            Hmat = np.einsum("ikj,kstv,uvw->isujtw",E,self.tensor_list[pos],F)
            Hmat = Hmat.reshape(psi.in_dims[pos-1]*psi.out_dims[pos]*psi.in_dims[pos],
                psi.in_dims[pos-1]*psi.out_dims[pos]*psi.in_dims[pos])
            eigval, eigvec = scipy.linalg.eigh(Hmat,eigvals=(0,0))
            psi.tensor_list[pos][:] = eigvec.reshape(psi.tensor_list[pos].shape)
            return eigval[0]

    def variation_ground_state(self,psi,maxit,tol):
        it = 0
        ediff = 1.0 + tol
        L = self.length
        for ix in range(L-1,0,-1):
            psi.right_normalize_QR(ix)
        psi.tensor_list[0] /= la.norm(psi.tensor_list[0])
        energy, F_list = self.contract_from_right_all(psi,psi)

        while ediff > tol and it < maxit:
            energy_new = self.optimize_tensor(psi,0,None,F_list[-1])
            psi.left_normalize_QR(0)
            E = self.contract_from_left_until(psi,psi,0)

            # print(energy_new)

            for ix in range(1,L-1):
                energy_new = self.optimize_tensor(psi,ix,E,F_list[L-2-ix])
                psi.left_normalize_QR(ix)
                E = self.contract_from_left( E,np.conj(psi.tensor_list[ix]),
                            self.tensor_list[ix],psi.tensor_list[ix] )

                # print(energy_new)

            energy_new = self.optimize_tensor(psi,L-1,E,None)
            # print(energy_new)

            print("At iteration",it,"the energy is",energy_new)
            it += 1
            ediff = energy - energy_new
            if ediff < -1e-8:
                raise RuntimeError("Optimization failed!")

            for ix in range(L-1,0,-1):
                psi.right_normalize_QR(ix)
            psi.tensor_list[0] /= la.norm(psi.tensor_list[0])
            energy, F_list = self.contract_from_right_all(psi,psi)
        return energy
