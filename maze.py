from cell import Cell


class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.thickness = 4
        self.grid_cells = self._create_grid_cells()

    def _create_grid_cells(self):
        return [[Cell(col, row, self.thickness) for col in range(self.cols)] for row in range(self.rows)]

    def _get_valid_neighbors(self, cell):
        x, y = cell.x, cell.y
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < self.cols and 0 <= ny < self.rows]
        return [self.grid_cells[ny][nx] for nx, ny in valid_neighbors if not self.grid_cells[ny][nx].visited]

    def generate_maze(self):
        stack = []
        current_cell = self.grid_cells[0][0]
        current_cell.visited = True
        stack.append(current_cell)

        while stack:
            current_cell = stack[-1]
            neighbors = self._get_valid_neighbors(current_cell)
            if neighbors:
                next_cell = neighbors[0]
                next_cell.visited = True
                stack.append(next_cell)
                self._remove_walls(current_cell, next_cell)
            else:
                stack.pop()

    def _remove_walls(self, current, next):
        dx, dy = current.x - next.x, current.y - next.y
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        elif dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
