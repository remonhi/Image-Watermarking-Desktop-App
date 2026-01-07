# - Import modules to follow my CONVENTIONS 

import art               # - for ASCII art
import os                # - for OS commands to clear the screen
import sys               # - for system-specific parameters and functions
import requests          # - for making HTTP requests
import random            # - for random number generation
import time              # - for time-related functions

# - Define "global" variables and functions.

ttt = "Tic Tac Toe" 
board = []
game = "NEW" 
computer_symbol = ""
user_symbol = ""
coin = ""      
flip = ""
turn = ""

def coin_flip(pick):

    iss_dict = api_request(url=iss_url, params=iss_parms)

    if isinstance(iss_dict, dict):
        heads = float(iss_dict["iss_position"]["latitude"])
        tails = float(iss_dict["iss_position"]["longitude"])

    if pick in ["H", "HEADS"]:
        last_digit = str(heads).split('.')[-1][-1]
        last_digit = int(last_digit)
        if last_digit % 2 == 0:
            result = "HEADS"
        else:
            result = "TAILS"
    else:
        last_digit = str(tails).split('.')[-1][-1]
        last_digit = int(last_digit)
        if last_digit % 2 == 0:
            result = "TAILS"
        else:
            result = "HEADS"

    return result

def print_board(choice=None, symbol=None):

    if symbol:   #? udpating with a choice and symbol are provided
        for row in range(3):
            for col in range(3):
                if board[row][col] == str(choice):
                    board[row][col] = symbol

    for row in range(3): #? print the board
        print(f" {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row < 2:
            print("---|---|---")

    print("\n")

def check_win(symbol):

    for row in board: #? check rows
        if all(cell == symbol for cell in row):
            return True

    for col in range(3): #? check columns
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)): #? check diagonals
        return True

    return False

def available_locations():
    available_spots = [cell for row in board for cell in row if cell.isdigit()]
    if available_spots:
        return available_spots
    return None

def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:                # For macOS and Linux (posix-based systems)
        os.system('clear')

def api_request(url, params=None):

    response = requests.get(url=url, params=params)

    try:
        response.raise_for_status()
        # print(f"Status → {http_codes[response.status_code]}")
    except requests.exceptions.HTTPError as status:
        print(f"Error → {status}")
        return f"Error → {status}"
    else:
        try:
            dict = response.json()
            # print(f"JSON: → {response.json()}")
        except requests.exceptions.JSONDecodeError as status:
            # print(f"Error → {status}. \nThe response might be empty or invalid.")
            return f"Error → {status}"
        else:
            # print(f"Status → {http_codes[response.status_code]}")
            # print(f"URL: → {response.url}")
            # print("Dict: →", dict)
            return dict

# - Set up APIs

http_codes = {
    200: "OK - The request was successful.",
    201: "Created - The request was successful and a new resource was created.",
    204: "No Content - The request was successful, but there is no content to return.",
    400: "Bad Request - The server could not understand the request due to invalid syntax.",
    401: "Unauthorized - Authentication is required to access the resource.",
    403: "Forbidden - The client does not have permission to access the resource.",
    404: "Not Found - The requested resource could not be found.",
    405: "Method Not Allowed - The request method is not supported for the resource.",
    500: "Internal Server Error - The server encountered an unexpected condition.",
    502: "Bad Gateway - The server received an invalid response from an upstream server.",
    503: "Service Unavailable - The server is not ready to handle the request.",
    504: "Gateway Timeout - The server did not receive a timely response from an upstream server."
    }

iss_url = "http://api.open-notify.org/iss-now.json"
iss_parms = {}

# - Start with my CONVENTION of introductory information  

clear_screen()
print(art.text2art(ttt, font='medium'))

# - Setup APPLICATION LOGIC "layer" for business logic, routing, templates, etc. 

#! Ask user if they want to play Tic Tac Toe

play = input("Would you like to play Tic Tac Toe? (Y,N, Yes, No, etc.) \u2192 ")
play = play.strip().upper()
if play not in ["Y", "YES"]:
    print("Maybe next time. Goodbye!")
    sys.exit()  

#! Ask user to pick Heads or Tails for coin flip to go first

while True:
    coin = input("\nNow, flip virtual coin to go first by picking Heads or Tails (H, T, Heads, Tails, etc.) \u2192 ")
    coin = coin.strip().upper()
    if coin in ["H", "HEADS"]:
        coin = "HEADS"
        location = "latitude"
        break
    elif coin in ["T", "TAILS"]:
        coin = "TAILS"
        location = "longitude"
        break
    else:
        print("\nInvalid choice. Please enter h, t, H, or T, heads or tails.")
    
flip = coin_flip(coin)

if flip == coin:
    turn = "USER"
    user_symbol = "X"
    computer_symbol = "O"
else:
    turn = "COMPUTER"
    user_symbol = "O"
    computer_symbol = "X"

#! Play/loop the game

while True:

    if turn == "USER" and game == "NEW":
        print(f"You choose {coin}, and won the coin flip!")
        print("You will be X and go first.")
        input("\nPress Enter to start the game.")

    elif turn == "COMPUTER" and game == "NEW":
        print(f"You choose {coin}, but the flip was {flip}")
        print("The computer will be X and go first.")
        input("\nPress Enter to start the game.")


    if game.strip().upper() in ["NEW", "AGAIN"]:
        board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"] 
        ]
        clear_screen()
        print(art.text2art(ttt, font='medium'))
        print("Starting a new game! Here's the board:\n\n")
        print_board()
        game = "IN PROGRESS"

    if turn == "USER":
        choice = input("Enter the number of the cell where you want to place your symbol: \u2192 ") 
        choice = choice.strip()

        if not choice.isdigit():
            print("Invalid choice. Please enter a number between 1 and 9.")
            continue    

        choice = int(choice)

        if choice not in range(1,10):
            print("Invalid choice. Please enter a number between 1 and 9.")
            continue

        print(f"You selected \u2192 {choice}.")
        if str(choice) not in available_locations():
            print("That cell is already taken. Please choose another one.")
            continue
        symbol = user_symbol
        turn = "COMPUTER"

    elif turn == "COMPUTER":

        choice = random.choice(available_locations())
        print(f"The computer selected \u2192 {choice}.")    
        symbol = computer_symbol
        turn = "USER"
        time.sleep(3)

    clear_screen()
    print(art.text2art(ttt, font='medium'))
    print_board(choice,symbol)
    
    if check_win(user_symbol): #? check for win
        print("USER wins!")
        game = "OVER"
    elif check_win(computer_symbol):
        print("COMPUTER wins!")
        game = "OVER"
    elif not available_locations():
        print("It's a tie!")
        game = "OVER"

    if game == "OVER": #? ask to play again 
        game = input("Would you like to play again? (Y,N, Yes, No, etc.) \u2192 ")
        if game.strip().upper() in ["Y", "YES"]:
            game = "AGAIN"
        else:
            print("Thanks for playing! Goodbye!")
            break



