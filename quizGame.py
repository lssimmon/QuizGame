# Author: Lauryn Simmons
# Date: 
# Description:
# Inspired by: 

# imports the arrays of questions and answers
from qna import *
import time
userInput = "temp"
print("Welcome to my quiz game!") 
time.sleep(2)
while(userInput != "exit"):
    
    # prompts user
    print()
    print("start -> begin quiz")
    print("add -> add more questions")
    print("del -> delete question")
    print("exit -> terminates program")

    userInput = input().lower()


    if userInput == "start":
        temp = 0
        score = 0
        while temp < count:
            userInput = input(questions[temp] + ": ").lower()
            if userInput == answers[temp]:
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect:(")
            temp = temp + 1

        print("Congrats! You got " + str(score) + " out of " + str(count) + " questions correct!")
        time.sleep(3)
        
    elif userInput == "add":

        print("Input question to be added: ")
        userInput = input().lower()
        questions = questions + [str(userInput)]

        print("Input answer to question: ")
        userInput = input().lower()
        answers = answers + [str(userInput)]

        count = count + 1

    elif userInput == "del":
        temp = 0
        while( temp < count):

            print(str(temp)+ ": " + str(questions[temp]))
            temp = temp + 1

        userInput = input("Enter the number of the question you want to delete: ")

        del questions[int(userInput)]
        del answers[int(userInput)]

    elif userInput == "exit" :

        print("Goodbye")

    else :

        print("invalid input...try again.")

# saves updated question and answer set to qna.py
file = open("qna.py", "w")
file.write("questions = " + str(questions) + "\n")
file.write("answers = " + str(answers) + "\n")
file.write("count = " + str(count) + "\n")
file.close()







