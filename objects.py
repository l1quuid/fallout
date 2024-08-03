from settings import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()

        self.w = w
        self.h = h
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (w, h))

        self.rect = self.image.get_rect()
        self.rect.center = x, y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, w / 2, h / 2)

    def draw(self):
        win.blit(self.image)