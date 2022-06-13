import random

outcomes = ["R","P","S"]

while True:
    #This asks for user input
    user_input = input("Please enter an input R/P/S").upper()
    
    #next line validates user input
    
    if user_input == "R" or user_input=="S"or user_input=="P":
        
        Computer = random.choice(outcomes)
        
        if user_input == Computer:
            print("This is a tie")
            
            continue
        elif user_input=="R" and Computer=="S":
            print("Player wins")
            break
        
        elif user_input == "S" and Computer=="R":
            print("CPU wins")
            break
        
        elif user_input == "P" and Computer=="R":
            print("Player wins")
            break
        
        elif user_input == "R" and Computer=="P":
            print("CPU wins")
            break
        
        elif user_input == "S" and Computer=="P":
            print("Player wins")
            break
        
        elif user_input == "P" and Computer=="S":
            print("CPU wins")
            
    else :
         print("Error, invalid entry. Enter a valid option!")
         continue
    
        
        
        
        
            
            
            
         
         
      
        
        
    
    
    