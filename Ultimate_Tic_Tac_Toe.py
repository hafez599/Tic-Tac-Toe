import tkinter as tk
from tkinter import messagebox

# Create the main application window
# Create the main application window
root = tk.Tk()
root.title("9-Grid Tic Tac Toe")
root.configure(bg="lightgray")  # Hexadecimal for dark blue

# Initialize variables
current_player = "X"
main_board = [[""] * 9 for _ in range(9)]  # 9 boards, each with 9 cells
count_x = 0
count_y = 0
# Function to check if a subgrid has a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            return board[combo[0]]
    if "" not in board:
        return "Tie"
    return None

# Function to update the label for the current player
def update_player_label():
    player_label.config(text=f"Current Player: {current_player}")

def update_Score(x,o):
    O_Score.config(text=f"Current O Score: {o}")
    X_Score.config(text=f"Current X Score: {x}")

# Function to handle button clicks
# def button_click(button, subgrid_index, cell_index):
#     global count_x
#     global count_y
#     global current_player, main_board
#     subgrid = main_board[subgrid_index]
#
#     # Check if the move is valid
#     if button["text"] == "" and subgrid[cell_index] == "":
#         button["text"] = current_player
#         subgrid[cell_index] = current_player
#
#         # Check if the current subgrid has a winner
#         winner = check_winner(subgrid)
#         if winner:
#             if winner == "Tie":
#                 messagebox.showinfo("Subgrid Result", f"Subgrid {subgrid_index + 1} is a Tie!")
#             elif(winner != None):
#                 if(current_player == 'X'):
#                     count_y = 0
#                     count_x  +=1
#                     update_Score(count_x,count_y)
#                 elif(current_player == 'O'):
#                     count_x = 0
#                     count_y  +=1
#                     update_Score(count_x,count_y)
#                 if(count_x == 3):
#                     messagebox.showinfo("winnnn", f"Player {winner}!")
#                     reset()
#                 elif(count_y == 3):
#                     messagebox.showinfo("winnnn", f"Player {winner}!")
#                     reset()
#                 messagebox.showinfo("Subgrid Result", f"Player {winner} wins Subgrid {subgrid_index + 1}!")
#                 print(count_y , count_x)
#
#         # Switch the player
#         current_player_switch()
#         update_player_label()
# Function to handle button clicks
def button_click(button, subgrid_index, cell_index):
    global count_x, count_y, current_player, main_board
    subgrid = main_board[subgrid_index]

    # Check if the move is valid
    if button["text"] == "" and subgrid[cell_index] == "":
        button["text"] = current_player
        subgrid[cell_index] = current_player

        # Check if the current subgrid has a winner
        winner = check_winner(subgrid)
        if winner:
            # Disable all buttons in the subgrid
            for b in all_buttons[subgrid_index]:
                b.config(state="disabled")

            if winner == "Tie":
                messagebox.showinfo("Subgrid Result", f"Subgrid {subgrid_index + 1} is a Tie!")
            else:
                if current_player == 'X':
                    count_y = 0
                    count_x += 1
                    update_Score(count_x, count_y)
                elif current_player == 'O':
                    count_x = 0
                    count_y += 1
                    update_Score(count_x, count_y)
                if count_x == 3 or count_y == 3:
                    messagebox.showinfo("Game Over", f"Player {winner} wins the game!")
                    reset_grid()
                    return
                messagebox.showinfo("Subgrid Result", f"Player {winner} wins Subgrid {subgrid_index + 1}!")

        # Switch the player
        current_player_switch()
        update_player_label()


# Reset function should also re-enable all buttons
def reset_grid():
    global current_player, main_board, count_x, count_y
    main_board = [[""] * 9 for _ in range(9)]  # Reset the main board
    current_player = "X"
    count_x = 0
    count_y = 0
    update_Score(count_x, count_y)
    update_player_label()

    for subgrid_buttons in all_buttons:
        for button in subgrid_buttons:
            button.config(text="", state="normal")


# def labelOfWinner():
#     messagebox.showinfo("Subgrid Result", f"Player {winner} wins Subgrid {subgrid_index + 1}!")

# Function to switch the player
def current_player_switch():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Create a main grid of 3x3 to hold 9 subgrids
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=1, padx=20, pady=20)

# Create a frame for the label on the left
label_frame = tk.Frame(root)
label_frame.grid(row=0, column=0, padx=20, pady=20)


# Label to display the current player
player_label = tk.Label(label_frame, text=f"Current Player: {current_player}", font=("Arial", 16))
player_label.grid(row=0, column=0)

O_Score = tk.Label(label_frame, text=f"Player O Score: {count_y}", font=("Arial", 16))
O_Score.grid(row=2, column=0)

X_Score = tk.Label(label_frame, text=f"Player X Score: {count_x}", font=("Arial", 16))
X_Score.grid(row=4, column=0)

# Store all buttons for subgrids
all_buttons = []

for subgrid_row in range(3):  # Loop through rows of the main grid
    for subgrid_col in range(3):  # Loop through columns of the main grid
        subgrid_index = subgrid_row * 3 + subgrid_col
        #subgrid_frame = tk.Frame(main_frame, borderwidth=2, relief="solid")
        subgrid_frame = tk.Frame(main_frame, borderwidth=2, relief="solid", bg="lightblue")

        subgrid_frame.grid(row=subgrid_row, column=subgrid_col, padx=5, pady=5)

        # Store buttons for the current subgrid
        subgrid_buttons = []

        # Create a 3x3 grid inside this subgrid
        for cell_row in range(3):
            for cell_col in range(3):
                cell_index = cell_row * 3 + cell_col

                # Create button and use lambda to bind its command properly
             #   button = tk.Button(subgrid_frame, text="X", font=("Arial", 14), height=2, width=5, bg="yellow", fg="black")

                button = tk.Button(subgrid_frame,   text="", font=("Arial", 14), height=2, width=5 )
                button.config(command=lambda b=button, s=subgrid_index, c=cell_index: button_click(b, s, c))
                
                button.grid(row=cell_row, column=cell_col, padx=2, pady=2)
                subgrid_buttons.append(button)
        
        # Add the subgrid buttons to the main list
        all_buttons.append(subgrid_buttons)
# def reset():
#     for button in all_buttons:
#         for b in button:
#             b["text"] =""
#             #main_board = [""] *9
#             update_Score(0,0)
#             current_player = 'X'
# Start the Tkinter event loop
root.mainloop()
