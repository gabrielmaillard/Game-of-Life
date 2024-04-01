import tkinter as tk
import json
from classes.GameOfLife import GameOfLife
from classes.GameGUI import GameGUI

CONFIGURATION_FILE = "configuration.json"

with open(CONFIGURATION_FILE, "r") as config_file:
    config_data = json.load(config_file)

size_x = config_data["size_x"]
size_y = config_data["size_y"]
probability = config_data["cell_probability"]

root = tk.Tk()
root.title("Game of Life")
root.iconbitmap("ico/main.ico")

game = GameOfLife((size_x, size_y), probability)
gui = GameGUI(root, game)

root.mainloop()
