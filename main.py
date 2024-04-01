import tkinter as tk
from classes.GameOfLife import GameOfLife
from classes.GameGUI import GameGUI

def start_game():
    size_x = int(entry_size_x.get())
    size_y = int(entry_size_y.get())
    probability = float(entry_probability.get())

    game = GameOfLife((size_x, size_y), probability)
    
    label_probability.destroy()
    label_size_x.destroy()
    label_size_y.destroy()
    entry_size_x.destroy()
    entry_size_y.destroy()
    entry_probability.destroy()
    start_button.destroy()
    
    gui = GameGUI(root, game)

root = tk.Tk()
root.title("Game of Life")
root.iconbitmap("ico/main.ico")

label_size_x = tk.Label(root, text="Enter the size of the map (X-axis):")
label_size_x.pack()

entry_size_x = tk.Entry(root)
entry_size_x.pack()

label_size_y = tk.Label(root, text="Enter the size of the map (Y-axis):")
label_size_y.pack()

entry_size_y = tk.Entry(root)
entry_size_y.pack()

label_probability = tk.Label(root, text="Enter the probability of a cell being alive initially (0.0 to 1.0):")
label_probability.pack()

entry_probability = tk.Entry(root)
entry_probability.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()
