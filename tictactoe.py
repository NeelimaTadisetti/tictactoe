
# Print Board to hold game board data (Place holder for player input)
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# ---------Initialising global Variables  -----------
# Checking if the game still on 
game_continues = True

# Determines winner of the game
winner = None

# Current Player selection (X goes first)
current_player = "X"

# ------------- Functions ---------------

# Main function that runs and plays tic tac toe game
def play_game():

  # Display the initial game board
  display_board()

  # Looping until the game stops (winner or tie)
  while game_continues:

    #  Handling each player turns
    handle_turn(current_player)

    # Check to see if game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()
    # Out put the result by printing results winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")
  else:
      replay()
 # Display Game board along with guided position for the player input.
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

  # Function to organise turns for each player 
def handle_turn(player):

  # Choosing the player and corresponding position on the board
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

# Checking valid user input to the board
  valid = False  # set default to false
  while not valid:
    # Ensure all entries of the board are valid  
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
  
   # Position the correct index of the board list for the given number 1-9 of user input
    position = int(position) - 1

# Checking if entry is available if not alert the player to try choose different position on the board
    if board[position] == "-":
      valid = True
    else:
      print("Entry alredy filled/Invalid entry, Try choosing different spot.")

  # Positioning the player on the board
  board[position] = player

  # Display game board with players entries
  display_board()

# Checking the game status after each player entry
def check_if_game_over():
    check_for_winner()
    check_for_tie()

# check if any winnings across the board 
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere with match
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

# Check three rows of the board for a winner
# if any row has all equal values and is not empty, player has won
# if any row has unequal values and is empty, player has drawn, loss, or is still playing the game
# return the winner if a winning row is found
# return None if no winner is found in the three rows
def check_rows():
  # Set global variables
  global game_continues
  # Checking rows with same value(X or O) and not empty
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row with matching value, show the result with win
  if row_1 or row_2 or row_3:
    game_continues = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if no winner in the game
  else:
    return None

# Check three columns of the board for a winner
# if any column has all equal values and is not empty, player has won
# if any column has unequal values and is empty, player has drawn, loss, or is still playing the game
# return the winner if a winning column is found
# return None if no winner is found in the three columns
def check_columns():
  # Set global variables
  global game_continues
  # Checking column with same value(X or O) and not empty
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any column with matching value, show the result with win
  if column_1 or column_2 or column_3:
    game_continues = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if no winner
  else:
    return None

# Check two diagonals of board for a winner
# if any of the two diagonals has all equal values and is not empty, player has won
# if any of the two diagonals has unequal values and is empty, player has drawn, loss, or is still playing the game
# return the winner if a winning diagonal is found
# return None if no winner is found in the two diagonals
def check_diagonals():
  # Set global variables
  global game_continues
  # Checking column with same value(X or O) and not empty
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row with matching value, show the result with win
  if diagonal_1 or diagonal_2:
    game_continues = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if no winner
  else:
    return None
  
# Checking if there is a tie
def check_for_tie():
  # Set global variables
  global game_continues
  # If board is full
  if "-" not in board:
    game_continues = False
    return True
  # Else there is no tie
  else:
    return False


# Fliping the current player from X to O, or O to X
def flip_player():
  # Global variables
  global current_player
  # If the current player is X, change to O
  if current_player == "X":
    current_player = "O"
  # Or if the current player is O, change to X
  elif current_player == "O":
    current_player = "X"

# replay game again
def replay():
    playAgain = input("Do you want to play again (y/n) ? ")
    if playAgain == 'y':
        play_game()
    if playAgain== 'n':
        print('Good Bye')

# Start Execution of tic tac toe game by calling function
play_game()