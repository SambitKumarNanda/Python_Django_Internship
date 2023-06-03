from rock_paper_scissor import game_logic

want_to_play = 0

while(want_to_play == 0):
    print("Welcome to Rock, Paper and Scissors Game: ")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print()

    player_name = input("Please Enter your name: ")
    no_of_turns = int(input(f"{player_name} what is the number of rounds you want to play: "))
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    
    c_total = 0
    u_total = 0
    
    while(no_of_turns != 0):
        user_res = input("Choose rock, paper, or scissor: ")
        result = game_logic(user_res)
        c_point,u_point = result
        c_total+= c_point
        u_total+= u_point
        print(f"{player_name} gets {u_point} points and computer gets {c_point} points")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print()
        no_of_turns-=1
        
    comp_point,us_points = result
    
    
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    if c_total > u_total:
        print(f"{player_name} loses and Computer wins")
    elif c_total < u_total:
        print(f"{player_name} wins computer loses")
    else:
        print(f"Its a draw between {player_name} and computer")
        
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    want_to_play = int(input("Do you want to play again\n 0: for yes\n 1: for no\n"))