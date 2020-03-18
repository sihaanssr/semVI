#Written using only numpy
from numpy import array,mean,cov
from numpy.linalg import eig

#define matrix
A = array([[1,2],[3,4],[5,6]])
print(A)

#Calculate mean
M = mean(A.T,axis = 1)
print(M)

#Scale columns by subtracting column means
C = A - M
print(C)

#Calculate covariance
V = cov(C.T)
print(V)

values,vectors = eig(V)
print(vectors)
print(values)

P = vectors.T.dot(C.T)
print(P.T)