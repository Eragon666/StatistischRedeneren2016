# Opgave 4.7
# Door: Younes Ouazref (10732519),
# 		Kwan Win Chung (10729585), 
# 		Matthijs Thoolen (10447822)
# Datum: 12-05-2016

from pylab import *
import numpy as np
from sklearn import svm, grid_search, cross_validation

# read the natural spectra and make it into a set for classification
# the colors found in the dataset

Colors = ['black', 'blue', 'brown', 'gray',
		'green', 'orange', 'pink', 'red',
		'violet', 'white', 'yellow']


# does a line of text contains a color name?
def containsColor( line ):
	for c in Colors:
		if line.find(c)>=0:
			return Colors.index(c), c
	return None, None


# read the file and store spectra in matrix D (rows are the spectra)
# and the classes in vector y
fp = open("natural400_700_5.asc")
lines = fp.readlines()

D = zeros((0, 61))
y = array([])

for i in range(0,len(lines), 2):
	ind, c = containsColor(lines[i])
	if ind is not None:
		d = fromstring(lines[i+1],dtype=int,sep=" ")
		D = append(D,array([d]),axis=0)
		#print d
		#print D
		y= append(y,ind)
		
# calculate the parameters for the Grid Search
C = 10.0 ** np.arange(-4, 4)
gamma = 10.0 ** np.arange(-4, 4)

# Add the kernel, C range and gamma range together
params = {'kernel':['rbf', 'linear'], 'C':C.tolist(), 'gamma':gamma.tolist()}

# We need a training set of 80 percent and a test set of 20 percent.
train_X, test_X, Y_train, test_Y = cross_validation.train_test_split(D, y, test_size=0.2, random_state=0)

svr = svm.SVC()

# With the help of grid search we can find the optimal parameters
clf = grid_search.GridSearchCV(svr, params)
clf.fit(train_X, Y_train)

print 'Beste estimator gevonden: ', clf.best_estimator_
result = clf.predict(test_X)

# Compute score for the classification of our test set
count = 0.0
for x in range(len(result)):

    if result[x] == test_Y[x]:
        count += 1

print int(count), 'van de', len(result), 'correct geclassificeerd. De succes ratio is dan:', ((count / len(result)) * 100.0), '%'
