import tkinter as tk
from tkinter import messagebox
import os

class GameHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Hub")
        self.root.geometry("300x250")
        self.root.configure(bg="black") 
        self.root.iconphoto(True, tk.PhotoImage(file="icon.png"))    

        self.label = tk.Label(root, text="Welcome to the Game Hub!", font=("Arial", 16), bg="black", fg="white")
        self.label.pack(pady=10)

        self.tic_tac_toe_btn = tk.Button(root, text="Tic Tac Toe", command=self.open_tic_tac_toe, bg="gray", fg="white", activebackground="green", activeforeground="white", border=5, borderwidth=2, relief="raised", font=("Arial", 12))
        self.tic_tac_toe_btn.pack(fill=tk.X, padx=20, pady=5)

        self.chess_btn = tk.Button(root, text="Chess", command=self.open_chess, bg="gray", fg="white", activebackground="green", activeforeground="white", border=5, borderwidth=2, relief="raised", font=("Arial", 12))
        self.chess_btn.pack(fill=tk.X, padx=20, pady=5)

        self.sudoku_btn = tk.Button(root, text="Sudoku", command=self.open_sudoku, bg="gray", fg="white", activebackground="green", activeforeground="white", border=5, borderwidth=2, relief="raised", font=("Arial", 12))
        self.sudoku_btn.pack(fill=tk.X, padx=20, pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=self.on_exit, bg="gray", fg="white", activebackground="red", activeforeground="white", border=5, borderwidth=2, relief="raised", font=("Arial", 12))
        self.exit_btn.pack(fill=tk.X, padx=20, pady=5)

        # Add hover effects
        self.add_hover_effects(self.tic_tac_toe_btn)
        self.add_hover_effects(self.chess_btn)
        self.add_hover_effects(self.sudoku_btn)
        self.add_hover_effects(self.exit_btn)

    def add_hover_effects(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="darkgray"))
        widget.bind("<Leave>", lambda e: widget.config(bg="gray"))

    def open_tic_tac_toe(self):
        os.system("python tictactoe.py")

    def open_chess(self):
        os.system("python chess.py")

    def open_sudoku(self):
        os.system("python sudoku.py")

    def on_exit(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to exit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameHub(root)
    root.mainloop()
