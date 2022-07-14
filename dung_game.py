import random
import os



# draw grid
# pick random location for the player
# pick random location for the exit door
# pick random location for the monster
# draw player in the grid
# take input or movement
# move player , unless invalid move (past edges of grid)
# check for win/lose
# clear screen and random grid

celss = [
(0,  0) , (1 , 0) , (2 , 0) , (3 , 0) , (4 , 0),
(0,  1) , (1 , 1) , (2 , 1) , (3 , 1) , (4 , 1),
(0,  2) , (1 , 2) , (2 , 2) , (3 , 2) , (4 , 2),
(0,  3) , (1 , 3) , (2 , 3) , (3 , 3) , (4 , 3),
(0,  4) , (1 , 4) , (2 , 4) , (3 , 4) , (4 , 4)

]

def clear_screen():
    os.system('cls')

def get_location():
    return random.sample(celss , 3)

def move_player(player , move):
    x , y = player
    if move == 'RIGHT':
        x += 1
    if move == 'LEFT':
        x -= 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    
    return x , y

def get_move(player):

    moves = ["RIGHT", "LEFT", "UP" , "DOWN"]

    x , y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in celss:
        x , y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                outpout =   tile.format("X")
            else:
                outpout = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                outpout = tile.format("x")
            else:
                 outpout = tile.format("_|")
        print(outpout , end = line_end)

def game_loop():
    player , monster , door = get_location()
    playing = True
    while playing:
        clear_screen()
        draw_map(player)
        valid_move = get_move(player)

        print("you're currently in room {}".format(player))
        print("you can move {}".format(", ".join(valid_move)))
        print("enter 'QUIT' to quit !")

        move=input("> ")
        move=move.upper()

        if move == 'QUIT':
            break
        if move in valid_move:
            player = move_player(player, move)
            if player == monster:
                print("\n ** OH NO! the monster got you ** \n")
                playing = False
            if player == door:
                print("\n ** YES! you won :))) ** \n")
                playing = False
        else:
            input("\n ** walls are hard! don't run into then ** \n")
        
    else:
        input("paly again? [y/n]").lower() != 'n'
        game_loop()

clear_screen()
print("welcome to game :)")
input("press 'return' to start! ")
clear_screen()
game_loop()
    