# Tic Tac Toe Game in Python

# Allocate list to store 9 box values

boxes = ["-"] * 9

# Create a function to print the boxes in a 3 by 3 grid


def print_board(board):
    # using box characters:
    print(
        f"""
          ┌────┬────┬────┐
          │  {board[0]} │  {board[1]} │  {board[2]} │
          │────┼────┼────│
          │  {board[3]} │  {board[4]} │  {board[5]} │
          │────┼────┼────│
          │  {board[6]} │  {board[7]} │  {board[8]} │
          └────┴────┴────┘
          """
    )


def main():
    # This is where our game would actually start from
    print_board(boxes)
    # while loop to ask for player choices, condition is that game is ongoing
    while check_game(boxes) == "ONGOING":
        # Take input from players for their desired choices
        player_a = int(input("Player A, Enter box number (1-9): "))
        # check if player entered correct box number and keep asking for input until its correct
        while player_a < 1 or player_a > 9:
            player_a = int(input("Player A, Enter correct box number (1-9): "))
            # check if box number is already filled
            if boxes[player_a - 1] != "-":
                continue
        # Update box number to X
        boxes[player_a - 1] = "X"
        # check if game has ended
        if check_game(boxes) == "END":
            print_board(boxes)
            print("Player A wins!")
            break
        print_board(boxes)
        player_b = int(input("PLayer B, Enter box number (1-9): "))
        while player_b < 1 or player_b > 9:
            player_b = int(input("Player B, Enter correct box number (1-9): "))
            # check if box number is already filled
            if boxes[player_b - 1] != "-":
                continue
        # Update box number to Or
        boxes[player_b - 1] = "O"
        if check_game(boxes) == "END":
            print_board(boxes)
            print("Player B wins!")
            break
        print_board(boxes)

    print("Its a draw! Good Game")


# Check games status by comparing box values
def check_game(board):
    if (
        board[0] == board[1] == board[2] == "X"
        or board[0] == board[1] == board[2] == "O"
    ):
        return "END"
    elif (
        board[3] == board[4] == board[5] == "X"
        or board[3] == board[4] == board[5] == "O"
    ):
        return "END"
    elif (
        board[6] == board[7] == board[8] == "X"
        or board[6] == board[7] == board[8] == "O"
    ):
        return "END"
    elif (
        board[0] == board[4] == board[8] == "X"
        or board[0] == board[4] == board[8] == "O"
    ):
        return "END"
    elif (
        board[2] == board[4] == board[6] == "X"
        or board[2] == board[4] == board[6] == "O"
    ):
        return "END"
    elif "-" not in board:
        return "DRAW"
    else:
        return "ONGOING"


main()
