# shmup.py
# Top down shoot-em-up (shmup) game
# Get more comfortable with sprites and mouse
#   * creation of new sprite objects in the main loop
#   * using pygame.mouse a little more comfortably

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 720
HEIGHT = 1000
TITLE = "Shmup"

# Class Player, Enemies, Bullets


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/Galaga_ship.png")  # 128x128
        self.image = pygame.transform.scale(self.image, [64, 64])
        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()

        if self.rect.y < HEIGHT - 80:
            self.rect.y = HEIGHT - 80


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/Mario.png")
        self.rect = self.image.get_rect()

        self.x_vel = 3

    def update(self):
        self.rect.x += self.x_vel

        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= -1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords):
        """
        Arguments:
            coords = tuples of x, y
        """
        super().__init__()

        self.image = pygame.image.load("./images/bullets.png")
        self.image = pygame.transform.scale(self.image, [21, 36])

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (coords)

        self.y_vel = -3

    def update(self):
        self.rect.y += self.y_vel



def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite Groups
    all_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()

    # Populate sprite groups
    enemy = Enemy()
    enemy.rect.y = 150
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # mouse button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # create a bullet where the player is
                if len(bullet_sprites) <= 3:
                    bullet = Bullet(player.rect.midtop)
                    all_sprites.add(bullet)
                    bullet_sprites.add(bullet)

        # ----- LOGIC
        all_sprites.update()
        # remove bullet if off screen
        for bullet in bullet_sprites:
            if bullet.rect.y < -20:
                bullet.kill()
            # collision
            enemy_hit_group = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
            if len(enemy_hit_group):
                bullet.kill()

            if bullet.rect.y < 0:
                bullet.kill()

            # collision


        # ----- DRAW
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()