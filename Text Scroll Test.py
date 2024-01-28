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

counter = 0
speed = 10
active_message = 0
message = messages[active_message]
done = False
counter_rounded = 0


def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    render_text = font.render(display_text, True, pygame.Color("coral"))
    screen.blit(render_text, (text_location.x, text_location.y))


class ScrollText:
    def __init__(self, text_, speed_, delta_time):
        self.text = text_
        self.dt = delta_time
        self.speed = speed_
        # Setting the counter
        self.counter = 0
        self.counter_rounded = 0
        self.snip = font.render("", True, "white")
        self.screen = screen

    def update(self):
        if self.counter < len(self.text):
            self.counter += (self.dt * self.speed)
            self.counter_rounded = round(self.counter)

    def render(self, ):
        self.update()
        self.snip = font.render(self.text[0:counter_rounded], True, "white")
        self.screen.blit(self.snip, (10, 500))


def render():
    screen.fill("black")

    show_text(message[0:counter_rounded], (10, 310))
    show_text(f'FPS: {str(int(clock.get_fps()))}', (10, 0))
    show_text(f'Delta Time: {str(dt)}', (500, 0))
    show_text(f'Timeer: {str(int(timer))}', (700, 0))

    text1.render()

    pygame.display.flip()


text1 = ScrollText("Check this sick message", 10, dt)

while running:
    # fill the screen with a color to wipe away anything from last frame
    dt = clock.tick(60) / 1000
    timer += dt
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
