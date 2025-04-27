#number guessing game 

import random 

def number_guessing_game(): 
    
    print(" Welcome to The Number Guessing Game !! ")
    
    print(" I am thinking of a number between 1 and 100 ")
    
    #generate a random number 1 and 100
    
    Numberguess = random.randint(1,100)
    
    print(Numberguess)
      
   #start loop 
    
    while True : 
        
        guessnum = int(input("Enter your Guess: ")) #ask user to guess
        
        if guessnum<Numberguess : 
            
            print("Your guess is smaller than what I choose")
            
        elif guessnum>Numberguess :
            
            print("Your guess is greater than what i choose")
            
        else :
            
            print("you win")    
            
        
number_guessing_game() 