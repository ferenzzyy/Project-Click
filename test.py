# Example file showing a circle moving on screen
import math

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()
running = True
dt = 0
timer = 0
# counter = 0
# Text
text = "Yeah"


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    display_text = font.render(text, True, pygame.Color("coral"))
    # return display_text
    screen.blit(display_text, (text_location.x,text_location.y))


def scroll_text(text, location, timer, speed): # THe time is
    display_text = text
    text_location = pygame.Vector2(location)
    text_speed = 0
    done = False
    timing = 0
    timing = timer
    text_speed += math.floor(timing * speed)
    show_text(display_text[0:text_speed], (text_location.x, text_location.y))



while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    text = "bruh"
    timer += dt
    scroll_text("THIS IS INSANE!", (0, 0), timer, 15)
    scroll_text("THIS IS INSANE!", (0, 10), timer, 15)
    show_text(str(int(clock.get_fps())), (1100, 15))

    # counter = math.floor(timer)
    # print(counter)
    # show_text(text[0:counter],(0,0))
    # scroll_text(text,(0,0),3)


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # screen.blit(show_text(f'Timer: {timer}'), (1100, 0))  # Shows Points
    # text = "bruh"
    # show_text(text[0], (0,0))
    show_text(f'Timer: {timer}', (1100,0))


    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()