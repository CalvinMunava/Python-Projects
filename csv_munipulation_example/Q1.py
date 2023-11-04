print("Please enter three stick lengths...")
#get the three length for each side(stick)
stick1 = input("Stick 1 length: ")
stick2 = input("Stick 2 length: ")
stick3 = input("Stick 3 length: ")
isTriangle = ""
# create function to check if sticks make up a triangle
def is_triangle(s1,s2,s3):
    res = "No"
    isDigit1 = False
    isDigit2 = False
    isDigit3 = False
    #loop through inputs to scheck if all inputs are a valid number
    while (isDigit1 == False) or (isDigit2 == False) or (isDigit3 == False):
        #if input is a digit set isDigit to true
        if s1.isdigit() == True:
            isDigit1 = True
        #else request new input again
        else:
            print ("Please type in an integer number.")
            s1 = input("Stick 1 length: ")

        #if input is a digit set isDigit to true
        if s2.isdigit() == True:
            isDigit2 = True
        #else request new input again
        else:
            print ("Please type in an integer number.")
            s2 = input("Stick 2 length: ")

        #if input is a digit set isDigit to true
        if s3.isdigit() == True:
            isDigit3 = True
        #else request new input again
        else:
            print ("Please type in an integer number.")
            s3 = input("Stick 3 length: ")

    #connvert values to int here
    side1 = int(s1)
    side2 = int(s2)
    side3 = int(s3)
    #check if all values are equal
    if side1 + side2 > side3:
        if side1 + side3 > side2:
            if side2 + side3 > side1:
                res = "Yes"
            
    #return res (true or false)
    return res

#call is triangle function
isTriangle = is_triangle(stick1, stick2, stick3)
#print if triangle or not
print(isTriangle)