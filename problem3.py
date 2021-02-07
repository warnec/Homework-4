#Colston Warne
#Homework 4
#problem 3
#this site was used as reference for the isinstance method https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/

def combineStrings(str1, str2):

    #see if the first string is valid
    if(isinstance(str1,str)):
        first = str1
    else:
        print("The first input was not a string!")
        return None

    #see if second string is valid
    if (isinstance(str2, str)):
        second = str2
    else:
        print("The second input was not a string!")
        return None
    #see if strings are empty
    if (len(str1) == 0):
        print("The first string is empty!")
        return None
    if(len(str2) == 0):
        print("The second string is empty!")
        return None
    #combine them
    final = first + second
    return final

