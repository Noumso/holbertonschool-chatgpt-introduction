#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board.
    Args:
        board (list): The game board as a 2D list.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """
    Check if there is a winner on the current board.
    Args:
        board (list): The game board as a 2D list.
    Returns:
        str: The winner's symbol ("X" or "O"), or None if no winner.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    """
    Check if the board is full (no empty spaces left).
    Args:
        board (list): The game board as a 2D list.
    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            # Get user input
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Validate input
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2. Try again.")
                continue

            # Check if the spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[row][col] = player

            # Check for a winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            # Check for a draw
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers only. Try again.")


if __name__ == "__main__":
    tic_tac_toe()

