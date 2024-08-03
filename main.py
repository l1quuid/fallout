from settings import *

game = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if game:
        win.blit(background_image, (0, 0))

    pygame.display.update()
    clock.tick(FPS)