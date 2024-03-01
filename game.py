import pygame

pygame.font.init()


class Game:
    def __init__(self, goal_cell, tile):
        self.font = pygame.font.SysFont("arial", 35)
        self.message_color = pygame.Color("darkorange")
        self.goal_cell = goal_cell
        self.tile = tile

    # добавление точки финиша
    def add_goal_point(self, screen):
        # картинка у финиша
        img_path = "/img/gate.png"
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (self.tile, self.tile))
        screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

    # победное сообщение
    def message(self):
        msg = self.font.render('You Win!!', True, self.message_color)
        return msg

    # дошел ли игрок до финиша
    def is_game_over(self, player):
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
        if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
            return True
        else:
            return False
