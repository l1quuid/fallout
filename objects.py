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

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color, label, callback):
        super().__init__()
        self.callback = callback
        self.color = color
        r = min(color[0] + 15, 255)
        g = min(color[1] + 15, 255)
        b = min(color[2] + 15, 255)
        self.light_color = (r, g, b)
        self.w = w
        self.h = h
        self.pressed = False

        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.center = x, y

        self.text = label
        self.label_rect = self.text.get_rect()
        self.label_rect.centerx = w / 2
        self.label_rect.centery = h / 2

        self.surface.fill(self.color)
        self.surface.blit(self.text, self.label_rect)

    def is_on(self):
        x, y = pygame.mouse.get_pos()
        on = self.rect.collidepoint(x, y)
        if on:
            self.surface.fill(self.light_color)
        else:
            self.surface.fill(self.color)
        return on

    def is_press(self):
        bt = pygame.mouse.get_pressed()
        if self.is_on() and bt[0] and not self.pressed:
            self.pressed = True
            self.callback()

        if not bt[0]:
            self.pressed = False

    def update(self):
        self.is_press()
        self.surface.blit(self.text, self.label_rect)


    def draw(self):
        win.blit(self.surface, self.rect)






