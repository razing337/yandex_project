import pygame
import sys
import os


pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Нажмите любую кнопку, чтобы начать")

background_image = pygame.image.load("/img/backround.png")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 36)


# Функция отрисовки начального экрана
def draw_start_screen():
    WIN.blit(background_image, (0, 0))
    text = font.render("Нажмите любую кнопку, чтобы начать", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WIN.blit(text, text_rect)
    pygame.display.update()


def main():
    draw_start_screen()
    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                start = True

    os.system('python main.py')


if __name__ == "__main__":
    main()
    # стартовое окно
