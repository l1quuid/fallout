import random

import pygame.transform
import math

from settings import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()

        self.w = w
        self.h = h
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (w, h))
        self.start_image = self.image

        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, w / 2, h / 2)

    def change_image(self, new_image):
        self.image = pygame.transform.scale(pygame.image.load(new_image).convert_alpha(), (self.w, self.h))
        self.start_image = self.image
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))


    def draw(self):
        win.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__(image, x, y, w, h, speed)
        self.max_hp = 100
        self.hp = self.max_hp
        self.reload = 0
        self.rate = 20


    def update(self):
        self.hitbox.center = self.rect.center

        keys = pygame.key.get_pressed()
        mp = pygame.mouse.get_pressed()

        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[pygame.K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.centerx += self.speed
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.centery += self.speed

        if mp[0]:
            if self.reload == 0:
                self.fire()
                self.reload = self.rate

        if self.reload != 0:
            self.reload -= 1




        pos = pygame.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]
        ang = math.degrees(math.atan2(dy, dx))

        self.rotate(ang)

    def fire(self):
        pistol_sound.set_volume(0.05)
        pistol_sound.play()

        pos = pygame.mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]
        ang = -math.atan2(dy, dx)
        b = Bullet(bullet_image, self.rect.centerx, self.rect.centery, 20, 20, 60, ang)
        bullets.add(b)

class Bullet(GameSprite):
    def __init__(self, image, x, y, w, h, speed, angle):
        super().__init__(image, x, y, w, h, speed)
        self.angle = angle

    def update(self):
        self.hitbox.center = self.rect.center
        self.rotate(math.degrees(-self.angle))
        self.rect.x += math.cos(self.angle) * self.speed
        self.rect.y += math.sin(self.angle) * self.speed

class Enemy(GameSprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__(image, x, y, w, h, speed)
        self.max_hp = 1
        self.hp = self.max_hp

    def spawn(self):
        self.change_image(random.choice(zombie_images))
        self.hp = self.max_hp

        place = random.randint(1,4)
        if place == 1:
            self.rect.x = random.randint(0, win_width)
            self.rect.y = -100
        elif place == 2:
            self.rect.x = win_width + 100
            self.rect.y = random.randint(0, win_height)
        elif place == 3:
            self.rect.x = random.randint(0, win_width)
            self.rect.y = win_height + 100
        elif place == 4:
            self.rect.x = -100
            self.rect.y = random.randint(0, win_height)

    def update(self, angle):
        self.hitbox.center = self.rect.center
        self.rotate(math.degrees(-angle))
        self.rect.x += math.cos(angle) * self.speed
        self.rect.y += math.sin(angle) * self.speed




