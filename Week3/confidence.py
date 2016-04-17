# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# File:         confidence.py
#
# In deze file is de confindence opdracht geimplementeerd.


import numpy as np
import random


tijden = []
n = 50

# Deze functie leest het bestand in en stopt het in de lijst tijden.
def readIn():

	# Probeer de file te openen.
	try:
		with open('tijden-medium.log') as f:
			content = f.readlines()
	except:
		return 0

	# Stop de getallen in de list tijden.
	for i in range(len(content)):
		tijden.append(float(content[i]))


# In deze file worden willekeurige tijdseenheden uit de file genomen.
def randomPick():

	steekproef = []

	for i in range(n):
		steekproef.append(random.choice(tijden))

	return steekproef


# Deze functie berekend de betrouwbaarheidsintervallen en checked of 
# mu er tussen zit.
def betrouwbaarheids(gemiddelde_populatie):

	steekproef = randomPick()
	# Bereken het gemiddele en standaarddeviatie.
	mu = np.mean(steekproef)
	var = np.std(steekproef)

	# De waarde voor alpha staat op deze pagina. Het verschilt per percentage.
	# https://en.wikipedia.org/wiki/Confidence_interval#Basic_Steps
	alpha = 1.96

	linker_grens = (mu - alpha * (var / np.sqrt(n)))
	rechter_grens = (mu + alpha * (var / np.sqrt(n)))

	print "Linkergrens = " + str(linker_grens) + " en de rechtergrens = " + str(rechter_grens)
	print "gemiddelde van de populatie (mu) = " + str(gemiddelde_populatie)

	if((linker_grens <= gemiddelde_populatie) & (gemiddelde_populatie <= rechter_grens)):
		print "Mu zit in de betrouwbaarheidsinterval.\n"
		return 1
	else:
		print "Mu zit niet in de betrouwbaarheidsinterval.\n"
		return 0

if __name__ == '__main__':

	if(readIn() == 0):
		print "Kon de file niet openen. Check of de file met de waarden en file met de code in dezelfde map zitten."
	else:
		aantal = 0

		# De mu van de gehele populatie.
		gemiddelde_populatie = np.mean(tijden)
		# print "gemiddelde van gehele populatie " + str(gemiddelde_populatie)

		# Herhaal de steekproef 100 keer. En hou bij hoe vaak het goed gaat.
		for i in range(100):
			aantal += betrouwbaarheids(gemiddelde_populatie)
		print "Aantal keren dat mu in het betrouwbaarheidsinterval zit is " + str(aantal) + "/100"
