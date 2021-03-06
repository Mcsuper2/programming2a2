# dvdblock.py

# Initial goal: get a block moving on the screen
#        * x and y direction
#        * modify its velocity
# Stretch goal: replace the block with an image of
#        the dvd logo (like the Office Segment)

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "DVD Image"


class Block:
    def __init__(self):
        # initial loc in the middle
        self.x, self.y = (WIDTH/2, HEIGHT/2)
        self.width, self.height = (125, 100)
        self.colour = SKY_BLUE
        self.x_vel = 3
        self.y_vel = 3

    def update(self):
        """updates the x- and y- location of the block
        based on its x_vel and y_vel
        Returns: None
        """
        self.x += self.x_vel
        self.y += self.y_vel

        # TODO: bounce the block when it reaches the sides
        # TODO:    for x
        if self.x < 0 or self.x + self.width > WIDTH:
            self.x_vel *= -1
        if self.y < 0 or self.y + self.height > HEIGHT:
            self.y_vel *= -1

    def draw(self, screen):
        """draws this block on the screen
        arguments:
            screen = surface we draw on

        returns:
            none
        """
        pygame.draw.rect(
            screen,
            self.colour,
            [
                self.x,
                self.y,
                self.width,
                self.height,
            ]
        )


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    block = Block()
    secondblock = Block()
    secondblock.colour = WHITE
    secondblock.y_vel = random.choice([-4, -2, 2, 4])
    secondblock.x_vel = random.choice([-4, -2, 2, 4])

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        block.update()  # update the block's location
        secondblock.update()

        # ----- DRAW
        screen.fill(BLACK)

        # Draw method
        # input is screen
        # pygame.draw.rect()

        block.draw(screen)
        secondblock.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
