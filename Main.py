from Engine import Game
from colorama import Fore, Back, Style, init
from time import sleep
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King

#Initilizes colorama 
init()

def get_input(input_str):
    while 1:
        try:
            a = input(input_str)
            return a
        except:
            print("Error: Incorrect Input")
            pass

def print_board(str_board):
    checker_table = {0: Back.BLUE, 1: Back.BLACK}
    print(Style.BRIGHT)
    print(Fore.RED + Back.GREEN + "             ")
    for i in range(len(str_board) - 1, -1, -1):
        print(Fore.RED + Back.GREEN + " " + str(i + 1) + " ", end="")
        for j in range(0, len(str_board[i])):
            fore = Fore.GREEN
            back = checker_table[(i + j) % 2 == 0]
            if str_board[i][j].lower() == str_board[i][j]:
                fore = Fore.RED
            if str_board[i][j] == "-":
                print(fore + back + " ", end="")
            else: 
                print(fore + back + str_board[i][j], end="")
            if j == len(str_board) - 1:
                print(Back.GREEN, end="  ")
        print()
    print(Fore.RED + Back.GREEN + "             ")
    print(Fore.RED + Back.GREEN + "   ABCDEFGH  ")

if __name__ == "__main__":
    player_1 = get_input("Type player 1's name: ")
    player_2 = get_input("Type player 2's name: ")
    game = Game(player_1, player_2)
    while 1:
        Board = game.board.str_board()
        print_board(Board)
        if game.turn == "white":
            print(Style.RESET_ALL + "\n " + game.player_1 + "'s move: ", end="")
        else:
            print(Style.RESET_ALL + "\n " + game.player_2 + "'s move: ", end="")
        move = input().lower()
        move.strip()
        move = move.split()
        try:
            move_output = game.move_piece(move)
        except:
            pass
        if  move_output == False:
            print("\nNot a valid move.")
        if game.is_checkmate == True:
            print("\nCheck Mate!")
            if game.turn == "white":
                print("Black Wins!")
            else:
                print("White Wins!")
            answer = input("Want to play again? " )
            if "y" in answer.lower():
                game.reset_game()
            else:
                break
            
            
