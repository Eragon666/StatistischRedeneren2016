# Opgave 4.2
# Door: Younes Ouazref (10732519),
# 		Kwan Win Chung (10729585), 
# 		Matthijs Thoolen (10447822)
# Datum: 08-05-2016

from pylab import loadtxt, arange, loadtxt, permutation, transpose,\
    zeros, sum, plot, subplot, array, scatter, logical_and, figure,\
    savefig, tile, argmin, argsort

import sys
sys.path.append("./python")

# Class for k-Nearest Neighbor (Partly given)
class NNb:

	# All given
    def __init__(self, X, c):
        self.n, self.N = X.shape
        self.X = X
        self.c = c

    def classify(self, x, k): 
        d = self.X - tile(x.reshape(self.n,1), self.N);
        dsq = sum(d*d,0)
        minindex = argmin(dsq)
        temp = argsort(dsq)
		
		### Custom code starting here ###
		
        # Save the data for each class around the point in a array
        score = [0, 0, 0]

        # With the help of k surrounding points score each class
        for x in range (0, k):
            if ((self.c[temp[x]]) == 1.0):
                score[0] +=1;
            elif ((self.c[temp[x]]) == 2.0):
                score[1] += 1;
            elif ((self.c[temp[x]]) == 3.0):
                score[2] += 1; 

        # Check to which class the point is classified
        if (score[0] > score[1] and score[0] > score[2]):
            return 1.0
        elif (score[1] > score[2]):
            return 2.0

        # If there are points with the same value, assign the class of the nearest neighbour.
        elif(score[0] == score[1] and score[0] == score[2]):       
            return self.c[minindex]
        else:
            return 3.0

# Given function
def cnvt(s):
    tab = {'Iris-setosa':1.0, 'Iris-versicolor':2.0, 'Iris-virginica':3.0}
    if tab.has_key(s):
        return tab[s]
    else:
        return -1.0


# Main function (all given in handout)		
def main():
	XC = loadtxt('iris.data', delimiter=',', dtype=float, converters={4: cnvt})

	ind = arange(150) # indices into the dataset
	ind = permutation(ind) # random permutation
	L = ind[0:90] # learning set indices
	T = ind[90:] # test set indices

	# Learning Set
	X = transpose(XC[L,0:4])
	nnc = NNb(X, XC[L,-1])

	# Classification of Test Set
	c = zeros(len(T))
	for i in arange(len(T)):
		print sys.argv[1]
		print int(sys.argv[1])
		c[i] = nnc.classify(XC[T[i],0:4],int(sys.argv[1]))
	# Confusion Matrix
	CM = zeros((3,3))
	for i in range(3):
		for j in range(3):
			CM[i,j] = sum( logical_and(XC[T,4]==(i+1),c==(j+1)) )

	print(CM)

	# Plot Test Set
	figure(1)
	color = array( [[1,0,0],[0,1,0],[0,0,1]] )
	for i in range(4):
		for j in range(4):
			subplot(4,4,4*i+j+1)
			if i==j:
				continue
			
			print color[XC[T,4].astype(int)-1]
			print [1,1,1]*len(T)
			print color[c.astype(int)-1]
				
			scatter( XC[T,i], XC[T,j], s=100, marker='s', edgecolor=color[XC[T,4].astype(int)-1], facecolor=[1,1,1]*len(T))
			scatter( XC[T,i], XC[T,j], s=30, marker='+', edgecolor=color[c.astype(int)-1])

	savefig('figures/nnbtest.pdf')
	
if __name__ == "__main__":
	main()


