from objects import *
player = Player(player_image, 100, 100, 50, 50, 3)

game = True
scores = 0
boss_round = False

for i in range(10):
    enemy = Enemy(zombie_images[0], 100, 100, 50, 50, 2)
    enemy.spawn()
    enemies.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game:
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
                    player.hp -= 10
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

        if player.hp <= 0:
            death_sound.play()
            win.blit(death_image, (0, 0))
            game = False




    pygame.display.update()
    clock.tick(FPS)