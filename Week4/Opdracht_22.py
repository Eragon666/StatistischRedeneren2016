from pylab import *

def meanAndCovariance(mu, Sigma):

    # First generate data set with known mu and Sigma
    d, U = eig(Sigma)
    L = diagflat(d)
    A = dot(U, sqrt(L))
    X = randn(4, 1000)
    # Our data matrix is Y
    Y = dot(A,X) + tile(mu, 1000)

    # Calculate mean
    Ybar = mean(Y, 1)

    # subtract mean from each column
    Yzm = Y - tile(Ybar[:,newaxis], 1000)
    # Estimate covariance matrix
    S = dot(Yzm, transpose(Yzm)) / 999
    print("Estimated mean:", Ybar)
    print("Estimated Covariance matrix:", S)
    
def calcMu(mu, Sigma):
    # An array that will hold the estimations of the mean
    collect = np.zeros((1000, 4))

    # First generate data set with known mu and Sigma
    d, U = eig(Sigma)
    L = diagflat(d)
    A = dot(U, sqrt(L))
    X = randn(4, 1000)
    Y = dot(A,X) + tile(mu, 1000)

    # Calculate the mean values and put it in a data matrix
    for x in range (0, 1000):
	    Mean = mean(Y, 1)
	    collect[x] = Ybar

    collect = collect.reshape(4, 1000)
    Y = collect
    Mean = mean(Y, 1)
    # subtract mean from each column
    Yzm = Y - tile(Ybar[:, newaxis], 1000)
    # Estimate covariance matrix
    CoMa = dot(Yzm, transpose(Yzm)) / 999
    
    print("Mean (Estimated):\n", Mean)
    print("Covariance matrix (Estimated):\n", CoMa)
    
def main():

    Sigma = array( [[  3.01602775,   1.02746769,  -3.60224613,  -2.08792829],
	    [  1.02746769,   5.65146472,  -3.98616664,   0.48723704],
	    [ -3.60224613,  -3.98616664,  13.04508284,  -1.59255406],
	    [ -2.08792829,   0.48723704,  -1.59255406,   8.28742469]] )
	    
    mu = array([[1],[2],[3],[4]])

    meanAndCovariance(mu, Sigma)
    calcMu(mu, Sigma)

if __name__ == "__main__":
    main()
