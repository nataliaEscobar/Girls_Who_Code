myContact = {}
myContact = {"Emergency":"911", "Home": "(323)895-3370"}

addContact = True
addNumber = True
addAddress = True

while addContact == True:
    print("Would you like to add a contact? (y/n)")
    answer = input().lower()
    if (answer == "yes" or "y"):
        list1 = []
        print("What is the name?")
        name = input()
        
        
    elif(answer == "no" or "n"):
        print("Your contact book has been updated!")
        addContact = False
    else:
        print("Please enter 'yes' or 'no'")

while addNumber == True:
    print("Would you you like to add a phone number? (y/n)")
    num = input().lower()
    if (answer == "yes" or "y"):
        print("What is the number?")
        num = int(input())
        list1.append(num)
    elif (answer == "no" "n"):
        addNumber = False
    else:
        print("Please enter 'yes' or 'no'")
    

while addAddress == True:
    ("Would you like to add an address?(y/n)")
    answer2 = input()
    if (answer2 == "yes" or "y"):
        print("What is the address?")
        address = input()
        list1.append(address)
    elif(answer == "no" or "no"):
        print("Okay, here is you contact book.")
        addContact = False
    else:
        print("Please enter 'yes' or 'no'")

myContact[name]= list1

print("My Contact Book:")
print()

for item in myContact:
    print("Contact Name:" + item)
    name = myContact[item]
    defineType = type(name)

    if (defineType == str):
        print("Phone Number:")
        print(myContact[item])
    elif (defineType == int):
        print("Address:")
        print(myContact[item])

    elif(defineType == list):

        for x in number:
            print("- " + x)
    print()
    
    







        
    
