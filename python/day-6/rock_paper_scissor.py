import random as rand

options = ["rock","paper","scissor"]

# Generates Random Response from Computer 
def generate_computer_response():
    return options[rand.randint(0, 2)]

# Game Logic for the rock, paper and scissor game
def game_logic(user_res):
    computer_points = 0 
    user_points = 0
    computer_response = generate_computer_response()
    user_response = user_res
    
    if user_response == "rock" and computer_response == "rock" or user_response == "paper" and computer_response == "paper" or user_response == "scissor" and computer_response == "scissor":
        print(f"Computer chose {computer_response} and you chose {user_response}")
        computer_points+= 0
        user_points+= 0
    elif user_response == "rock" and computer_response == "scissor" or user_response == "paper" and computer_response == "rock" or user_response == "scissor" and computer_response == "paper":
         print(f"Computer chose {computer_response} and you chose {user_response}")
         computer_points+=0
         user_points+=10
    elif computer_response == "rock" and user_response == "scissor" or computer_response == "paper" and user_response == "rock" or computer_response == "scissor" and user_response == "paper":
         print(f"Computer chose {computer_response} and you chose {user_response}")
         user_points+=0
         computer_points+=10
    return (computer_points,user_points)
    
