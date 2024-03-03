import pygame


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player_size = 10
        self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.speed = 4

    # метод для обновления позиции
    def update_position(self, keys_pressed, grid_cells, thickness, tile):
        self._handle_input(keys_pressed)
        self._move(grid_cells, thickness, tile)

    # метод для обработки ввода пользователя
    def _handle_input(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.y += self.speed

    # метод для перемещения игрока и проверки столкновений с стенами
    def _move(self, grid_cells, thickness, tile):
        current_cell_x, current_cell_y = self.x // tile, self.y // tile
        current_cell = self._get_current_cell(current_cell_x, current_cell_y, grid_cells)
        current_cell_abs_x, current_cell_abs_y = current_cell_x * tile, current_cell_y * tile

        self._check_wall_collision(current_cell, thickness, tile, current_cell_abs_x, current_cell_abs_y)

        self.rect = pygame.Rect(int(self.x), int(self.y), self.player_size, self.player_size)

    # метод для получения текущей ячейки игрока
    def _get_current_cell(self, x, y, grid_cells):
        for cell in grid_cells:
            if cell.x == x and cell.y == y:
                return cell

    # метод для проверки столкновений с стенами
    def _check_wall_collision(self, current_cell, thickness, tile, current_cell_abs_x, current_cell_abs_y):
        if self.x <= current_cell_abs_x + thickness:
            self.x = current_cell_abs_x + thickness
        if self.x >= current_cell_abs_x + tile - (self.player_size + thickness):
            self.x = current_cell_abs_x + tile - (self.player_size + thickness)
        if self.y <= current_cell_abs_y + thickness:
            self.y = current_cell_abs_y + thickness
        if self.y >= current_cell_abs_y + tile - (self.player_size + thickness):
            self.y = current_cell_abs_y + tile - (self.player_size + thickness)

    # модель игрока
    def hero(self):
        # ...
        self.running_images = [pygame.image.load('\img\run1.png'),
                               pygame.image.load('\img\run2.png'),
                               pygame.image.load('\img\run3.png'),
                               pygame.image.load('\img\run4.png'),
                               pygame.image.load('\img\run5.png'),
                               pygame.image.load('\img\run6.png'),
                               pygame.image.load('\img\run7.png'),
                               pygame.image.load('\img\run8.png'),
                               pygame.image.load('\img\run9.png'),
                               pygame.image.load('\img\run10.png'),]
        self.standing_image = pygame.image.load('\img\stand.png')
        self.current_image = self.standing_image
        self.current_frame = 0
        self.is_running = False
