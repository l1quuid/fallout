from objects import *
player = Player(player_image, 100, 100, 50, 50, 3)
game = True

for i in range(10):
    enemy = Enemy(zombie_images[0], 100, 100, 50, 50, 1.5)
    enemy.spawn()
    enemies.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game:
        print(player.hp)
        win.blit(background_image, (0, 0))
        for enemy in enemies:
            dx = enemy.rect.centerx - player.rect.centerx
            dy = player.rect.centery - enemy.rect.centery
            ang = -math.atan2(dy, dx) - math.pi
            enemy.update(ang)
            enemy.draw()

            if player.hitbox.colliderect(enemy.hitbox):
                damage_sound.play()
                player.hp -= 20
                enemy.spawn()

        collide = pygame.sprite.groupcollide(bullets, enemies,True, False)
        for bullet in collide:
            for enemy in collide[bullet]:
                enemy.hp -= 1
                if enemy.hp <= 0:
                    coin_sound.play()
                    enemy.spawn()

        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)

        pygame.draw.rect(win, interface_color, interface_rect)

        f1 = pygame.font.Font(None, 60)
        f2 = pygame.font.Font(None, 80)
        text = f1.render(str(player.hp), 1, (0, 255, 0))
        hpicon = f2.render("+", 1, (0, 255, 0))
        win.blit(text, (615, 507))
        win.blit(hpicon, (585, 495))



    pygame.display.update()
    clock.tick(FPS)