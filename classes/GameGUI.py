import numpy as np
import tkinter as tk
from tkinter import Label, Scale, Button, Toplevel, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class GameGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.after_id = None

        self.fig_map, self.ax_map = plt.subplots(figsize=(8, 4))
        self.canvas_map = FigureCanvasTkAgg(self.fig_map, master=master)
        self.canvas_map.get_tk_widget().pack(fill="both", expand=True)

        self.label_generation = Label(master, text="Generation: 0")
        self.label_generation.pack()

        self.scale = Scale(master, label="Delay (seconds)", from_=0.1, to=5, orient=tk.HORIZONTAL, resolution=0.1)
        self.scale.pack()

        self.start_button = Button(master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.stop_button = Button(master, text="Stop", command=self.stop_game)
        self.stop_button.pack()
        

        self.label_neighbors = Label(master, text="Average Neighbors: 0")
        self.label_neighbors.pack()

        self.label_birth_percentage = Label(master, text="Birth Percentage: 0%")
        self.label_birth_percentage.pack()

        self.label_death_percentage = Label(master, text="Death Percentage: 0%")
        self.label_death_percentage.pack()

        self.label_population_density = Label(master, text="Population Density: 0%")
        self.label_population_density.pack()

        # Open statistics
        self.open_statistics_window()
        self.draw_map()

    def draw_map(self):
        self.ax_map.clear()
        cell_size = 1.0
        self.ax_map.imshow(self.game.current_map, cmap='binary', interpolation='nearest', extent=[0, self.game.size[0] * cell_size, 0, self.game.size[1] * cell_size])
        self.canvas_map.draw()

    def update_generation_label(self):
        self.label_generation.config(text=f"Generation: {self.game.generation_count}")

    def run_game(self):
        if not self.game.stop_game:
            self.game.set_next_generation()
            self.draw_map()
            self.game.generation_count += 1
            self.update_generation_label()
            self.update_statistics_window()
            # Store the ID of the new after function
            self.after_id = self.master.after(int(self.game.delay * 1000), self.run_game)

    def start_game(self):
        delay = self.scale.get()
        self.game.set_delay(delay)
        self.game.stop_game = False
        # Cancel the precedent after function if there is one
        if self.after_id:
            self.master.after_cancel(self.after_id)
        # --> New after function with new delay
        self.run_game()

    def stop_game(self):
        self.game.stop_game = True
        
    def open_statistics_window(self):
        # Number of living cells in another window
        self.graphics_window = Toplevel(self.master)
        self.graphics_window.title("Game Statistics")
        self.graphics_window.iconbitmap("ico/graph.ico")

        self.fig_stats, self.ax_stats = plt.subplots(figsize=(8, 4))
        self.ax_stats.plot(range(len(self.game.cell_count)), self.game.cell_count, marker='o', label='Cell Count', markersize=1)
        self.ax_stats.set_title('Number of Cells Over Time')
        self.ax_stats.set_xlabel('Generation')
        self.ax_stats.set_ylabel('Number of Cells')
        self.ax_stats.legend()
        self.ax_stats.grid(True)
        self.fig_stats.tight_layout()
        self.canvas_stats = FigureCanvasTkAgg(self.fig_stats, master=self.graphics_window)
        self.canvas_stats.get_tk_widget().pack()

        self.fig_survival, self.ax_survival = plt.subplots(figsize=(8, 4))
        self.ax_survival.set_ylim([0, 1])
        self.canvas_survival = FigureCanvasTkAgg(self.fig_survival, master=self.graphics_window)
        self.canvas_survival.get_tk_widget().pack()

        # Heat in another window
        self.heat_window = Toplevel(self.master)
        self.heat_window.title("Heat map")
        self.heat_window.iconbitmap("ico/heatmap.ico")

        self.figHeat, self.axHeat = plt.subplots(figsize=(4, 4))

        self.canvas_heat = FigureCanvasTkAgg(self.figHeat, master=self.heat_window)
        self.canvas_heat.get_tk_widget().pack()
        
        if self.game.generation_count > 0:
            self.axHeat.imshow(np.divide(self.game.numberOfGenerationsPerCell, self.game.generation_count), cmap='hot', interpolation='nearest', extent=[0, self.game.size[0] * 1, 0, self.game.size[1] * 1])

    def update_statistics_window(self):
        # Updates the graphics
        self.ax_stats.clear()
        self.ax_stats.plot(range(len(self.game.cell_count)), self.game.cell_count, marker='o', label='Cell Count', markersize=0)
        self.ax_stats.set_title('Number of Cells Over Time')
        self.ax_stats.set_xlabel('Generation')
        self.ax_stats.set_ylabel('Number of Cells')
        self.ax_stats.legend()
        self.ax_stats.grid(True)
        self.fig_stats.tight_layout()
        self.canvas_stats.draw()

        self.axHeat.clear()
        self.axHeat.imshow(np.divide(self.game.numberOfGenerationsPerCell, self.game.generation_count), cmap='hot', interpolation='nearest') #, extent=[0, self.game.size[0] * 1, 0, self.game.size[1] * 1])

        self.canvas_heat.draw()

        self.label_neighbors.config(text=f"Average Neighbors: {self.game.average_neighbors[-1]:.2f}")
        self.label_birth_percentage.config(text=f"Birth Percentage: {self.game.birth_percentage[-1]*100:.2f}%")
        self.label_death_percentage.config(text=f"Death Percentage: {self.game.death_percentage[-1]*100:.2f}%")
        self.label_population_density.config(text=f"Population Density: {self.game.population_density[-1]*100:.2f}%")

        self.ax_survival.clear()
        self.ax_survival.plot(range(len(self.game.survival_rate)), self.game.survival_rate, marker='o', label='Survival Rate', markersize=0, color="red")
        self.ax_survival.set_title('Survival Rate Over Time')
        self.ax_survival.set_xlabel('Generation')
        self.ax_survival.set_ylabel('Survival Rate')
        self.ax_survival.set_ylim([0, 1])
        self.ax_survival.legend()
        self.ax_survival.grid(True)
        self.fig_survival.tight_layout()
        self.canvas_survival.draw()