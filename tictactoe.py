
# Print Board to hold game board data (Place holder)
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# ---------Initialising global Variables  -----------
# Checking if the game still on 
game_still_on = True

# setting winner of the game
winner = None

# Deciding who's going to play first (X goes first)
current_player = "X"

# ------------- Functions ---------------

# Main function for tic tac toe game play
def play_game():

  # user to show the initial game board
  display_board()

  # Looping until the game stops (winner or tie)
  while game_still_on:

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

 # Display Game board along with guided position for the player input.
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

  # Function to organise turns for each player 
def handle_turn(player):

  # Choosing the player position
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

# Checking valid user input to the board
  valid = False
  while not valid:
    # Ensure all entries in the board are valid  
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
  
   # Position the correct index in the board list
    position = int(position) - 1

# Checking if entry is available if not alert player to try choose different position
    if board[position] == "-":
      valid = True
    else:
      print("Entry alredy filled/Invalid entry, Try choosing different spot.")

  # Positioning the player on the board
  board[position] = player

  # Display game board with players entries
  display_board()

# Checking the game status after each entry
def check_if_game_over():
  check_for_winner()
  check_for_tie()

# check if any winnings across the board
def check_for_winner():
  # Set global variables
  global winner
  # Check if there was a winner anywhere
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

# Check the rows for a win
def check_rows():
  # Set global variables
  global game_still_on
  # Checking rows with same value(X or O) and not empty
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row with matching value, show the result with win
  if row_1 or row_2 or row_3:
    game_still_on = False
  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or return None if no winner
  else:
    return None

# Check the columns for a win
def check_columns():
  # Set global variables
  global game_still_on
  # Checking column with same value(X or O) and not empty
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any column with matching value, show the result with win
  if column_1 or column_2 or column_3:
    game_still_on = False
  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or return None if no win
  else:
    return None

# Check the diagonals for a winner
def check_diagonals():
  # Set global variables
  global game_still_on
  # Checking column with same value(X or O) and not empty
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row with matching value, show the result with win
  if diagonal_1 or diagonal_2:
    game_still_on = False
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
  global game_still_on
  # If board is full
  if "-" not in board:
    game_still_on = False
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

# Start Execution of tic tac toe game by calling this function
play_game()