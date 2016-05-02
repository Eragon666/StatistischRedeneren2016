# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20

import numpy as np
from matplotlib import pyplot as plt


def calculations():
	Sigma=np.array(
	[[ 3.01602775,  1.02746769, -3.60224613, -2.08792829],
	[ 1.02746769,  5.65146472, -3.98616664,  0.48723704],
	[-3.60224613, -3.98616664, 13.04508284, -1.59255406],
	[-2.08792829,  0.48723704, -1.59255406,  8.28742469]] )

	temp_array = np.array([[1],[2],[3],[4]])
	w, v = np.linalg.eig(Sigma)
	flat = np.diagflat(w)
	dot_prod = np.dot(v, np.sqrt(flat))
	X = np.random.randn(4, 400)
	dot_prod_X = np.dot(dot_prod,X) 
	Y = dot_prod_X + np.tile(temp_array, 400)
	return X, Y

def plotting(X, Y):
	f, ax = plt.subplots(4,4)
	for i in xrange(len(ax)):
		for j in xrange(len(ax)):
			ax[i,j].scatter(Y[i],Y[j])
	plt.show()

def main():
	X, Y = calculations()
	plotting(X, Y)

if __name__ == "__main__":
    main()




