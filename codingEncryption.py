#GLOBAL VARIABLES
codeWords = []
realWords = []


#FUNCTIONS
def createCodeWords():
    codingWords = True

    while codingWords:
        print("Would you like to add a word to your code? (y/n)")
        answer = input().lower()
        if(answer == "y" or "yes"):
            print("What is the real word you would like to add?")
            real = input().lower()
            realWords.append(real)
            print("What would your code word be?")
            code = input().lower()
            codeWords.append(code)
            
        elif(answer == "n" or "no"):
             print("Your code has been saved!")
             codingWords = False

             print("Your code words are")
             print(codeWords)

             print("They correspond to")
             print(realWords)

        else:
            print("Security break! Abort mission")
            exit()

def encryptMessage():
    print()
    print("______________________")
    print()

    print("What is your message that you would like enrypted?")
    message = input().lower()
    wordList = message.split()

    codedMessage = ""
    for word in wordList:
        for realWord in realWords:
            print("Checking Words" + word + "and" + realWord)
            if(word == realWord):
                print("MATCH FOUND!")
                codedMessage = codedMessage + word + codeWords[0]
            else:
                codedMessage = codedMessage + word
                  


#RUNNING CODE
createCodeWords()
encryptedMessage()



        
