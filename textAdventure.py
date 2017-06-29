print("Welcome to the Carnival!")
print("You must be hungry! We have cotton candy, snow cones, and popcorn.")
print("You have 10 tickets... choose wisley and have fun!")

print("What are you craving?")

choosingFood = True
foodChoice = ""
ticket = 10

while choosingFood == True:
    foodChoice = input()

    if (foodChoice == "cotton candy"):
        if (ticket == 0):
            print("NO MORE TICKETS!")
            choosingFood = False
        elif (ticket < 2):
            print("Not enough tickets!")
            print("Sorry.")
            choosingFood = False
            
        print("Welcome to the cotton candy stand!")
        print("We have pink and blue, which one would you like? Each is 2 tickets")
        print("For pink, type 'p'. For blue, type 'b'.")

        ccChoice = input()
        if(ccChoice == 'p'):
            print("Nice choice! That is so Pinky Pink!")
            ticket = ticket - 2
            print("You have %d left" %(ticket))
            print("Are you still hungry? (y/n)")
            moreFood = input()
            if (moreFood == 'y'):
                print("What else are you craving?")
            elif(moreFood == 'n'):
                print("Thank you for visiting the Carnival!")
        elif(ccChoice == 'b'):
            print("Cool blue!")
            ticket = ticket - 2
            print("You have %d left" %(ticket))
            print("Are you still hungry? (y/n)")
            moreFood = input()
            if (moreFood == 'y'):
                print("What else are you craving?")
            elif(moreFood == 'n'):
                print("Thank you for visiting the Carnival!")
            

    elif(foodChoice == "snow cones"):
        if (ticket == 0):
            print("NO MORE TICKETS!")
            choosingFood = False
        elif (ticket < 3):
            print("Not enough tickets!")
            print("Sorry.")
            choosingFood = False
        print("Welcome to the snow cone stand. It sure is a hot day, why not cool down with a cone!")
        print("Do you want a rainbow cone?")
        print("If you want rainbow type 'r'. If not type 'n'")

        flavorChoice = input()
        if(flavorChoice == 'r'):
            print("What a colorful cone!")
            ticket = ticket - 3
            print("You have %d left" %(ticket))
        elif(flavorChoice == 'n'):
            print("How boring.")
            ticket = ticket - 3
            print("You have %d left" %(ticket))

        print("Are you still hungry? (y/n)")
        moreFood = input()
        if(moreFood == 'y'):
            print("What else are you craving?")
        elif(moreFood == 'n'):
            print("Thank you for visiting the Carnival!")
            

    elif(foodChoice == "popcorn"):
        if (ticket == 0):
            print("NO MORE TICKETS!")
            choosingFood = False
        elif (ticket < 1):
            print("Not enough tickets!")
            print("Sorry.")
            choosingFood = False
        print("Welcome to the popcorn stand! Would you like a bag?")
        print("We have two flavors, caramel and kettle. What would you like?")
        print("If you want caramel type 'c'. If you want kettle type 'k'.")
        
        popChoice = input()
        if(popChoice == 'c'):
            print("What a sweet choice!")
            ticket = ticket - 1
            print("You have %d left" %(ticket))
        elif(popChoice == 'k'):
            print("Classic!")
            ticket = ticket - 1
            print("You have %d left" %(ticket))

        print("Are you still hungry? (y/n)")
        moreFood = input()
        if(moreFood == 'y'):
            print("What else are you craving?")
        elif(moreFood == 'n'):
            print("Thank you for visiting the Carnival!")
            




