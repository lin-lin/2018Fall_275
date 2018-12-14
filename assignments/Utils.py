import numpy as np
import MPS
import MPO

def generate_random_mps(length, site_dim, max_bond):
    in_dims = np.zeros(length-1,np.int)
    in_dims[0] = min(site_dim, max_bond)
    in_dims[-1] = min(site_dim, max_bond)
    if length % 2 == 0:
        for ix in range(1,length//2):
            in_dims[ix] = min(in_dims[ix-1]*site_dim, max_bond)
            in_dims[-ix-1] = min(in_dims[-ix]*site_dim, max_bond)
    else:
        for ix in range(1,length//2):
            in_dims[ix] = min(in_dims[ix-1]*site_dim, max_bond)
            in_dims[-ix-1] = min(in_dims[-ix]*site_dim, max_bond)
    tensor_list = []
    tensor_list.append(np.random.randn(site_dim,in_dims[0])+
                    1.0j*np.random.randn(site_dim,in_dims[0]))
    for ix in range(1,length-1):
        tensor_list.append(np.random.randn(in_dims[ix-1],site_dim,in_dims[ix])
                + 1.0j*np.random.randn(in_dims[ix-1],site_dim,in_dims[ix]))
    tensor_list.append(np.random.randn(in_dims[-1],site_dim)+
                1.0j*np.random.randn(in_dims[-1],site_dim))
    return MPS.MatrixProductState(tensor_list)


def generate_quadratic_nn_mpo(alpha,beta):
    L = len(beta)
    creation_op = np.array([[0.0, 0.0], [1.0, 0.0]])
    annihilation_op = np.array([[0.0, 1.0], [0.0, 0.0]])
    number_op = np.array([[0.0, 0.0], [0.0, 1.0]])
    W = np.zeros([2,2,4],dtype=np.complex)
    W[:,:,0] = np.eye(2)
    W[:,:,1] = alpha[0]*creation_op
    W[:,:,2] = alpha[0]*annihilation_op
    W[:,:,3] = beta[0]*number_op
    tensor_list = [W]
    for ix in range(1,L-1):
        W = np.zeros([4,2,2,4],dtype=np.complex)
        W[0,:,:,0] = np.eye(2)
        W[0,:,:,1] = alpha[ix]*creation_op
        W[0,:,:,2] = alpha[ix]*annihilation_op
        W[0,:,:,3] = beta[ix]*number_op
        W[1,:,:,3] = annihilation_op
        W[2,:,:,3] = creation_op
        W[3,:,:,3] = np.eye(2)
        tensor_list.append(W)
    W = np.zeros([4,2,2],dtype=np.complex)
    W[0,:,:] = beta[-1]*number_op
    W[1,:,:] = annihilation_op
    W[2,:,:] = creation_op
    W[3,:,:] = np.eye(2)
    tensor_list.append(W)
    return MPO.MatrixProductOperator(tensor_list)


def generate_hubbard_mpo(t,U,mu,L):
    creation_op = np.array([[0.0, 0.0], [1.0, 0.0]])
    annihilation_op = np.array([[0.0, 1.0], [0.0, 0.0]])
    Z = np.array([[1.0, 0.0], [0.0, -1.0]])
    I2 = np.eye(2)
    creation_up = np.kron(Z, creation_op)
    creation_down = np.kron(creation_op, I2)
    annihilation_up = creation_up.T
    annihilation_down = creation_down.T
    number_up = np.diag([0.0, 1.0, 0.0, 1.0])
    number_down = np.diag([0.0, 0.0, 1.0, 1.0])
    P = np.kron(Z, Z) # Parity operator
    I4 = np.eye(4)
    W = np.zeros([4,4,6])
    W[:,:,0] = U*(np.dot(number_up, number_down)) - mu*(number_up+number_down)
    W[:,:,1] = -t*(np.dot(creation_up, P))
    W[:,:,2] = -t*(np.dot(P, annihilation_up))
    W[:,:,3] = -t*(np.dot(creation_down, P))
    W[:,:,4] = -t*(np.dot(P, annihilation_down))
    W[:,:,5] = I4
    tensor_list = [W]
    for ix in range(1,L-1):
        W = np.zeros([6,4,4,6])
        W[0,:,:,0] = I4
        W[1,:,:,0] = annihilation_up
        W[2,:,:,0] = creation_up
        W[3,:,:,0] = annihilation_down 
        W[4,:,:,0] = creation_down
        W[5,:,:,0] = U*(np.dot(number_up,number_down)) - mu*(number_up+number_down)
        W[5,:,:,1] = -t*(np.dot(creation_up, P))
        W[5,:,:,2] = -t*(np.dot(P, annihilation_up))
        W[5,:,:,3] = -t*(np.dot(creation_down, P))
        W[5,:,:,4] = -t*(np.dot(P, annihilation_down))
        W[5,:,:,5] = I4
        tensor_list.append(W)
    W = np.zeros([6,4,4])
    W[0,:,:] = I4
    W[1,:,:] = annihilation_up 
    W[2,:,:] = creation_up
    W[3,:,:] = annihilation_down 
    W[4,:,:] = creation_down
    W[5,:,:] = U*(np.dot(number_up, number_down)) - mu*(number_up+number_down)
    tensor_list.append(W)
    return MPO.MatrixProductOperator(tensor_list)
