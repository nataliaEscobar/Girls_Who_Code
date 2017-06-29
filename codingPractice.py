from random import randint

#FUNCTIONS

def level1(numlist):
    counter = 0
    for num in numlist:
        if num %5 == 0:
            counter +=1
    return counter
    print(level1(numlist))

def level2(numlist):
    numSum = 0

    for num in numlist:
        if num %3 ==0 or num %5 ==0:
            print(num)
            numSum += num
    print("Final sum:")
    print(numSum)


def level3(numlist):
    primeSum = 0

    #part 1: iterate through the list
    for num in numlist:

        prime = True
    #part 2: determine if a prime number
        for x in range(2,num):
            if num % x == 0:
                prime = False

        if prime == True:
            primeSum += num

    #part 3: add to the sum
    print("Final number")
    print(primeSum)
    
#RUNNING CODE
    
#generates random list of number
numlist = []
for x in range (100):
    num = randint(10,99)
    numlist.append(num)

#level2(numlist)
level3(numlist)

##print(numlist)
