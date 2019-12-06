from Node import Node
import math
import pygame

DIAGONAL = math.sqrt(2)


def search(screen, map_grid, start, goal):
    X_LENGTH = len(map_grid)
    Y_LENGTH = len(map_grid)
    open_list = []      # always sorted for lowest f value
    closed_list = []
    start_node = start
    goal_node = goal
    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        # Find lowest cost node in open list
        for index, node in enumerate(open_list):
            if node.f < current_node.f:
                current_node = node
                current_index = index

        # move current node from open to close
        open_list.pop(current_index)
        closed_list.append(current_node)
        current_node.list = 'closed'
        pygame.draw.rect(screen, (0, 255, 255), current_node.rectangle)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node.parent is not None:
                path.append([current_node.x, current_node.y])
                current_node = current_node.parent
            return path[::-1]

        child_nodes = []

        # check all possible child nodes for out of range
        if current_node.y < Y_LENGTH - 1:
            child_nodes.append(map_grid[current_node.x, current_node.y + 1])
        if current_node.x < X_LENGTH - 1 and current_node.y < Y_LENGTH - 1:
            child_nodes.append(map_grid[current_node.x + 1, current_node.y + 1])
            child_nodes[-1].c = DIAGONAL
        if current_node.x < X_LENGTH - 1:
            child_nodes.append(map_grid[current_node.x + 1, current_node.y])
        if current_node.x < X_LENGTH - 1 and current_node.y > 0:
            child_nodes.append(map_grid[current_node.x + 1, current_node.y - 1])
            child_nodes[-1].c = DIAGONAL
        if current_node.y > 0:
            child_nodes.append(map_grid[current_node.x, current_node.y - 1])
        if current_node.x > 0 and current_node.y > 0:
            child_nodes.append(map_grid[current_node.x - 1, current_node.y - 1])
            child_nodes[-1].c = DIAGONAL
        if current_node.x > 0:
            child_nodes.append(map_grid[current_node.x - 1, current_node.y])
        if current_node.x > 0 and current_node.y < Y_LENGTH - 1:
            child_nodes.append(map_grid[current_node.x - 1, current_node.y + 1])
            child_nodes[-1].c = DIAGONAL

        for node in child_nodes:
            if node.list is None:
                node.parent = current_node
                node.g = current_node.g + node.c * node.terrain
                node.h = (goal_node.x - node.x) ** 2 +\
                         (goal_node.y - node.y) ** 2
                node.f = node.g + node.h
                node.list = 'open'
                open_list.append(node)
                pygame.draw.rect(screen, (255, 255, 0), node.rectangle)
            elif node.list == 'open':
                if node.g > current_node.g + 1:
                    node.g = current_node.g + 1
                    node.parent = current_node

