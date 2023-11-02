import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Định nghĩa một số hằng số
from common import *

#Lớp cho board
class GameBoard:
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.board = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.player = {}
    def place_craftsman(self, x, y, craftsman):
        self.board[x][y] = craftsman

    def remove_craftsman(self, x, y):
        if self.board[x][y]:
            self.board[x][y] = None

    def build_wall(self, x, y, player):
        if self.board[x][y] is None:
            self.board[x][y] = player  # Đánh dấu ô này thuộc về người chơi

    def destroy_wall(self, x, y):
        if isinstance(self.board[x][y], Player):
            self.board[x][y] = None

    def place_castle(self, x, y):
        # Đánh dấu ô này là có castle
        self.board[x][y] = "Castle"

    def get_cell_state(self, x, y):
        return self.board[x][y]

    def is_occupied(self, x, y):
        return self.board[x][y] is not None

    def is_castle(self, x, y):
        return self.board[x][y] == "Castle"

    def draw_grid(self):
    
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))
        #left of a grid: x * GRID_SIZE
        #right of a grid: (x + 1) * GRID_SIZE
        for x in range(0, self.grid_size - 1):
            for y in range(0, self.grid_size - 1):
                if(self.board[x][y] == "Castle"):
                    
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                elif self.board[x][y] is not None: #has wall here
                    player = self.board[x][y]
                    pygame.draw.rect(screen, player.color, pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                #elif is_occupied(x, y):
        def reCheck(self):
            pass

# Lớp cho craftsmen
class Craftsman:
    def __init__(self, x = 1, y=1, player = 0):
        self.x = x
        self.y = y
        self.player = player  # Người chơi sở hữu
        
    def move(self, direction):
        self.x += change[direction][0]
        self.y += change[direction][1]
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.y >= GRID_NUM:
            self.y = GRID_NUM - 1
        if self.x >= GRID_NUM:
            self.x = GRID_NUM - 1

    def draw(self):
        # Vẽ craftsmen
        screen.blit(craftsman_img, (self.x * GRID_SIZE + 2, self.y * GRID_SIZE + 2))
    def build_wall(self, direction):
        # Xây tường ở ô bên cạnh
        pass

    def destroy_wall(self, wall):
        # Phá tường ở ô bên cạnh
        pass

# Lớp cho người chơi
class Player:
    def __init__(self, name = 'a', player = 0):
        self.name = name
        self.walls = 0
        self.territory = []
        self.player = player
        self.color = (153, 134, 129)
        if(self.player):
            self.color = (118, 179, 214)
    def update_territory(self, territory):
        # Cập nhật khu vực đất
        pass

    def update_walls(self, walls):
        # Cập nhật số tường
        pass

# Lớp cho tường
class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Ví dụ về tạo một người chơi và một craftsmen
player1 = Player(0)
player2 = Player(name = 'b', player = 1)

craftsman1 = Craftsman(5, 4, player1)
craftsman2 = Craftsman(10, 10, player2)

gameBoard = GameBoard(20)
# Vòng lặp chính
running = True


while running:
    action = "move"
    action_param = ""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                action_param = "left"
            elif (event.key == pygame.K_RIGHT):
                action_param = "right"
            elif (event.key == pygame.K_UP):
                action_param = "up"
            elif (event.key == pygame.K_DOWN):
                action_param = "down"
            elif (event.key == pygame.K_SPACE):
                action = "build"
    # Xử lý các sự kiện và logic trò chơi ở đây
    if action == "move":
        craftsman1.move(action_param)
    elif action == "build":
        pass
    elif action == "destroy":
        pass
    # Xóa màn hình và vẽ lại grid
    screen.fill((255, 255, 255))
    gameBoard.place_castle(3,4)

    gameBoard.build_wall(3, 5, player1)
    gameBoard.build_wall(5,6, player2)
    gameBoard.draw_grid()

    # Vẽ các đối tượng và người chơi ở đây
    craftsman1.draw()
    pygame.display.update()
    fpsClock.tick(FPS)

# Kết thúc Pygame
pygame.quit()
sys.exit()
