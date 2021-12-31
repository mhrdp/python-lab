import os
import pygame
import random
import time

pygame.init()

# Window
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

X_WIDTH = 800
Y_HEIGHT = 600

DISPLAY = pygame.display.set_mode((X_WIDTH, Y_HEIGHT))
# BG = pygame.transform.scale(
#    pygame.image.load(os.path.join('assets', 'bg_space.png')),
#    (X_WIDTH, Y_HEIGHT)
#)

pygame.display.set_caption('Space Battle')

# Game assets
SPACESHIP = pygame.image.load(os.path.join('assets', 'space-invaders.png'))
SPACESHIP_LASER = pygame.image.load(os.path.join('assets', 'vertical-line.png'))

ENEMY_1 = pygame.image.load(os.path.join('assets', 'project.png'))
# Abstract class, meaning we only use it to store variable
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    
    def move(self, velocity):
        self.y += velocity

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, velocity, obj):
        self.Cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(Y_HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def Cooldown(self):
        if self.cooldown >= self.COOLDOWN:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def shoot(self):
        if self.cooldown == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cooldown = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = SPACESHIP
        self.laser_img = SPACESHIP_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    
    def move_lasers(self, velocity, objs):
        self.Cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_screen(Y_HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Ship):
    ENEMY = {
        '1': (ENEMY_1, SPACESHIP_LASER),
        '2': (ENEMY_1, SPACESHIP_LASER),
    }
    def __init__(self, x, y, ship_type, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.ENEMY[ship_type]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, velocity):
        self.y += velocity

    def shoot(self):
        if self.cooldown == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    main_font = pygame.font.SysFont('comicsansms', 25)
    danger_font = pygame.font.SysFont('comicsansms', 30)

    run = True
    lost = False

    FPS = 60
    level = 0
    lives = 5
    lost_count = 0

    velocity = 5

    enemies = []
    wave_length = 5
    enemy_velocity = 1
    laser_velocity = 4

    clock = pygame.time.Clock()
    ship = Player(300, 450)

    def redraw_window():
        DISPLAY.fill(WHITE)

        lives_label = main_font.render(f'Lives: {lives}', 1, (0, 0, 0))
        level_label = main_font.render(f'Level: {level}', 1, (0, 0, 0))

        DISPLAY.blit(lives_label, (10, 10))
        DISPLAY.blit(level_label, (X_WIDTH - level_label.get_width() - 10, 10))
        
        for enemy in enemies:
            enemy.draw(DISPLAY)

        ship.draw(DISPLAY)

        if lost:
            lost_label = danger_font.render('YOU LOST!', 1, (255, 0, 0))
            DISPLAY.blit(lost_label, (X_WIDTH/2-lost_label.get_width()/2, 300))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or ship.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                enemy = Enemy(random.randrange(100, X_WIDTH-50), random.randrange(-1500, -100), random.choice(['1', '2']))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # To move in all direction
        # keys will return a dict of all keys in pygame
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x + velocity > 0:
            ship.x -= velocity
        if keys[pygame.K_RIGHT] and ship.x + velocity + ship.get_width() < X_WIDTH:
            ship.x += velocity
        if keys[pygame.K_UP] and ship.y - velocity > 0:
            ship.y -= velocity
        if keys[pygame.K_DOWN] and ship.y + velocity + ship.get_height() < Y_HEIGHT:
            ship.y += velocity
        if keys[pygame.K_SPACE]:
            ship.shoot()
        
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_LEFT]:
                ship.x -= (-1 * (velocity-2))
            if keys[pygame.K_RIGHT]:
                ship.x += (-1 * (velocity-2))
            if keys[pygame.K_UP]:
                ship.y -= (-1 * (velocity-2))
            if keys[pygame.K_DOWN]:
                ship.y += (-1 * (velocity-2))
        
        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            enemy.move_lasers(laser_velocity, ship)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()
            
            if collide(enemy, ship):
                ship.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > Y_HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        
        ship.move_lasers(-laser_velocity, enemies)


if __name__ == '__main__':
    main()
