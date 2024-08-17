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
        win.blit(background_image, (0, 0))
        for enemy in enemies:
            dx = enemy.rect.centerx - player.rect.centerx
            dy = player.rect.centery - enemy.rect.centery
            ang = -math.atan2(dy, dx) - math.pi
            enemy.update(ang)
            enemy.draw()

        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)




    pygame.display.update()
    clock.tick(FPS)