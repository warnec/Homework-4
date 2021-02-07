#Colston Warne
#HW 4
#Problem 2

def listAvg(list):
    #see if list has no elements
    badFlag = False
    if (len(list) == 0):
        badFlag = True
        print("There are no elements in this list!")
        return None

    #see if the list average is zero
    if (sum(list) == 0):
        badFlag = True
        print("The sum of this list is zero and cannot be averaged!")
        return None

    #otherwise return the average of the list
    if(badFlag == False):
        result = sum(list) / len(list)
        return result