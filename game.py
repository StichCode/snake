import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Multiplayer snake")

x = 250
y = 250
height = 10
width = 10
speed = 5


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - speed:
        x += speed
    if keys[pygame.K_UP] and y > speed:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - speed:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
