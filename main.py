from objects import *
player = Player(player_image, 100, 100, 50, 50, 5)
game = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game:
        win.blit(background_image, (0, 0))
        player.update()
        player.draw()
        bullets.update()
        bullets.draw(win)




    pygame.display.update()
    clock.tick(FPS)