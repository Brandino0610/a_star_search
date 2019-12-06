from pygame import Rect


class Node:

    def __init__(self, x, y, parent=None):
        self.parent = parent
        self.list = None
        self.x = x
        self.y = y
        self.rectangle = Rect

        self.terrain = 1
        self.f = 0
        self.g = 0
        self.h = 0
        self.c = 1

    def __eq__(self, other):
        return self.x == other.y and self.y == other.y
