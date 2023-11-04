import csv #import py library for csv files
import pandas as pd #import py library for pandas (arrays)

data = pd.read_csv('duplicate.csv') #read csv file into a panda
r,c  = data.shape #calculate amount of rows (r) and columns (c) in panda

noDup = data.drop_duplicates() #create new panda woth no duplicate rows
rr,cc  = noDup.shape #calculate amount of rows (rr) and columns (cc) in new panda

noDup.to_csv('duplicates_removed.csv', index = False) #create csv file with no duplicates by exporting new panda to csv file
str = 'duplicates_removed.csv created with ' + str(rr) + ' records.' #create output string

dup_count = r - rr #calculate amount of duplicate rows

#print output
print ('Original CSV records:')
print (r)
print('')
print ('Number of duplicates:')
print (dup_count)
print('')
print (str)

            