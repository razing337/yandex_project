import pygame
import time

pygame.font.init()


class Clock:
    def __init__(self):
        self.reset_timer()

    def reset_timer(self):
        self.start_time = None
        self.elapsed_time = 0
        self.font = pygame.font.SysFont("monospace", 35)
        self.message_color = pygame.Color("white")

    def start_timer(self):
        self.start_time = time.time()

    def get_elapsed_time(self):
        if self.start_time is not None:
            self.elapsed_time = time.time() - self.start_time
        return self.elapsed_time

    def format_time(self, elapsed_time):
        secs = int(elapsed_time % 60)
        mins = int(elapsed_time / 60)
        formatted_time = f"{mins:02}:{secs:02}"
        return formatted_time

    def display_timer(self):
        elapsed_time = self.get_elapsed_time()
        my_time = self.font.render(self.format_time(elapsed_time), True, self.message_color)
        return my_time

    def stop_timer(self):
        self.start_time = None
