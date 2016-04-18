# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# File:         random_2.py
#
# In deze file zijn de subassignments van opdracht 2 geimplementeerd.


import numpy as np
from matplotlib import pyplot as plt


# De IBM methode
def IBM(a, c, m, x_old):
	return (a * x_old + c) % m


# De IBM afleiding kan het volgende 'random' getal berekenen.
# parameters: x = k+1 en y = k
# return k + 2
def IBM_afleiding(x, y):
	return 6*x - 9*y	


def assignment2_1():

	x = np.random.uniform(0, 1, 500)
	y = np.random.uniform(0, 1, 500)
		
	plt.scatter(x, y, color='red')
	plt.title("Numpy: Random points between 0 and 1")
	    
	plt.show()


def assignment2_2():

	# de parameters
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

	# De eerste random getal wordt berekend voor beide seeds.
	print "Seed1 is: " + str(seed1)
	k1 = IBM(a, c, m, seed1)

	print "Seed2 is: " + str(seed2)
	k2 = IBM(a, c, m, seed2)

	# Vervolgend worden er 500 random getallen gegenereerd.
	for i in range(500):
		k1 = IBM(a, c, m, k1)
		x.append(k1 / float(m))

	for i in range(500):
		k2 = IBM(a, c, m, k2)
		y.append(k2 / float(m))

	# De getallen worden geplot als x en y coordinaten..
	plt.scatter(x, y, color='red')
	plt.title("IBM method : Random points between 0 and 1")
	    
	plt.show()


# In deze opdracht wordt bewezen dat je een 'random' getal van de IBM methode
# kan raden als je de twee vorige getallen weet.
def assignment2_3():

	# de parameters
	a = 65539
	c = 0
	m = 2**31

	# Een willekeurige seed.
	seed = 1
	
	# De eerste 3 randomgetallen die zijn berekend.
	k1 = IBM(a, c, m, seed)
	k2 = IBM(a, c, m, k1)
	k3 = IBM(a, c, m, k2)
	# De berekening die het juiste 'random' getal geeft wanneer het de twee
	# vorige getallen gebruikt.
	afl = IBM_afleiding(k2, k1)

	print "We hebben met de IBM methode een random getal berekend: " + str(k3)
	print 
	print """Als we nu deze \'random\' getal proberen te berekenen met de twee 
vorige \'random\' getallen dan krijgen we hetzelfde getal: """ + str(afl)


if __name__ == '__main__':
	
	assignment2_1()
	assignment2_2()
	assignment2_3()
