import pygame
import math as M
# from rounding import round_up

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()
running = True
dt = 0
timer = 0

messages = ["Check this sick message",
            "This is another message!",
            "Isn\'t programming FUN :)))))))))))))"]
# snip = font.render("", True, "white")
counter = 0
speed = 10  # Higher means slower speeds
active_message = 0
message = messages[active_message]
done = False
counter_rounded = 0


def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    render_text = font.render(display_text, True, pygame.Color("coral"))
    screen.blit(render_text, (text_location.x, text_location.y))

# def scroll_text():


def render():
    screen.fill("black")

    show_text(message[0:counter_rounded], (10, 310))
    show_text(f'FPS: {str(int(clock.get_fps()))}', (10, 0))
    show_text(f'Delta Time: {str(dt)}', (500, 0))
    show_text(f'Timeer: {str(int(timer))}', (700, 0))
    show_text(f'Counter: {str(counter_rounded)}', (1000, 0))

    pygame.display.flip()





while running:
    # fill the screen with a color to wipe away anything from last frame
    dt = clock.tick(60) / 1000
    timer += dt
    # timer_ = round(timer)
    if counter < len(message):
        counter += dt * speed
        counter_rounded = round(counter)

    if counter >= len(message):
        done = True


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # snip = font.render(message[0:counter], True, "white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and done and active_message < len(messages) - 1 and counter > 0:
        counter = 0
        active_message += 1
        done = False
        message = messages[active_message]
    # flip() the display to put your work on screen
    render()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()
