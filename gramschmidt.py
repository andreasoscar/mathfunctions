import numpy as np
def ortho(A):
    v = []
    for i in range(np.shape(A)[1]):
        y = A[:,i]/np.linalg.norm(A[:,i],2)
        v.append(y)
    return v
def gramschmidt(v,A):
    q = np.empty(shape=(A.shape[0],0))
    rl = np.empty(shape=(A.shape[1],0))
    for j in range(1,np.shape(A)[1]+1):
        y = A[:,j-1]
        rc = []
        for i in range(1,j):
            if j == 1:
                qi = v[i-1]
            else:
                qi = q[:,i-1]
            r = ((qi.transpose())*y).item(0)
            rc.append([r])
            y = y - r*qi
        r = np.linalg.norm(y,2)
        rc.append([r])
        while len(rc) < A.shape[1]:
            rc.append([0])
        rl = np.hstack((rl,rc))
        qj = y/r
        q = np.hstack((q,qj))
    return q,rl
