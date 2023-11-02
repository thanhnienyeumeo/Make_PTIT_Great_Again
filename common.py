import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_NUM = 20
GRID_SIZE = SCREEN_WIDTH // GRID_NUM

craftsman_img = pygame.image.load('craftsman.webp')
craftsman_img = pygame.transform.scale(craftsman_img, (GRID_SIZE - 5, GRID_SIZE - 5))
# Tạo màn hình Pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Title")


# Khởi tạo clock để giới hạn FPS
FPS = 60
fpsClock = pygame.time.Clock()

#change direction
change = {"":[0,0],"up": [0, -1], "down": [0, 1], "left": [-1, 0], 
          "right": [1, 0], "lower_left": [-1, 1], "lower_right": [1, 1], 
          "upper_left": [-1, -1], "upper_right": [1, -1]}