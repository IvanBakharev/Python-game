import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна игры
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Создание игрового поля
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game")

# Размеры клетки на игровом поле
CELL_SIZE = 50

# Генерация рек
def generate_rivers():
    rivers = []
    for _ in range(5):
        x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
        y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
        rivers.append((x, y))
    return rivers

# Генерация деревьев
def generate_trees():
    trees = []
    for _ in range(10):
        x = random.randint(0, WINDOW_WIDTH // CELL_SIZE - 1)
        y = random.randint(0, WINDOW_HEIGHT // CELL_SIZE - 1)
        trees.append((x, y))
    return trees

# Проверка принадлежности клетки игровому полю
def is_valid_cell(x, y):
    return 0 <= x < WINDOW_WIDTH // CELL_SIZE and 0 <= y < WINDOW_HEIGHT // CELL_SIZE

# Основной цикл игры
def game_loop():
    running = True

    # Генерация рек и деревьев
    rivers = generate_rivers()
    trees = generate_trees()

    # Позиция вертолета
    helicopter_x = WINDOW_WIDTH // 2 // CELL_SIZE
    helicopter_y = WINDOW_HEIGHT // 2 // CELL_SIZE

    while running:
        # Отрисовка фона
        game_window.fill((0, 255, 0))
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            for x in range(0, WINDOW_WIDTH, CELL_SIZE):
                if (x // CELL_SIZE, y // CELL_SIZE) in rivers:
                    pygame.draw.rect(game_window, (0, 0, 255), (x, y, CELL_SIZE, CELL_SIZE))
                    game_window.blit(pygame.font.SysFont("Segoe UI Emoji", 30).render("🌊", True, (0, 0, 0)), (x + 10, y + 10))
                else:
                    pygame.draw.rect(game_window, (0, 255, 0), (x, y, CELL_SIZE, CELL_SIZE))
                    game_window.blit(pygame.font.SysFont("Segoe UI Emoji", 30).render("🟩", True, (0, 0, 0)), (x + 10, y + 10))

        # Отрисовка деревьев
        for tree in trees:
            x, y = tree
            game_window.blit(pygame.font.SysFont("Segoe UI Emoji", 30).render("🌳", True, (0, 0, 0)), (x * CELL_SIZE + 10, y * CELL_SIZE + 10))

        # Отрисовка вертолета
        game_window.blit(pygame.font.SysFont("Segoe UI Emoji", 30).render("🚁", True, (0, 0, 0)), (helicopter_x * CELL_SIZE + 10, helicopter_y * CELL_SIZE + 10))

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Перемещение вертолета
                if event.key == pygame.K_UP and is_valid_cell(helicopter_x, helicopter_y - 1):
                    helicopter_y -= 1
                elif event.key == pygame.K_DOWN and is_valid_cell(helicopter_x, helicopter_y + 1):
                    helicopter_y += 1
                elif event.key == pygame.K_LEFT and is_valid_cell(helicopter_x - 1, helicopter_y):
                    helicopter_x -= 1
                elif event.key == pygame.K_RIGHT and is_valid_cell(helicopter_x + 1, helicopter_y):
                    helicopter_x += 1

                # Проверка столкновения вертолета с рекой или деревом
                if (helicopter_x, helicopter_y) in rivers or (helicopter_x, helicopter_y) in trees:
                    print("Game Over")
                    running = False

        # Обновление экрана
        pygame.display.update()

# Запуск игры
game_loop()

# Завершение Pygame
pygame.quit()