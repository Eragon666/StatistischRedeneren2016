# Names:        Kwan Win Chung, Matthijs Thoolen & Younes Ouazref
# StudentIds:   10729585 , 10447822 & 10732519
# Group:        20
# File:         Naivebayes.py
#
# In this file the Naive Bayes is implemented.

import csv
import array
import numpy as np
from matplotlib import pyplot as plt

# Global arrays used for plotting.
male_weight_array = []
male_height_array = []
male_size_array = []

female_weight_array = []
female_height_array = []
female_size_array = []


def gauss_classifier(mu, sigma, bins):
    '''
    This function calculates the output of a Gaussian Distribution based on a given mu, binsize and sigma
    '''
    return (1/(np.sqrt((sigma**2) * 2 * np.pi))) * (np.exp( - (bins - mu)**2 / (2 * sigma**2) ))
  
  
def split_sex(dataset):
    '''
    Make two different datasets. One for male data the other for female data
    '''
    return {
        'M': [list(row)[1:] for row in dataset if row[0].strip() == 'M'],
        'F': [list(row)[1:] for row in dataset if row[0].strip() == 'F']
    }
    
    
def calc_mean_stdev(splitted_dataset):
    '''
    Generate an array with the calculated mean and standard deviation for each item (shoe shize, height and weight) and sex
    '''
    info = {
        'M': [],
        'F': []
    }
    
    for sex, data in splitted_dataset.iteritems():
        for col in zip(*data):
            info[sex].append(
                {
                    'mean': np.mean(col),
                    'stdev': np.std(col, ddof=1, dtype=np.float64)
                }
            )
            
    return info  
    
    
def calc_sex(info, weight, height, shoe_size):
    '''
    Calculate the gender of the input based on all the gathered data and the calculated training set
    '''

    # The chance that someone has gender X, we choose to use a 50/50 chance. But we also tried to
    # use the chance based on the given dataset. 
    male_prob = 0.5
    female_prob = 0.5

    # Compute the conditional probability using the Gaussian distribution
    male_weight_prob = gauss_classifier(info['M'][0]['mean'], info['M'][0]['stdev'], weight)
    male_height_prob = gauss_classifier(info['M'][1]['mean'], info['M'][1]['stdev'], height)
    male_size_prob = gauss_classifier(info['M'][2]['mean'], info['M'][2]['stdev'], shoe_size)

    female_weight_prob = gauss_classifier(info['F'][0]['mean'], info['F'][0]['stdev'], weight)
    female_height_prob = gauss_classifier(info['F'][1]['mean'], info['F'][1]['stdev'], height)
    female_size_prob = gauss_classifier(info['F'][2]['mean'], info['F'][2]['stdev'], shoe_size)

    # Save the probabilities in a global array.
    male_weight_array.append(male_weight_prob)
    male_height_array.append(male_height_prob)
    male_size_array.append(male_size_prob)

    female_weight_array.append(female_weight_prob)
    female_height_array.append(female_height_prob)
    female_size_array.append(female_size_prob)

    # Compute the probability
    prob_m = float(male_prob) * float(male_weight_prob) * float(male_height_prob) * float(male_size_prob)
    prob_f = float(female_prob) * float(female_weight_prob) * float(female_height_prob) * float(female_size_prob)

    prob_m = prob_m / (prob_m + prob_f)
    prob_f = prob_f / (prob_m + prob_f)

    return 0 if (prob_f > prob_m) else 1

def init_trainingset(dataset, j, shoe_size, weight, height):
    '''
    This function generates a training set for testing if someone is a male or female
    based on the given shoe_size, weight and height.
    The function handles both test items and user input tests.
    '''
    array_size = len(dataset)
    
    seperated = split_sex(dataset)
    
    info = calc_mean_stdev(seperated)

    male_count = len(seperated['M'])
    female_count = len(seperated['F'])
    
    # If shoe_size is not given, we must use the data from the test item
    if(shoe_size is None):
        weight = dataset[j][1]
        height = dataset[j][2]
        shoe_size = dataset[j][3]

    return calc_sex(info, weight, height, shoe_size)


def test_classifier(dataset):
    ''' 
    Test the accuracy of the classifier with the given dataset. For each item N-1 items are picked
    for the learn set. The other item is used for the test item, then a confusion matrix is populated and used
    to determine the success rate. 
    '''
    
    confusion_matrix = {
        'M': {
            'M': 0,
            'F': 0
        },
        'F': {
            'F': 0,
            'M': 0
        }
    }
    
    for i, data in enumerate(dataset):
        if(init_trainingset(dataset, i, None, None, None) is 1 and 'M' in data[0]):
            confusion_matrix['M']['M'] += 1
        elif(init_trainingset(dataset, i, None, None, None) is 1 and 'F' in data[0]):
            confusion_matrix['M']['F'] += 1
        elif(init_trainingset(dataset, i, None, None, None) is 0 and 'M' in data[0]):
            confusion_matrix['F']['F'] += 1
        elif(init_trainingset(dataset, i, None, None, None) is 0 and 'F' in data[0]):
            confusion_matrix['F']['M'] += 1

    print "The Confusion Matrix, classifier is on the x-axis, test on y-axis."    
    print np.array([
            ["    ", "Male", "Female"], 
            ["Male  ", confusion_matrix['M']['M'], confusion_matrix['M']['F']], 
            ["Female", confusion_matrix['F']['F'], confusion_matrix['F']['M']]
        ])


def user_input(data):
    '''
    Ask the user to input their height, weight and shoesize. Now create a trainingset with the
    given data and check if the user is a male or female according to the dataset. 
    '''
    height = float(raw_input("Weight (kilograms): "))
    weight = float(raw_input("Height (centimeters): "))
    size = float(raw_input("Shoe size: "))
    
    check = init_trainingset(data, None, size, height, weight)
    
    if(check is 0):
        print "Are you a female?"
    elif(check is 1):
        print "Are you a male?"
    else: 
        print "Are you sure your input is correct?" 


# This function plots the Probability density functions of the male and female
# for their weight, height and shoe size.
def plot():

    # Steps of 1/61 from 0 to 1.
    x = np.arange(0, 1, 1/61.0)

    # Plot the 3 figures.

    plt.hist(male_weight_array, 61, normed=True, color='blue')
    plt.hist(female_weight_array, 61, normed=True, color='red')
    plt.title("Probability density function of the weight")
    plt.legend(["male","female"])
    plt.show()

    plt.hist(male_height_array, 61, normed=True, color='blue')
    plt.hist(female_height_array, 61, normed=True, color='red')
    plt.title("Probability density function of the height")
    plt.legend(["male","female"])
    plt.show()

    plt.hist(male_size_array, 61, normed=True, color='blue')
    plt.hist(female_size_array, 61, normed=True, color='red')
    plt.title("Probability density function of the shoe size")
    plt.legend(["male","female"])
    plt.show()


def main():
    # Load the file into an array
    data = np.genfromtxt('biometrie2014.csv', delimiter=',', skip_header=5, dtype=None)

    while True:
        user_option = (raw_input("Do you want to do a manual test? Y/N \n"))

        if(user_option == 'Y'):
            user_input(data)
            break 
        elif(user_option == 'N'):
            test_classifier(data)
            plot()
            break
        else:
            print "Wrong input, try again"
        
if __name__ == '__main__':
    main()
