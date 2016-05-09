# Namen: Kwan Win Chung, Matthijs Thoolen en Younes Ouazref
# Studentnummers: 10729585, 10447822 en 10732519
# File: opgave43.py
# 
# Comments: In deze file zijn de figuren getekend.


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def main():

	# De waarden.
	mu1 = 4
	sigma1 = 1
	pc1 = 0.3

	mu2 = 7
	sigma2 = 2
	pc2 = 0.7

	# De x as lengte.
	x = np.arange(-4, 15.01, 0.01)

	# Bereken pxc(x, C = 1) en pxc(x, C = 2).
	pxc1 = mlab.normpdf(x, mu1, sigma1) * pc1
	pxc2 = mlab.normpdf(x, mu2, sigma2) * pc2

	# Teken de figuren.
	plt.title('De figuren van opgave 4.3')
	plt.plot(x, pxc1, "b")
	plt.plot(x, pxc2, "r")
	# Bereken P(C = 1|x) en P(C = 2|x).
	plt.plot(x, pxc1 / (pxc1 + pxc2), "b--")
	plt.plot(x, pxc2 / (pxc1 + pxc2), "r--")

	plt.xlabel('x')
	plt.ylabel('y')

	plt.legend(['pxc(x, C = 1)', 'pxc(x, C = 2)', 'P(C = 1|x)', 'P(C = 2|x)'])
	plt.show()


if __name__ == '__main__':
	main()
