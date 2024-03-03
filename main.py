import pygame
import sys
from maze import Maze
from player import Player
from game import Game
from clock import Clock


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("cyan")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()

    def _handle_events(self, player, maze):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not self.game_over and event.type == pygame.KEYDOWN:
                player.handle_keydown(event.key)
            if not self.game_over and event.type == pygame.KEYUP:
                player.handle_keyup(event.key)
        if not self.game_over and player.has_moved():
            player.check_move(maze.tile, maze.grid_cells, maze.thickness)

    def _update_game(self, maze, player, game, clock):
        self.screen.fill("gray")
        self.screen.fill(pygame.Color("darkslategray"), (603, 0, 752, 752))
        [cell.draw(self.screen, maze.tile) for cell in maze.grid_cells]
        game.add_goal_point(self.screen)
        player.draw(self.screen)
        player.update()
        if self.game_over:
            clock.stop_timer()
            self.screen.blit(game.message(), (610, 120))
        else:
            clock.update_timer()
            self.screen.blit(clock.display_timer(), (625, 200))
        pygame.display.flip()

    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[-1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        clock = Clock()

        maze.generate_maze()
        clock.start_timer()

        while self.running:
            self._handle_events(player, maze)
            if game.is_game_over(player):
                self.game_over = True
                player.reset_movement()

            self._update_game(maze, player, game, clock)
            self.FPS.tick(60)


if __name__ == "__main__":
    window_size = (600, 600)
    screen = (window_size[0] + 150, window_size[-1])
    tile_size = 30
    screen = pygame.display.set_mode(screen)
    pygame.display.set_caption("Maze")

    game = Main(screen)
    game.main(window_size, tile_size)
