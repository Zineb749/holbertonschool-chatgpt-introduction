#!/usr/bin/python3
def print_board(board):
    """
    Print the Tic Tac Toe board in a user-friendly format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if there's a winner on the Tic Tac Toe board.

    Parameters:
    board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
    str: The winner ("X" or "O") if there's a winner, otherwise None.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    """
    Check if the Tic Tac Toe board is full.

    Parameters:
    board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
    bool: True if the board is full, otherwise False.
    """
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """
    Main function to play a game of Tic Tac Toe.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}'s turn.")

        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Validate input
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter a number between 0 and 2.")
                continue

            # Check if the chosen cell is empty
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Place the player's marker on the board
            board[row][col] = player

            # Check for a winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            # Check for a tie
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    tic_tac_toe()

