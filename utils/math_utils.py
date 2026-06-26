import numpy as np
def skew(w):
    w1 = w[0]
    w2 = w[1]
    w3 = w[2]
    skew_matrix = np.array([[0, -w3, w2],[w3, 0, -w1],[-w2, w1, 0]], dtype=float)
    return skew_matrix


def screw_matrix(S):
    omega = S[:3]
    v = S[3:]
    mat = np.zeros((4,4))
    mat[:3,:3]=skew(omega)
    mat[:3,3]=v
    return mat

def matrix_exp_screw(S,theta):
    omega = S[:3]
    v = S[3:]
    W = skew(omega)
    W2 = W@W
    R = np.eye(3) + np.sin(theta)*W + (1-np.cos(theta))*W2
    G = np.eye(3)*theta + (1-np.cos(theta))*W + (theta-np.sin(theta))*W2
    T = np.eye(4)
    T[:3,:3] = R
    T[:3,3] = G@v
    return T