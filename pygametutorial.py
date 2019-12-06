import pygame
import math
import numpy as np
from AStarSearch import search
from Node import Node

# pygame variables
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
GRAY = (150, 150, 150, 255)
FPS = 60
MARGIN = 1
RECTANGLES = 50
RECT_SIZE = 15
WIDTH = RECTANGLES * (RECT_SIZE + MARGIN)
HEIGHT = RECTANGLES * (RECT_SIZE + MARGIN)
WINDOW_SIZE = (WIDTH, HEIGHT)

# A* variables
map_grid = np.ndarray(shape=(RECTANGLES, RECTANGLES), dtype=Node)

# Initialize display, clock, and icon
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('A Star Search')
clock = pygame.time.Clock()

# Draw Grid
for x in range(RECTANGLES):
    for y in range(RECTANGLES):
        map_grid[x, y] = Node(x, y)
        map_grid[x, y].rectangle = pygame.Rect((x * RECT_SIZE + x * MARGIN,
                                 y * RECT_SIZE + y * MARGIN),
                                 (RECT_SIZE, RECT_SIZE))
        pygame.draw.rect(screen, GRAY, map_grid[x, y].rectangle)

START_X = 5
START_Y = RECTANGLES // 4
GOAL_X = 45
GOAL_Y = 45

start_node = map_grid[START_X, START_Y]
goal_node = map_grid[GOAL_X, GOAL_Y]
pygame.draw.rect(screen, BLUE, start_node.rectangle)
pygame.draw.rect(screen, BLACK, goal_node.rectangle)

# Game Loop
running = True
while running:
    clock.tick(FPS)

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left Click
            if pygame.mouse.get_pressed() == (True, False, False):
                mouse_pos = pygame.mouse.get_pos()
                column = mouse_pos[0] // (RECT_SIZE + MARGIN)
                row = mouse_pos[1] // (RECT_SIZE + MARGIN)
                pygame.draw.rect(screen, RED, map_grid[column, row].rectangle)
                map_grid[column, row].terrain = 10000000
                print("Left Click ", mouse_pos, "Grid coordinates: ", row, column)
            # Right Click
            elif pygame.mouse.get_pressed() == (False, False, True):
                mouse_pos = pygame.mouse.get_pos()
                row = mouse_pos[0] // (RECT_SIZE + MARGIN)
                column = mouse_pos[1] // (RECT_SIZE + MARGIN)
                if goal_node is not map_grid[row, column]:
                    pygame.draw.rect(screen, GRAY, goal_node.rectangle)
                    pygame.display.update(goal_node.rectangle)
                    goal_node = map_grid[row, column]
                    pygame.draw.rect(screen, BLACK, goal_node.rectangle)
                    print("Right Click ", mouse_pos, "Grid coordinates: ", row, column)
            # Middle Click
            elif pygame.mouse.get_pressed() == (False, True, False):
                path = search(screen, map_grid, start_node, goal_node)
                for x, y in path:
                    pygame.draw.rect(screen, GREEN, map_grid[x, y].rectangle)
                    pygame.display.update(map_grid[x, y].rectangle)
                pygame.draw.rect(screen, BLUE, start_node.rectangle)
                pygame.draw.rect(screen, BLACK, goal_node.rectangle)

    # Update display before loop terminates
    pygame.display.update()
# End Game Loop

pygame.quit()
