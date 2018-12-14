import numpy as np
import numpy.linalg as la

class MatrixProductState(object):

    def __init__(self,tensor_list):
        # deals with a MPS chain (ring not allowed)
        # tensor_list is a list of tensors, starting with a 2-tensor, followed by
        # 3-tensors, and ending with a 2-tensor
        # run a series of checkes to make sure the dimension matches
        #
        # Ordering of indices as follows:
        #
        #     M0--1  0--Mk--2  0--M(L-1)
        #      |         |         |
        #      0         1         1
        #
        self.length = len(tensor_list)
        self.in_dims = np.zeros(self.length-1,np.int)  # bond dimensions
        self.out_dims = np.zeros(self.length,np.int)
        self.tensor_list = tensor_list
        # check dimension compatibility
        assert tensor_list[0].shape[1] == tensor_list[1].shape[0]
        assert len(tensor_list[0].shape) == 2
        assert len(tensor_list[-1].shape) == 2
        for ix in range(1,self.length-1):
            assert len(tensor_list[ix].shape) == 3
            assert tensor_list[ix].shape[2] == tensor_list[ix+1].shape[0]
            self.in_dims[ix-1] = tensor_list[ix].shape[0]
            self.out_dims[ix] = tensor_list[ix].shape[1]
        self.in_dims[-1] = tensor_list[-1].shape[0]
        self.out_dims[-1] = tensor_list[-1].shape[1]
        self.out_dims[0] = tensor_list[0].shape[0]
        # check bond dimensions
        # if fails means bond dimensions at certain sites are unnecessarily large
        # which will cause error in QR factorization
        assert self.out_dims[0] >= self.in_dims[0]
        assert self.out_dims[-1] >= self.in_dims[-1]
        for ix in range(1,self.length-1):
            assert self.in_dims[ix-1]*self.out_dims[ix] >= self.in_dims[ix]
            assert self.in_dims[ix]*self.out_dims[ix] >= self.in_dims[ix-1]

    def left_normalize_QR(self,pos):
        # Left normalize the tensor at pos
        assert pos <= self.length-2  # CANNOT left normalize the last tensor
        if pos == 0:  # Left normalize the first tensor
            Q, R = la.qr(self.tensor_list[0])
            self.tensor_list[0][:] = Q
            tM = np.matmul( R,
                self.tensor_list[1].reshape(self.in_dims[0],self.out_dims[1]*self.in_dims[1]) )
            self.tensor_list[1][:] = tM.reshape(self.tensor_list[1].shape)
        elif pos == self.length-2:  # Left normalize the second-to-last tensor
            Q, R = la.qr( self.tensor_list[pos].reshape(
                        self.in_dims[pos-1]*self.out_dims[pos],self.in_dims[pos]) )
            self.tensor_list[pos][:] = Q.reshape(self.tensor_list[pos].shape)
            tM = np.matmul( R, self.tensor_list[-1] )
            self.tensor_list[-1][:] = tM
        else:  # Left normalize in the middle
            Q, R = la.qr( self.tensor_list[pos].reshape(
                        self.in_dims[pos-1]*self.out_dims[pos],self.in_dims[pos]) )
            self.tensor_list[pos][:] = Q.reshape(self.tensor_list[pos].shape)
            tM = np.matmul( R,
                self.tensor_list[pos+1].reshape(
                    self.in_dims[pos],self.out_dims[pos+1]*self.in_dims[pos+1]) )
            self.tensor_list[pos+1][:] = tM.reshape(self.tensor_list[pos+1].shape)

    def right_normalize_QR(self,pos):
        # Right normalize the tensor at pos
        assert pos >= 1
        if pos == 1: #Right normalize the second tensor
            QT, RT = la.qr( self.tensor_list[pos].reshape(
                self.in_dims[pos-1],self.out_dims[pos]*self.in_dims[pos]).T )
            self.tensor_list[pos][:] = QT.T.reshape(self.tensor_list[pos].shape)
            tM = np.matmul( self.tensor_list[0], RT.T )
            self.tensor_list[0][:] = tM.reshape(self.tensor_list[0].shape)
        elif pos == self.length-1:
            QT, RT = la.qr( self.tensor_list[-1].T )
            self.tensor_list[-1][:] = QT.T
            tM = np.matmul( self.tensor_list[pos-1].reshape(
                self.in_dims[pos-2]*self.out_dims[pos-1],self.in_dims[pos-1]), RT.T )
            self.tensor_list[pos-1][:] = tM.reshape(self.tensor_list[pos-1].shape)
        else:
            QT, RT = la.qr( self.tensor_list[pos].reshape(
                self.in_dims[pos-1],self.out_dims[pos]*self.in_dims[pos]).T )
            self.tensor_list[pos][:] = QT.T.reshape(self.tensor_list[pos].shape)
            tM = np.matmul( self.tensor_list[pos-1].reshape(
                self.in_dims[pos-2]*self.out_dims[pos-1],self.in_dims[pos-1]), RT.T )
            self.tensor_list[pos-1][:] = tM.reshape(self.tensor_list[pos-1].shape)
