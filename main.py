from database import Database
from objects import *
import database
import random


db = Database("database.json")
game = False
finish = True
restart = False
menu = True
shop = False
sett = False
scores = 0
enemyspd = random.randint(15, 20) / 10
coins = db.get_coins()
boss_round = False

def callback_start():
    global game, boss_round, finish, scores, player
    player = Player(player_image, 100, 100, 50, 50, 3)
    game = True
    enemies.empty()
    for i in range(10):
        enemy = Enemy(zombie_images[0], 100, 100, 50, 50, enemyspd)
        enemy.spawn()
        enemies.add(enemy)
        finish = False
        scores = 0
        boss_round = False
        pygame.mixer.music.play()

def callback_menu():
    global game, menu, restart, shop
    menu = True
    game = False
    restart = False
    shop = False

def callback_shop():
    global game, menu, shop, restart, sett
    menu = False
    game = False
    shop = True
    sett = False
    restart = False

def callback_sett():
    global game, menu, shop, restart, sett
    menu = False
    game = False
    shop = False
    restart = False
    sett = True

def callback_buy():


menu_color = (171, 154, 99)
bt_start = Button(win_width / 2, 420, 190, 70, (menu_color), bt_start_text, callback=callback_start)
bt_restart = Button(190, 385, 150, 50, (50, 50, 100), bt_restart_text, callback=callback_start)
bt_menu = Button(190, 455, 150, 50, (50, 50, 100), bt_menu_text, callback=callback_menu)
bt_shop = Button(win_width / 2 - 190, 420, 150, 50, (menu_color), bt_shop_text, callback=callback_shop)
bt_sett = Button(win_width / 2 + 190, 420, 150, 50, (menu_color), bt_setting_text, callback=callback_sett)
bt_back = Button(85, 45, 150, 50, (menu_color), bt_back_text, callback=callback_menu)
bt_buy = Button(130, 478, 150, 50, (50, 205, 50), bt_buy_text, callback=callback_menu)
bt1_buy = Button(345, 478, 150, 50, (50, 205, 50), bt_buy_text, callback=callback_menu)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    acoins_text = ui_font.render(f"Total Coins: {coins}", True, (240, 231, 90))
    ak_text = ui_font.render("AK-47", True, (109, 49, 19))
    akd_text = ui_font.render("2.0", True, (220, 20, 60))
    akt_text = ui_font.render("0.3s", True, (0, 191, 255))
    akp_text = ui_font.render("450", True, (0, 255, 0))
    shotg_text = ui_font.render("Shotgun", True, (109, 49, 19))
    shotgd_text = ui_font.render("4.0", True, (220, 20, 60))
    shotgt_text = ui_font.render("1.0s", True, (0, 191, 255))
    shotgp_text = ui_font.render("800", True, (0, 255, 0))

    if shop:
        win.blit(backshop_image,(0, 0))
        bt_back.update()
        bt_back.draw()
        bt_buy.update()
        bt_buy.draw()
        bt1_buy.update()
        bt1_buy.draw()
        win.blit(acoins_text, (400, 30))
        win.blit(shotgun_image, (268,135))
        win.blit(ak_image, (50, 163))
        win.blit(ak_text, (77, 260))
        win.blit(akd_text, (97, 320))
        win.blit(akt_text, (104, 355))
        win.blit(akp_text, (97, 390))
        win.blit(shotg_text, (274, 260))
        win.blit(shotgd_text, (310, 320))
        win.blit(shotgt_text, (315, 355))
        win.blit(shotgp_text, (310, 390))


    if sett:
        win.blit(backset_image, (0, 0))
        bt_back.update()
        bt_back.draw()

    if menu:
        win.blit(menu_image, (0, 0))
        bt_start.update()
        bt_start.draw()
        bt_shop.update()
        bt_shop.draw()
        bt_sett.update()
        bt_sett.draw()

    if restart:
        bt_restart.update()
        bt_restart.draw()
        bt_menu.update()
        bt_menu.draw()

    if game:
        menu = False
        shop = False
        restart = False
        sett = False
        win.blit(background_image, (0, 0))
        for enemy in enemies:
            dx = enemy.rect.centerx - player.rect.centerx
            dy = player.rect.centery - enemy.rect.centery
            ang = -math.atan2(dy, dx) - math.pi
            enemy.update(ang)
            enemy.draw()

            if player.hitbox.colliderect(enemy.hitbox):
                if enemy.w == 50:
                    damage_sound.play()
                    player.hp -= 100
                    enemy.spawn()
                else:
                    damage_sound.play()
                    player.hp -= 20
                    enemy.kill()
                    boss_round = False


        collide = pygame.sprite.groupcollide(bullets, enemies,True, False)
        for bullet in collide:
            for enemy in collide[bullet]:
                enemy.hp -= 1
                if enemy.hp <= 0:
                    if enemy.w == 50:
                        coin_sound.play()
                        enemy.spawn()
                        scores += 1
                    else:
                        coins_sound.play()
                        enemy.kill()
                        scores += 10
                        boss_round = False

        if scores % 15 == 0 and scores != 0 and not boss_round:
            boss = Enemy(zombie_images[0], 100, 100, 100, 100, 2)
            boss.max_hp = 15
            boss.spawn()
            enemies.add(boss)
            boss_round = True

        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)

        pygame.draw.rect(win, interface_color, interface_rect)

        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 70)
        text = f1.render(str(player.hp), 1, (0, 255, 0))
        hpicon = f2.render("+", 1, (0, 255, 0))
        win.blit(text, (615, 507))
        win.blit(hpicon, (585, 497))
        score_text = ui_font.render(f"Coins: {scores}", True, (200, 200, 100))
        win.blit(score_text, (win_width - score_text.get_rect().width - 540, win_height + 7))

        if player.hp <= 0:
            pygame.mixer.music.stop()
            death_sound.play()
            win.blit(death_image, (0, 0))
            coins = coins + scores
            db.save_record(scores)
            record = db.get_record()
            db.save_coins(coins)
            coins = db.get_coins()
            highr_text = ui_font.render(f"High record: {record}", True, (50, 50, 210))
            ecoins_text = ui_font.render(f"Earned Coins: {scores}", True, (240, 231, 90))
            win.blit(highr_text, (330, 350))
            win.blit(acoins_text, (330, 400))
            win.blit(ecoins_text, (330, 450))
            game = False
            restart = True



    pygame.display.update()
    clock.tick(FPS)