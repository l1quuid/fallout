import pygame
pygame.init()
pygame.mixer.init()

win_width = 700
win_height = 500
FPS = 60

win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

background_image = pygame.transform.scale(pygame.image.load("textures/backg.jpg"), (win_width, win_height))
menu_image = pygame.transform.scale(pygame.image.load("textures/menu.jpg"), (win_width, win_height))
player_image = 'textures/ppistol.gif'
zombie_images = ['textures/zombie.png', 'textures/lzombie.png', 'textures/big zombie.png']
bullet_image = 'textures\\bullet.png'
heal_image = 'textures\\heal.png'

fire_sound = pygame.mixer.Sound('sounds\\fire.ogg')
coin_sound = pygame.mixer.Sound('sounds\\coin.ogg')
coins_sound = pygame.mixer.Sound('sounds\\coins.ogg')
damage_sound = pygame.mixer.Sound('sounds\\damage.ogg')
death_sound = pygame.mixer.Sound('sounds\\death.ogg')
levelup_sound = pygame.mixer.Sound('sounds\\levelup.ogg')
heal_sound = pygame.mixer.Sound('sounds\\heal.ogg')
error_sound = pygame.mixer.Sound('sounds\\error.ogg')
choice_sound = pygame.mixer.Sound('sounds\\choice.ogg')
buy_sound = pygame.mixer.Sound('sounds\\buy.ogg')

#pygame.mixer.music.load('sounds\\music.mp3')