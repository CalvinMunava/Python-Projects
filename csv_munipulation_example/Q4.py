import csv #import py library for csv files
import pandas as pd #import py library for pandas (arrays)
import numpy as np #import numpy 
import matplotlib.pyplot as plt #import mat plot lib nfor plotting graphs

tips = pd.read_csv('tips.csv') #read csv file into a panda

print('Original shape:')
print(tips.shape) #print row and col values (r, c)
print('')

tips['tip_percentage'] = round((tips['tip'] / tips['total_bill'] * 100),2) #create new col called 'tip_percentage' from calculation of other 2 cols
#tips.to_csv('addedColumn.csv', index = False)

print('After addition of calculated column:')
print(tips.shape) #print row and col values (r, c)
print('')

smokers = tips[tips.smoker.eq('Yes')] # create subset of tips called 'smokers' by taking out all rows that are from non smokers
#did this to calculates all data of customers who are smokers

print('Smokers tips:')
print(smokers.shape) #print row and col values (r, c)
print('')

corr = np.corrcoef(tips['total_bill'], tips['tip'])[0, 1] # calculate correlation coef of total_bill and tip
sig = 'Significant'
if (-0.8 < corr < 0.8 ): #chack is significant or not
    sig = 'Insignificant'

print(sig + ' correlation: ' + str(corr)) # print if significant

#funtion to plot graph
def plot_bar():
    grouped = tips.groupby(['day'])['total_bill'].mean() #groupby day column and calculate mean for total_bill per day
    grouped.plot.bar(x = 'day', y = 'total_bill') #plot bar graph
    plt.xlabel('Day', fontsize = 10) # cahnge x label of graph
    plt.ylabel('Average bill price ($)', fontsize = 10) # change y label of graph
    plt.title('Average price paid for a meal per day', fontsize=14) # give graph a title
    plt.show() #display graph

plot_bar() # call function