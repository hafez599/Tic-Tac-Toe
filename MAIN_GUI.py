import tkinter as tk
from tkinter import messagebox
def game1():
    game1_window = tk.Toplevel(root)
    game1_window.title("SuS Tic Tac Toe - Game 1")


    current_player = "S"
    main_board = [""] * 9
    count_x = 0
    count_y = 0

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]

    def check_winner(board):
        nonlocal winning_combinations
        for combo in winning_combinations:
            if board[combo[0]] + board[combo[1]] + board[combo[2]] == "SUS":
                winning_combinations = [c for c in winning_combinations if c != combo]
                return True

        if "" not in board:
            return "Tie"
        return None

    def update_player_label():
        player_label.config(text=f"Current Player: {current_player}")

    def update_score(x, o):
        o_score_label.config(text=f"Player O Score: {o}")
        x_score_label.config(text=f"Player S Score: {x}")

    def button_click(button, cell_index):
        nonlocal count_x, count_y, current_player, main_board
        if main_board[cell_index] == "":
            main_board[cell_index] = current_player
            button["text"] = current_player
            winner = check_winner(main_board)
            if winner:
                if current_player == "S":
                    count_x += 1
                else:
                    count_y += 1
                update_score(count_x, count_y)
            current_player_switch()
            update_player_label()
            check_final_win()

    def check_final_win():
        if "" not in main_board:
            if count_x > count_y:
                messagebox.showinfo("Game Over", "Player S wins")
            elif count_y > count_x:
                messagebox.showinfo("Game Over", "Player U wins")
            else:
                messagebox.showinfo("Game Over", "It's a tie!")
            reset_grid()

    def current_player_switch():
        nonlocal current_player
        current_player = "U" if current_player == "S" else "S"

    def reset_grid():
        nonlocal current_player, main_board, count_x, count_y
        # Reset the main board to a list of empty strings
        main_board = [""] * 9
        current_player = "S"  # Reset to the starting player
        count_x = 0
        count_y = 0
        update_score(count_x, count_y)
        update_player_label()

        # Clear the text and enable all buttons
        for button in all_buttons:
            button.config(text="", state="normal")

    main_frame = tk.Frame(game1_window)
    main_frame.grid(row=0, column=1, padx=20, pady=20)

    label_frame = tk.Frame(game1_window)
    label_frame.grid(row=0, column=0, padx=20, pady=20)

    player_label = tk.Label(label_frame, text=f"Current Player: {current_player}", font=("Arial", 16))
    player_label.grid(row=0, column=0)

    o_score_label = tk.Label(label_frame, text=f"Player O Score: {count_y}", font=("Arial", 16))
    o_score_label.grid(row=2, column=0)

    x_score_label = tk.Label(label_frame, text=f"Player S Score: {count_x}", font=("Arial", 16))
    x_score_label.grid(row=4, column=0)

    all_buttons = []

    for row in range(3):
        for col in range(3):
            cell_index = row * 3 + col
            subgrid_frame = tk.Frame(main_frame, borderwidth=2, relief="solid")
            subgrid_frame.grid(row=row, column=col, padx=5, pady=5)
            button = tk.Button(subgrid_frame, text="", font=("Arial", 14), height=2, width=5)
            button.config(command=lambda b=button, c=cell_index: button_click(b, c))
            button.grid(row=row, column=col, padx=2, pady=2)
            all_buttons.append(button)


def game2():
    game2_window = tk.Toplevel(root)
    game2_window.title("9-Grid Tic Tac Toe - Game 2")

    # Initialize variables
    current_player = "X"
    main_board = [[""] * 9 for _ in range(9)]  # 9 boards, each with 9 cells
    count_x = 0
    count_y = 0

    def check_winner(board):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
                return board[combo[0]]
        if "" not in board:
            return "Tie"
        return None

    def update_player_label():
        player_label.config(text=f"Current Player: {current_player}")

    def update_score(x, o):
        O_Score.config(text=f"Player O Score: {o}")
        X_Score.config(text=f"Player X Score: {x}")

    def reset_grid():
        nonlocal main_board, current_player, count_x, count_y
        main_board = [[""] * 9 for _ in range(9)]
        current_player = "X"
        count_x = 0
        count_y = 0
        update_score(count_x, count_y)
        update_player_label()

        for subgrid_buttons in all_buttons:
            for button in subgrid_buttons:
                button.config(text="", state="normal")

    def button_click(button, subgrid_index, cell_index):
        nonlocal current_player, main_board, count_x, count_y
        subgrid = main_board[subgrid_index]
        if button["text"] == "" and subgrid[cell_index] == "":
            button["text"] = current_player
            subgrid[cell_index] = current_player
            winner = check_winner(subgrid)
            if winner:
                for b in all_buttons[subgrid_index]:
                    b.config(state="disabled")
                if winner == "Tie":
                    messagebox.showinfo("Subgrid Result", f"Subgrid {subgrid_index + 1} is a Tie!")
                else:
                    if current_player == "X":
                        count_x += 1
                    else:
                        count_y += 1
                    update_score(count_x, count_y)
                    if count_x == 3 or count_y == 3:
                        messagebox.showinfo("Game Over", f"Player {winner} wins the game!")
                        reset_grid()
                        return
                    messagebox.showinfo("Subgrid Result", f"Player {winner} wins Subgrid {subgrid_index + 1}!")
            current_player = "O" if current_player == "X" else "X"
            update_player_label()

    # Create main and label frames
    main_frame = tk.Frame(game2_window)
    main_frame.grid(row=0, column=1, padx=20, pady=20)

    label_frame = tk.Frame(game2_window)
    label_frame.grid(row=0, column=0, padx=20, pady=20)

    player_label = tk.Label(label_frame, text=f"Current Player: {current_player}", font=("Arial", 16))
    player_label.grid(row=0, column=0)

    O_Score = tk.Label(label_frame, text=f"Player O Score: {count_y}", font=("Arial", 16))
    O_Score.grid(row=2, column=0)

    X_Score = tk.Label(label_frame, text=f"Player X Score: {count_x}", font=("Arial", 16))
    X_Score.grid(row=4, column=0)

    all_buttons = []
    for subgrid_row in range(3):
        for subgrid_col in range(3):
            subgrid_index = subgrid_row * 3 + subgrid_col
            subgrid_frame = tk.Frame(main_frame, borderwidth=2, relief="solid", bg="lightblue")
            subgrid_frame.grid(row=subgrid_row, column=subgrid_col, padx=5, pady=5)
            subgrid_buttons = []
            for cell_row in range(3):
                for cell_col in range(3):
                    cell_index = cell_row * 3 + cell_col
                    button = tk.Button(subgrid_frame, text="", font=("Arial", 14), height=2, width=5)
                    button.config(command=lambda b=button, s=subgrid_index, c=cell_index: button_click(b, s, c))
                    button.grid(row=cell_row, column=cell_col, padx=2, pady=2)
                    subgrid_buttons.append(button)
            all_buttons.append(subgrid_buttons)

root = tk.Tk()
root.title("Tic Tac Toe Games Menu")

menu_label = tk.Label(root, text="Choose a Game", font=("Arial", 20))
menu_label.pack(pady=20)

game1_button = tk.Button(root, text="SuS Tic Tac Toe", font=("Arial", 20), command=game1)
game1_button.pack(pady=10)

game2_button = tk.Button(root, text="Ultimate Tic Tac Toe", font=("Arial", 18), command=game2)
game2_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 20), command=root.destroy)

exit_button.pack(pady=10)

root.mainloop()