print('*'*15+'Plain numpy implementation of PCA'+'*'*15)
#Written using only numpy
from numpy import array,mean,cov
from numpy.linalg import eig
from sklearn.decomposition._pca import PCA

#define matrix
print("\n")
A = array([[1,2],[3,4],[5,6]])
print("Initial Martix = {} \n".format(A))

#Calculate mean
M = mean(A.T,axis = 1)
print("Mean of the matrix = {} \n".format(M))

#Scale columns by subtracting column means
C = A - M
print("Column scaling applied over the matrix = {} \n".format(C))

#Calculate covariance
V = cov(C.T)
print("Covariance of the matrix = {} \n".format(V))

values,vectors = eig(V)
print("Eigen Vectors = {} \n".format(vectors))
print("Eigen values = {} \n".format(values))

P = vectors.T.dot(C.T)
print("Matrix after applying PCA = {} \n".format(P.T))

#Scikit learn Verifcation of the above result
print('*'*15+'Verification of the above result using sklearn'+'*'*15)

from numpy import array
from sklearn.decomposition import PCA
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# create the PCA instance
pca = PCA(2)
# fit on data
pca.fit(A)
# access values and vectors
print(pca.components_)
print(pca.explained_variance_)
# transform data
B = pca.transform(A)
print(B)