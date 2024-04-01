import numpy as np

class GameOfLife:
    def __init__(self, size, initial_probability):
        self.size = size
        self.delay = 1
        self.stop_game = False
        self.current_map = self.generate_random_map(initial_probability)
        self.initial_cell_count = np.sum(self.current_map)

        # Statistics
        self.generation_count = 0
        self.average_neighbors = []
        self.birth_percentage = []
        self.death_percentage = []
        self.cell_count = []
        self.population_density = []
        self.current_cells_ages = np.zeros(self.size)
        self.sumLifespan = 0
        self.totalNumberCells = 0
        self.numberOfGenerationsPerCell = np.zeros(self.size)
        self.survival_rate = []

    def generate_empty_map(self):
        return np.zeros(self.size, dtype=bool)

    def generate_random_map(self, probability):
        return np.random.choice([True, False], size=self.size, p=[probability, 1 - probability])

    def count_neighbors(self, x, y):
        neighbors = [
            self.current_map[(x + 1) % self.size[0], (y + 1) % self.size[1]],
            self.current_map[(x + 1) % self.size[0], y],
            self.current_map[x, (y + 1) % self.size[1]],
            self.current_map[(x + 1) % self.size[0], (y - 1) % self.size[1]],
            self.current_map[(x - 1) % self.size[0], (y - 1) % self.size[1]],
            self.current_map[(x - 1) % self.size[0], (y + 1) % self.size[1]],
            self.current_map[x, (y - 1) % self.size[1]],
            self.current_map[(x - 1) % self.size[0], y],
        ]
        return np.sum(neighbors)

    def set_next_generation(self):
        new_map = np.copy(self.current_map)
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                neighbors_count = self.count_neighbors(x, y)
                if self.current_map[x, y]:
                    new_map[x, y] = 2 <= neighbors_count <= 3
                else:
                    new_map[x, y] = neighbors_count == 3

        survival_sum = 0

        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if new_map[x, y] == True:
                    self.current_cells_ages[x, y] += 1
                    self.numberOfGenerationsPerCell[x, y] += 1
                    if self.current_map[x, y] == True:
                        survival_sum += 1
                elif new_map[x, y] == False and self.current_cells_ages[x, y] != 0:
                    self.sumLifespan += self.current_cells_ages[x, y]
                    self.current_cells_ages[x, y] = 0
                    self.totalNumberCells += 1

        average_neighbors = np.mean([self.count_neighbors(x, y) for x in range(self.size[0]) for y in range(self.size[1])])
        self.average_neighbors.append(average_neighbors)

        birth_percentage = np.sum(new_map) / np.size(new_map)
        self.birth_percentage.append(birth_percentage)

        death_percentage = 1 - np.sum(new_map) / np.size(new_map)
        self.death_percentage.append(death_percentage)

        population_density = np.sum(self.current_map) / np.size(self.current_map)
        self.population_density.append(population_density)

        if np.sum(self.current_map) != 0:
            self.survival_rate.append(survival_sum / np.sum(self.current_map))
        else:
            self.survival_rate.append(0)

        # Modify the map
        self.current_map = new_map
        self.cell_count.append(np.sum(self.current_map))
    
    def set_delay(self, delay):
        self.delay = delay