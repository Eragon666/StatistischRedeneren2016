# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# File:         Inverse_Transform_Sampling.py
#


import numpy as np
import math
from matplotlib import pyplot as plt

lamda = 1
random_list = []

# The main loop that generates random numbers
for i in range(1000000):
    random_number = np.random.uniform()
    result = math.fabs((1/lamda) * math.log(random_number))
    random_list.append(result)

# estimate lambda
mean_x = np.mean(random_list)
lambda_schatting = 1/mean_x
print 'Estimated lambda', lambda_schatting

# Plot all the random numbers in a histogram.
bins = 8
plt.hist(random_list, bins, range=[0, bins], normed=True)
plt.show()