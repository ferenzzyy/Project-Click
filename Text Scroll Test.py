import pygame

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
count = 0


def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    render_text = font.render(display_text, True, pygame.Color("coral"))
    screen.blit(render_text, (text_location.x, text_location.y))


class ScrollText:
    counter = 0

    def __init__(self, text_, speed_, location_):
        self.display_t = text_
        self.t_speed = speed_
        self.location = pygame.Vector2(location_)
        self.counter_rounded = round(ScrollText.counter)
        self.done = False

    def update(self):
        if self.counter < len(self.display_t):
            ScrollText.counter += (dt * self.t_speed)
        elif self.counter >= len(self.display_t):
            self.done = True

        snip_ = font.render(self.display_t[0:self.counter_rounded], True, "white")
        screen.blit(snip_, (self.location.x, self.location.y))


def scroll_text(text, location, speed_):
    global counter
    global counter_rounded
    global done
    t_speed = speed_
    display_text = text
    text_location = pygame.Vector2(location)

    if counter < len(display_text):
        counter += dt * t_speed
        counter_rounded = round(counter)

    if counter >= len(display_text):
        done = True

    show_text(display_text[0:counter_rounded], (text_location.x, text_location.y))


def render():
    screen.fill("black")

    show_text(f'FPS: {str(int(clock.get_fps()))}', (10, 0))
    show_text(f'Delta Time: {str(dt)}', (500, 0))
    show_text(f'Timeer: {str(int(timer))}', (700, 0))

    scroll_text(messages[active_message], (500, 500), 20)
    text1.update()

    pygame.display.flip()


while running:
    # fill the screen with a color to wipe away anything from last frame
    text1 = ScrollText("Check this sick message", 50, (500, 310))
    timer += dt

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
    dt = clock.tick(60) / 1000
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

pygame.quit()
