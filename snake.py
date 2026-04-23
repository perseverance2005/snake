# -*- coding: utf-8 -*-
import pygame
import sys
import random

pygame.init()

# 窗口
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# 👉 强制使用系统中文字体（绝对不乱码）
font = pygame.font.Font("C:/Windows/Fonts/simhei.ttf", 36)

# 蛇
snake = [(100, 50), (90, 50), (80, 50)]
direction = "RIGHT"

# 食物
food = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

# 分数
score = 0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # 移动
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= 10
    elif direction == "DOWN":
        head_y += 10
    elif direction == "LEFT":
        head_x -= 10
    elif direction == "RIGHT":
        head_x += 10

    new_head = (head_x, head_y)

    # 撞墙 / 撞自己
    if (head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT or
        new_head in snake):
        running = False

    snake.insert(0, new_head)

    # 吃食物
    if new_head == food:
        score += 1
        food = (random.randrange(0, WIDTH, 10),
                random.randrange(0, HEIGHT, 10))
    else:
        snake.pop()

    # 绘制
    screen.fill(BLACK)

    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, (food[0], food[1], 10, 10))

    # 中文分数
    text = font.render(f"分数: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)

# 游戏结束
screen.fill(BLACK)
text1 = font.render("游戏结束", True, WHITE)
text2 = font.render(f"最终分数: {score}", True, WHITE)

screen.blit(text1, (220, 150))
screen.blit(text2, (200, 200))

pygame.display.update()
pygame.time.wait(3000)

pygame.quit()
sys.exit()