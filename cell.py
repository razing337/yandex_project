import pygame
from random import choice


class Cell:
    def __init__(self, x, y, thickness):
        self.x, self.y = x, y
        self.thickness = thickness
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw(self, sc, tile):
        x, y = self.x * tile, self.y * tile
        for wall, is_present in self.walls.items():
            if is_present:
                if wall == 'top':
                    start = (x, y)
                    end = (x + tile, y)
                elif wall == 'right':
                    start = (x + tile, y)
                    end = (x + tile, y + tile)
                elif wall == 'bottom':
                    start = (x + tile, y + tile)
                    end = (x, y + tile)
                else:  # left
                    start = (x, y + tile)
                    end = (x, y)
                pygame.draw.line(sc, pygame.Color('darkgreen'), start, end, self.thickness)

    def is_valid_cell(self, x, y, cols, rows):
        return 0 <= x < cols and 0 <= y < rows

    def get_cell_index(self, x, y, cols):
        return x + y * cols

    def check_cell(self, x, y, cols, rows, grid_cells):
        if not self.is_valid_cell(x, y, cols, rows):
            return False
        return grid_cells[self.get_cell_index(x, y, cols)]

    def get_neighbors(self, cols, rows, grid_cells):
        neighbors = []
        potential_neighbors = [(self.x, self.y - 1), (self.x + 1, self.y), (self.x, self.y + 1), (self.x - 1, self.y)]
        for nx, ny in potential_neighbors:
            neighbor = self.check_cell(nx, ny, cols, rows, grid_cells)
            if neighbor and not neighbor.visited:
                neighbors.append(neighbor)
        return neighbors

    def choose_random_neighbor(self, cols, rows, grid_cells):
        neighbors = self.get_neighbors(cols, rows, grid_cells)
        return choice(neighbors) if neighbors else False
