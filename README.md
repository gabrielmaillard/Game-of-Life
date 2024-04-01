![GIF depicting the Game of Life](https://blog.datawrapper.de/wp-content/uploads/2021/06/game-of-life-loop-cropped.gif)
# Game of Life
A Python implementation of Conway's Game of Life with a sleek graphical user interface using Tkinter and Matplotlib.

## Overview

Conway's Game of Life is a classic cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Features
### Dynamic Visualization

Watch as generations evolve in real-time with a dynamic visualization. The grid updates with each generation, showcasing the emergence and extinction of cells.
### Comprehensive Statistics

Gain insights into the evolving population with comprehensive statistics:
* Number of Cells Over Time: Track the fluctuation in the number of cells across generations.
![Screenshot of the graph showing the number of cells as a function of generation](README/Screenshot%20Number%20of%20cells.JPG)
* Survival Rate: Monitor the percentage of cells that survive from one generation to the next.
![Screenshot of the graph showing the survival rate as a function of generation](README/Screenshot%20Survival%20rate.JPG)
* Birth Percentage: Analyze the proportion of new cells born in each generation.
* Death Percentage: Understand the rate of cell death in each generation.
* Population Density: Explore the density of the cell population throughout the simulation.

### Heatmap Representation

Visualize the distribution of cell activity across the grid with a heatmap. Bright spots indicate areas of high activity, while darker regions signify less active areas.

![Screenshot of the heat map](README/Screenshot%20Heat%20map.JPG)

## Installation

### Steps

1. Clone the repository:
```
git clone https://github.com/your_username/GameOfLife.git
```

2. Navigate to the project directory:
```
cd GameOfLife
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

### Dependencies

* Tkinter: GUI toolkit for Python.
* JSON: Handling configuration settings.
* NumPy: Scientific computing library for numerical operations.
* Matplotlib: Plotting library for visualization.

## Configuration

The size of the map and the initial probability of a cell being alive can be modified in the configuration.json file.

## Usage

Run the main.py file to start the Game of Life GUI:
```
python main.py
```

Once the GUI window opens, configure the size of the map and the initial probability of cell survival. Click "Start Game" to initiate the simulation.

Adjust the delay slider to control the speed of the simulation. Use the "Stop" button to pause the simulation at any time.
