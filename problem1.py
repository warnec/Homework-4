#Colston Warne
#Problem 1
#Homework 4

def volume(first, second, third):
    badflag = False
    # check for zero width
    if first == 0:
        print("The first value was zero which is impossible!")
        badflag = True
    if second == 0:
        print("The second value was zero which is impossible!")
        badflag = True
    if third == 0:
        print("The third value was zero which is impossible!")
        badflag = True

    # check for negative width
    if first < 0:
        print("The first value was negative which is impossible!")
        badflag = True
    if second < 0:
        print("The second value was negative which is impossible!")
        badflag = True
    if third < 0:
        print("The third value was negative which is impossible!")
        badflag = True

    result = first * second * third

    #make sure we didnt get a bad value
    if (badflag == False):
        return result


def main():
    try:
        print("Please enter the first value")
        first = float(input())
        print("Please enter the second value")
        second = float(input())
        print("Please enter the third value")
        third = float(input())
        result = volume(first, second, third)
        print("\nThe result is: \n")
        print(result)

    except ValueError:
        print("You must enter a float with no spaces!")
main()



