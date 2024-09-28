import pygame
pygame.init()
pygame.mixer.init()

win_width = 700
win_height = 500
FPS = 54

win = pygame.display.set_mode((win_width, win_height + 50))
clock = pygame.time.Clock()

background_image = pygame.transform.scale(pygame.image.load("textures/backg.jpg"), (win_width, win_height))
backshop_image = pygame.transform.scale(pygame.image.load("textures/shop1.png"), (win_width, win_height + 50))
backset_image = pygame.transform.scale(pygame.image.load("textures/shop.png"), (win_width, win_height + 50))
menu_image = pygame.transform.scale(pygame.image.load("textures/menu.jpg"), (win_width, win_height + 50))
death_image = pygame.transform.scale(pygame.image.load("textures/yd.jpg"), (win_width, win_height + 50))
player_image = 'textures/ppistol.gif'
zombie_images = ['textures/zombie.png', 'textures/lzombie.png', 'textures/big zombie.png']
bullet_image = 'textures\\bullet.png'
heal_image = 'textures\\heal.png'
shotgun_image = pygame.transform.scale(pygame.image.load('textures\\shotgun.png'), (150, 150))
ak_image = pygame.transform.scale(pygame.image.load('textures\\ak47.png'), (160, 100))

fire_sound = pygame.mixer.Sound('sounds\\fire.ogg')
pistol_sound = pygame.mixer.Sound('sounds\\pistolf.mp3')
coin_sound = pygame.mixer.Sound('sounds\\coin.ogg')
coins_sound = pygame.mixer.Sound('sounds\\coins.ogg')
damage_sound = pygame.mixer.Sound('sounds\\damage.ogg')
death_sound = pygame.mixer.Sound('sounds\\death.ogg')
levelup_sound = pygame.mixer.Sound('sounds\\levelup.ogg')
heal_sound = pygame.mixer.Sound('sounds\\heal.ogg')
error_sound = pygame.mixer.Sound('sounds\\error.ogg')
choice_sound = pygame.mixer.Sound('sounds\\choice.ogg')
buy_sound = pygame.mixer.Sound('sounds\\buy.ogg')

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

interface_rect = pygame.Rect(0, win_height, win_width, 50)
interface_color = (150,150,100)

pistol_sound.set_volume(0.32)
coin_sound.set_volume(0.3)
coins_sound.set_volume(0.3)
damage_sound.set_volume(0.2)
pygame.mixer.music.set_volume(0.15)

ui_font = pygame.font.Font(None, 50)
md_font = pygame.font.Font(None, 60)
st_font = pygame.font.Font(None, 70)
menutx_color = (234, 230, 212)
bt_start_text = st_font.render("Start", True, (menutx_color))
bt_restart_text = ui_font.render("Restart", True, (255, 255, 255))
bt_menu_text = ui_font.render("Menu", True, (255, 255, 255))
bt_shop_text = ui_font.render("Shop", True, (menutx_color))
bt_setting_text = ui_font.render("Settings", True, (menutx_color))
bt_back_text = ui_font.render("Back", True, (menutx_color))
bt_buy_text = ui_font.render("Buy", True, (212, 251, 212))

pygame.mixer.music.load('sounds/music.wav')