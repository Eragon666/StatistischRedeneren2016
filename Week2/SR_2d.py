# Names:			Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# Studentnumbers: 	10729585 , 10447822 & 10732519
# group: 20
# File: SR_2d.py
# 
# Comments: In deze file staat de implementatie voor opdracht 2d van de tweede
# week van Statistisch Redeneren.


import random
import numpy as np

# In de bin functie wordt voor een random waarde van p gekeken of de som van
# de kansen nog steeds gelijk aan 1 is.

def bin():
	# Neem een willekeurig getal tussen 0 en 1.
	r = random.randint(0, 100)
	p = (r / 100.0) 

	# Geef het aantal keer gooien van het muntstuk aan.
	n = 1000000

	# Bereken de kans voor munt.
	k = p
	comb = np.random.binomial(n, k)
	ans = comb

	# Bereken de kans voor kop.
	k = 1 - p
	comb = np.random.binomial(n, k)
	ans2  = comb

	# Bereken de som van de kansen. Want alle kansen waren bij elkaar opgeteld.
	returnWaarde = float(ans + ans2)/n
	return returnWaarde

def main():
	
	# Herhaal het kansexperiment voor een groot aantal keer. 
	temp= 0
	getal = 1000000
	for i in range(getal):
		temp = temp + bin()

	# Print de gemiddelde som van de kansen per beurt gooien. 
	print "De gemiddelde som van de kansen per beurt gooien: " + str(temp / getal)

if __name__ == '__main__':
	main()