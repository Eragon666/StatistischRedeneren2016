# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# File:         random_2.py
#
# In this file the subassignments of assignment 2 is implemented.


import numpy as np
from matplotlib import pyplot as plt


def IBM(a, c, m, x_old):
	return (a * x_old + c) % m

# De IBM afleiding kan het volgende 'random' getal berekenen.
# parameters: x = k+1 en y = k
# return k + 2
def IBM_afleiding(x, y):
	return 6*x - 9*y	


# Assignment 2.1
def assignment1():

	x = np.random.uniform(0, 1, 500)
	y = np.random.uniform(0, 1, 500)
		
	plt.scatter(x, y, color='red')
	plt.title("Numpy: Random points between 0 and 1")
	    
	plt.show()

	# Assignemnt 2.2
def assignment2():

	a = 65539
	c = 0
	m = 2**31
	# Wij gebruiken vaste seeds om de IBM generator te testen zodat we
	# het kunnen debuggen.
	# Het zou kunnen dat een seed kan worden afgeleid van de tijd van de 
	# computer. De tijd kan dan worden gemanipuleerd om een pseudo random
	# seed te genereren.
	seed1 = 5
	seed2 = 17

	x = []
	y = []

	print "Seed1 is: " + str(seed1)
	k1 = IBM(a, c, m, seed1)

	print "See2 is: " + str(seed2)
	k2 = IBM(a, c, m, seed2)

	for i in range(500):
		k1 = IBM(a, c, m, k1)
		# print k1 / float(m)
		x.append(k1 / float(m))

	for i in range(500):
		k2 = IBM(a, c, m, k2)
		# print k2 / float(m)
		y.append(k2 / float(m))


	plt.scatter(x, y, color='red')
	plt.title("IBM method : Random points between 0 and 1")
	    
	plt.show()



def assignment3():

	a = 65539
	c = 0
	m = 2**31

	seed = 1

	k1 = IBM(a, c, m, seed)
	k2 = IBM(a, c, m, k1)
	k3 = IBM(a, c, m, k2)

	afl = IBM_afleiding(k2, k1)

	print "We hebben met de IBM methode een random getal berekend: " + str(k3)
	print 
	print """Als we nu deze \'random\' getal proberen te berekenen met de twee 
vorige \'random\' getallen dan krijgen we hetzelfde getal: """ + str(afl)



if __name__ == '__main__':
	
	# assignment1()
	# assignment2()
	assignment3()
