import pygame
import math as M
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()
running = True
dt = 0
timer = 0

messages = ["Check this sick message",
            "THis is another message!",
            "Isn\'t programming FUN :)))))))))))))"]
snip = font.render("", True, "white")
counter = 0
speed = 3 # Higher means slower speeds
active_message = 0
message = messages[active_message]
done = False

while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    timer += dt

    if counter < speed * len(message):
        counter += 1

    elif counter >= speed  * len(message):
        done = True

    if len(messages) < 0:
        messages.append(" ")


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    snip = font.render(message[0:counter//speed], True, "white")
    screen.blit(snip, (10,310))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and done and active_message < len(messages) - 1:
        active_message += 1
        done = False
        message = messages[active_message]
        counter = 0


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()