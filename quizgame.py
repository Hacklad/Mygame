print("Welcome to my computer quiz!")

playing = input("Do you want to play, Yes or No?  ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score, scored = 0, 0

answer = input("What does CPU stand for? ")
scored += 1
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    print('Your score is currently ', score, 'out of', scored )
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
scored += 1
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
    print('Your score is currently ', score, 'out of', scored )
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
scored += 1
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
    print('Your score is currently ', score, 'out of', scored )
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
scored += 1
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
    print("You scored ",score, "out of 4")
else:
    print("Incorrect!")
