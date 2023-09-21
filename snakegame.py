import pygame
import random

# 게임 설정
WIDTH = 800
HEIGHT = 600
FPS = 10

# 색상 정의
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("꼬리잡기 게임")
clock = pygame.time.Clock()

# 게임 요소 초기화
block_size = 20
snake_speed = 20

font = pygame.font.SysFont(None, 30)

# 뱀 클래스 정의
class Snake:
    def __init__(self):
        self.segments = [(WIDTH / 2, HEIGHT / 2)]
        self.dx = block_size
        self.dy = 0

    def move(self):
        x, y = self.segments[0]
        x += self.dx
        y += self.dy
        self.segments.insert(0, (x, y))
        self.segments.pop()

    def change_direction(self, dx, dy):
        self.dx = dx * block_size
        self.dy = dy * block_size

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))

    def check_collision(self):
        if self.segments[0][0] < 0 or self.segments[0][0] >= WIDTH or self.segments[0][1] < 0 or self.segments[0][1] >= HEIGHT:
            return True
        for segment in self.segments[1:]:
            if self.segments[0] == segment:
                return True
        return False

    def check_eat(self, food):
        if self.segments[0] == food.position:
            return True
        return False

# 음식 클래스 정의
class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - block_size) // block_size * block_size,
                         random.randint(0, HEIGHT - block_size) // block_size * block_size)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], block_size, block_size))

# 게임 루프
def game_loop():
    game_over = False
    game_quit = False

    snake = Snake()
    food = Food()

    while not game_quit:
        while game_over:
            screen.fill(BLACK)
            game_over_text = font.render("게임 오버! 다시 하려면 R 키를 누르세요.", True, RED)
            screen.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2,
                                         HEIGHT / 2 - game_over_text.get_height() / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.dx != block_size:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT and snake.dx != -block_size:
                    snake.change_direction(1, 0)
                elif event.key == pygame.K_UP and snake.dy != block_size:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN and snake.dy != -block_size:
                    snake.change_direction(0, 1)

        snake.move()

        if snake.check_collision():
            game_over = True

        if snake.check_eat(food):
            snake.segments.append((food.position[0], food.position[1]))
            food = Food()

        screen.fill(BLACK)
        snake.draw()
        food.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# 게임 실행
game_loop()
