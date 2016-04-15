# Names:            Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# Studentnumbers:   10729585, 10447822 & 10732519
# Group:            20
# File:             SR_3.py
# 
# Comments: In deze file staat de derde opdracht van week 2 van 
# Statistisch Redeneren.

# Hier hebben we onze inspiratie voor de code.
# http://docs.scipy.org/doc/scipy-0.17.0/reference/generated/scipy.stats.norm.html


from matplotlib import pyplot as plt
from scipy import stats
import scipy as sp


# We nemen een stapgrootte van 100 tussen -10 en 10
x = sp.linspace(-5.0, 5.0, 100)

# Met pdf kunnen we de kansdichtheid berekenen.
pdf = stats.norm.pdf(x)

# Met cdf kunnen we de verdeling berekenen.
cdf = stats.norm.cdf(x)

# Trek 1000 getallen uit de standaard normaal vergelijking
histogram = stats.norm.rvs(loc=0, scale=1, size=1000)

# De titel van het plaatje.
plt.title("Opdracht 3")
# Print het histogram
plt.hist(histogram, 30, normed=True)
# plot de pdf en cdf lijnen.
plt.plot(x, pdf, 'g-')
plt.plot(x, cdf, 'r-')
# Legenda
plt.legend(["Kansdichtheid","Verdeling"])
plt.show()
