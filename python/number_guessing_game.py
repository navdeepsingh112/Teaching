# 1 - 100
# 5 chances 
# system ne sochia j usde brabar aaya ta tu c jit gye
# greater
# smaller
# Task starting ask difficulty level 1 , 2 ,3 , 4. 1- 10 chances number between 1 to 100 . 2 - 5 chances . 3 1 - 200 . 1 - 1000
#Task blackjack
import random
start = 1 
end =100
chances = 5
num = random.randint(start,end)
f= False
for i  in range(chances):
    guess = int(input("Guess the number between 1 to 100: "))
    if(guess == num):
        print("YAyyyyyyyyy you wonnnnn ")
        f = True
        break
    elif(guess > num):
        print("the number you have guessed is greater")
    elif(guess<num):
        print("the number you have guessed is smaller")
if(not f):
    print("the number to be guesses :" , num)