#https://www.youtube.com/watch?v=9bBgyOkoBQ0

import pygame
import sys
import random

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDZISE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDZISE
GRID_HEIGHT = SCREEN_WIDTH / GRIDZISE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class snake_class(object):
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 34, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDZISE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDZISE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice(UP, DOWN, LEFT, RIGHT)

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDZISE, GRIDZISE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.type == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.type == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.type == pygame.K_RIGHT:
                    self.turn(RIGHT)

class food_class(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDZISE, random.randint(0, GRID_HEIGHT-1) * GRIDZISE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDZISE, GRIDZISE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDZISE, y*GRIDZISE), (GRIDZISE, GRIDZISE))
                pygame.draw.rect(surface, (93, 216, 228), r)



def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake_class()
    food = food_class()

    myfont = pygame.font.SysFont("monospace", 16)

    score = 0
    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 00))
        text = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        screen.blit(surface, (0, 0))
        pygame.display.update()

main()
