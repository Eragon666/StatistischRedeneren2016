#######
# Opdracht 22
# Door: Kwan Win Chung, Younes en Matthijs Thoolen
# Datum: 2-5-2016
#######

from pylab import *

def meanAndCovariance(mu, Sigma, length):

    # With the known mu and sigma we generate the data set
    d, U = eig(Sigma)
    L = diagflat(d)
    A = dot(U, sqrt(L))
    X = randn(4, length)
    
    # The data matrix
    Y = dot(A,X) + tile(mu, length)

    Mean = mean(Y, 1)

    # We need to subtract the mean from each column
    Yzm = Y - tile(Mean[:,newaxis], length)
    
    # Estimate covariance matrix
    CoMa = dot(Yzm, transpose(Yzm)) / (length-1)
    
    return (Mean, CoMa)
    
def calcMu(mu, Sigma, length):    
    # With the known mu and sigma we generate the data set
    d, U = eig(Sigma)
    L = diagflat(d)
    A = dot(U, sqrt(L))
    X = randn(4, 1000)
    Y = dot(A,X) + tile(mu, 1000)
    
    # An array that will hold the estimations of the mean
    collection = np.zeros((length, 4))

    # Calculate the mean values and put it in a data matrix
    for x in range (0, length):
	    Mean = mean(Y, 1)
	    collection[x] = Mean   
    
    reshape = collection.reshape(4, 1000)
    Mean = mean(reshape, 1)
    
    # We need to subtract the mean from each column
    Yzm = reshape - tile(Mean[:, newaxis], 1000)
    
    # Estimate covariance matrix
    CoMa = dot(Yzm, transpose(Yzm)) / 999
    
    return (Mean, CoMa);
    
def main():

    Sigma = array( [[  3.01602775,   1.02746769,  -3.60224613,  -2.08792829],
	    [  1.02746769,   5.65146472,  -3.98616664,   0.48723704],
	    [ -3.60224613,  -3.98616664,  13.04508284,  -1.59255406],
	    [ -2.08792829,   0.48723704,  -1.59255406,   8.28742469]] )
	    
    mu = array([[1],[2],[3],[4]])
    
    length = 10**3

    #result1 = meanAndCovariance(mu, Sigma, length)
    #print("Mean (Estimated):", result1[0])
    #print("Covariance matrix (Estimated):", result1[1])
    
    result2 = calcMu(mu, Sigma, length)
    print("Mean (Estimated):", result2[0])
    print("Covariance matrix (Estimated):", result2[1])

if __name__ == "__main__":
    main()
