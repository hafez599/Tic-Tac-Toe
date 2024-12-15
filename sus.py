import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("9-Grid Tic Tac Toe")

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
    global winning_combinations
    for combo in winning_combinations:
        if board[combo[0]] + board[combo[1]] + board[combo[2]] == "SUS":
            winning_combinations = [c for c in winning_combinations if c != combo]
            print(winning_combinations)
            return True

    if "" not in board:
        return "Tie"
    return None


def update_player_label():
    player_label.config(text=f"Current Player: {current_player}")

def update_Score(x,o):
    O_Score.config(text=f"Current U Score: {o}")
    X_Score.config(text=f"Current S Score: {x}")


def button_click(button, cell_index):
    global count_x, count_y, current_player, main_board
    if main_board[cell_index] == "":
        main_board[cell_index] = current_player
        button["text"] = current_player
        winner = check_winner(main_board)
        if winner == True:
            if current_player == "S":
                count_x += 1
            else:
                count_y += 1
            update_Score(count_x, count_y)
        # elif(winner == "Tie"):
        #     messagebox.showinfo("Game Over", "It's a tie!")
        current_player_switch()
        check_final_win()
def check_final_win():
    global count_x , count_y
    if "" not in main_board:
        if count_x>count_y:
            messagebox.showinfo("Game Over", "Player S win")
        elif count_y>count_x:
            messagebox.showinfo("Game Over", "Player U win")
        else:
            messagebox.showinfo("Game Over", "Tie!")
        reset_grid()
def current_player_switch():
    global current_player
    current_player = "U" if current_player == "S" else "S"

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1, padx=20, pady=20)

label_frame = tk.Frame(root)
label_frame.grid(row=0, column=0, padx=20, pady=20)

player_label = tk.Label(label_frame, text=f"Current Player: {current_player}", font=("Arial", 16))
player_label.grid(row=0, column=0)

O_Score = tk.Label(label_frame, text=f"Player O Score: {count_y}", font=("Arial", 16))
O_Score.grid(row=2, column=0)

X_Score = tk.Label(label_frame, text=f"Player X Score: {count_x}", font=("Arial", 16))
X_Score.grid(row=4, column=0)

all_buttons = []

for row in range(3):
    for col in range(3):
        cell_index = row * 3 + col
        subgrid_frame = tk.Frame(main_frame, borderwidth=2, relief="solid")
        subgrid_frame.grid(row=row, column=col, padx=5, pady=5)
        button = tk.Button(
            subgrid_frame,
            text="", font=("Arial", 14), height=2, width=5
        )
        button.config(command=lambda b=button, c=cell_index: button_click(b, c))

        button.grid(row=row, column=col, padx=2, pady=2)
        all_buttons.append(button)


def reset_grid():
    global current_player, main_board, count_x, count_y
    main_board = [""] * 9  # Reset the main board
    count_x = 0
    count_y = 0
    current_player = "S"
    update_Score(count_x, count_y)
    update_player_label()

    # Reset the buttons in the UI
    for button in all_buttons:
        button["text"] = ""
root.mainloop()
