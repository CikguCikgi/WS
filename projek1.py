import time
print("***************************************************")
#Welcome the user
print("Welcome to the Football Facts EURO 2024!")
time.sleep(1)
print("***************************************************")

#Chances
chances=1
print("You have to pick", chances,"correct answer.\nYou will get 1 score if you pick a correct answer.\n")
time.sleep(1.5)

#score
score=0

#question 1
print("==================================================")
question_1=print("1) WHO IS THE MOST APPEARANCE PLAYER IN EURO 2024?\n(A) CHRISTIANO RONALDO\n(B) LIONEL MESSI\n(C) WAYNE ROONEY\n(D) JOHN TERRY\n\n")
answer_1= "a" 

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("CORRECT! SIUUUUU!!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(1.5)

#question 2
print("==================================================")
question_2 = print("2)WHAT IS THE OFFICIAL NAME OF EURO 2024 MASCOTT?\n(A) SIMBA\n(B) ALBART\n(C) ROCK\n(D) MIGUEL\n\n")  
answer_2 = "b"

for i in range(chances):
    answer = input("answer: ")
    if (answer.lower() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3)  WHAT IS THE OFFICIAL EURO 2024 SONG?\n(A) WATER\n(B) SOIL\n(C) FIRE\n(D) TREE\n\n")
answer_3= "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4)  WHERE WILL THE FINAL OF EURO 2024 BE PLAYED?\n(A) Munchen Stadium\n(B) Cologne Stadium\n(C) BVB Stadium Dortmund\n(D) BERLIN'S Olympiastadion\n\n")
answer_4= "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#question 5
print("==================================================")
question_5 =print("5)  HOW MANY STADIUMS ARE THERE IN EURO 2024?\n(A) 10\n(B) 11\n(C) 12\n(D) 13\n\n")
answer_5= "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_5, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
while score >=2:
    print("GOAALLL! YOUR SCORE WAS", score)
    break

while score <2:
    print("KEEP THE FACTS RIGHT ! YOUR SCORE WAS",score)
    break

#Goodbye message
print("THANK YOU FOR PLAYING THE EURO 2024 QUIZ GAME!")
