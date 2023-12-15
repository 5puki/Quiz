#first we welcome the users
print("Welcome to the stage!")

#next we need some user input
user = input("Do you wish to continue? Yes/No: ").lower()

#next we check if the user said yes and implement an exit if they say no
if user != "yes":
    print("No worries then. Goodbye!")
    quit()

#welcome the users who said yes and start a score system
print("Cool, lets play! :)")
score = 0

#lets start with the questions and check right away for the correct answers
answer = input("What does a CPU stand for?: ").lower()
if answer == "central processing unit":
    print("CORRECT!")
    score += 1
else:
    print("WRONG!")

answer = input("What does a GPU stand for?: ").lower()
if answer == "graphics processing unit":
    print("CORRECT!")
    score += 1
else:
    print("WRONG!")

answer = input("What does a RAM stand for?: ").lower()
if answer == "random access memory":
    print("CORRECT!")
    score += 1
else:
    print("WRONG!")

#last thing is to check what the user scored and to grade them upon it
points = round((score / 3) * 100)
print("You have scored " + str(points) + "%")
if points == 100:
    print("grade: A")
elif points == 67:
    print("grade: B")
elif points == 33:
    print("grade: C")
else:
    print("grade: F")