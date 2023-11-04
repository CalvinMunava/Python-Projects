#function to check if each word has an 'e'
def has_n_e(w):
    hasE = False
    #loop through each character in word
    for c in w: #if e in w: return true else: false - one liner way to do for loop
        # if character = 'e' then return true
        if c == 'e':
            hasE = True
    return hasE

#read each line from text file in to array f
f = open("crossword.txt","r").readlines()
count = 0

#loop through each line in file by looping through array of lines f
for x in f:
    word = x[:-1] # read every iteration of array except last line (:-1)
    res = has_n_e(word) # get true or false for if word has 'e'
    if res == False:
        count = count + 1 #if has e = true add one to count for amount of words that have e

#calculate percentage of words that have 'e'
iAns = (count/len(f))*100 # len(f) returns amount of items in array f
rAns = round(iAns,2) # round percentage to 2 decimal places
sAns = str(rAns) # convert int to string
fAns = sAns + "%" # create string that says : xx.xx%
print(fAns) #print answer