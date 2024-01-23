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

counter = 0
text = "Message 1 : this is the first message"
messages = ["Message1", "Message 2", "message 3"]
done = False
active_message = 0
current_message = messages[active_message]

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    display_text = font.render(text, True, pygame.Color("coral"))
    # return display_text
    screen.blit(display_text, (text_location.x, text_location.y))


def scroll_text(text, location, timer, speed):  # THe time is
    display_text = text
    text_location = pygame.Vector2(location)
    counter = 0
    timing = timer
    counter += math.floor(timing * speed)
    if counter >= len(display_text):
        # counter = 0
        global done
        done = True

    show_text(display_text[0:counter], (text_location.x, text_location.y))


while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    text = "bruh"
    timer += dt


    scroll_text("THIS IS INSANE!", (0, 0), timer, 15)
    scroll_text("THIS IS INSANE!", (0, 10), timer, 15)

    show_text(str(int(clock.get_fps())), (1100, 15))
    show_text(f'Timer: {timer}', (1100, 0))

    scroll_text(current_message, (100,10), timer, 10)




    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    # if keys[pygame.K_c] and done and active_message < len(messages):
    #     counter = 0
    #     done = False
    #     active_message += 1
    #     current_message = messages[active_message]

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
