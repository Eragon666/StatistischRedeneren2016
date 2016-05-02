# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# 
# Comments: In deze file is de code voor opdracht PCA: 5.3 van lab 4 gemaakt.


from pylab import *
import numpy as np
import matplotlib.pyplot as plt


# Functie leest het plaatje in en laat het ook zien bij het uncommenten
# van de stukjes code.
def readIn():

	a = imread('data/trui.png')

	# figure(1)
	# subplot(1,2,1)
	# imshow(a, cmap=cm.gray)

	d = a[100:125,100:125]

	# subplot(1,2,2)
	# imshow(d, cmap=cm.gray)
	# plt.show()

	return a, d

# Deze funcite berekend de covariance 
def covariance(im, detail):

	# Neem de afmetingen van de image.
	l1, r1 = im.shape
	# Neem de afmetingen van de detail.
	l2, r2 = detail.shape

	# S is een 625 * 625 matrix, nu even gevuld met nullen.
	S = zeros((l2 * r2, l2 * r2))

	# Manier om het aantal details te berekenen.
	l = l1 - l2 + 1
	r = r1 - r2 + 1
	aantalDetails = l * r # 53824

	# Vul de array met waarden uit de originele image. De forloops loopen
	# 231 * 231 keer over de waarden heen.
	# De berekeningen komen uit de pdf van de opdracht.
	for x in range(l1 - l2):
		for y in range(r1 - r2):
			# Neem de hoeveelheid die is gegeven van de detail en stop die in xi.
			xi = im[x : (x + l2), y : (y + r2)].reshape(l2 * r2, 1)
			# Neem de dot product van xi en xi transpose.
			S += np.dot(xi, xi.transpose())

	# de covariance S = X*X^t / (N - 1)
	S /= float(aantalDetails - 1)

	return S


# Gegeven in het document. Berekend de eigenwaardes.
def sortedeig(M):
	d, U = eig(M)
	si = argsort(d)[-1::-1]
	d = d[si]
	U = U[:,si]
	return (d,U)

# Plot de scree diagram. De eerste 25 eigenvalues worden weergegeven.
# (De rest van de eigenwaardes is bijna niet meer te zien.)
def plot_scree_diagram(d):

	# Maak een array met waarden 0,..,24
	x = []
	for i in range(25):
		x.append(i)
		
	fig1 = plt.figure()
	# d is gerangschikt van hoog naar laag.
	plt.plot(x, d[0:25])
	plt.show()


if __name__ == '__main__':

	print "De code runt nu dit kan even duren."

	im, detail = readIn()
	X = covariance(im, detail)
	mean = np.mean(X, dtype=np.float64)
	d, U = sortedeig(X)
	# Plot de scree diagram
	plot_scree_diagram(d)
