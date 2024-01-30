# Example file showing a basic pygame "game loop"
import math as M
import random as R

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
running = True
mouse_click = False
hit = False
font = pygame.font.SysFont("Arial", 18)

next_dialogue = False

next_level = False
targets = 0
increment = 7
points = 0
level = 1
max_amount = 500
timer = 0


class ScrollText:
    counter = 0
    active_text = 0

    def __init__(self, text_, speed_, location_):
        self.text_list = text_
        self.message = text_
        self.t_speed = speed_
        self.location = pygame.Vector2(location_)
        self.counter_rounded = round(ScrollText.counter)
        self.done = False
        # self.active_text = 0
        self.current_msg = self.text_list[self.active_text]

    def update(self):
        if self.counter < len(self.current_msg):
            ScrollText.counter += (dt * self.t_speed)
        elif self.counter >= len(self.current_msg):
            self.done = True

        t_keys = pygame.key.get_pressed()
        if t_keys[pygame.K_RETURN] and self.done and ScrollText.active_text < len(self.text_list) - 1:
            ScrollText.counter = 0
            ScrollText.active_text += 1
            self.current_msg = self.text_list[ScrollText.active_text]
            self.done = False

        snip_ = font.render(self.current_msg[0:self.counter_rounded], True, "white")
        screen.blit(snip_, (self.location.x, self.location.y))

    def single_text(self):
        if self.counter < len(self.message):
            ScrollText.counter += (dt * self.t_speed)

        snip_ = font.render(self.message[0:self.counter_rounded], True, "white")
        screen.blit(snip_, (self.location.x, self.location.y))


# Displaying Text
def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    render_text = font.render(display_text, True, pygame.Color("coral"))
    screen.blit(render_text, (text_location.x, text_location.y))


def target(surface, position, radius, colour, mouse_position, mouse_click):
    t_surface = surface
    t_position = position
    t_radius = radius
    t_colour = colour
    m_pos = mouse_position
    m_click = mouse_click

    # get_radius(t_radius)

    pygame.draw.circle(t_surface, t_colour, t_position, t_radius)

    # This calculates the distance between the mouse and the target 
    a = m_pos[0] - (t_position[0])
    b = m_pos[1] - (t_position[1])
    distance = M.sqrt((a * a) + (b * b))

    # checks if the distance between the mouse and target less than the targets radius 
    if distance <= t_radius:
        if m_click:
            global hit
            hit = True
            global points  # So this can be accessed by other places
            points += 1
            t_position[0] = 1000000  # Makes the target move out of screen


def random_points():
    spawn_point_x = R.randint(60, 1190)
    spawn_point_y = R.randint(60, 630)
    # global spawn_point
    spawn_point = pygame.Vector2(spawn_point_x, spawn_point_y)
    return spawn_point


def check_spawn_points():
    for x in range(len(positions)):
        a = positions[x] - (positions[x - 1])
        b = positions[x] - (positions[x - 1])
        distance = M.sqrt((a * a) + (b * b))
        if distance < 100:
            positions.remove(positions[x])
            random_points()
            positions.insert(x, random_points())


def level_complete_check():
    global hit
    global targets
    if hit:
        hit = False
        targets -= 1

    if targets == 0:
        global next_level  # needs to be accessed by in main loop and
        next_level = True


# Used to create random amounts of targets
# Also random spawn locations
# This always goes before the main loops
def spawn_point_generation(max_amount):
    m_amount = max_amount
    global positions  # needs to be accessed by others functions
    positions = []
    i = 0
    amount_of_targets = R.randint(m_amount - 2, m_amount)
    global targets  # need to be accessed by other functions
    targets = amount_of_targets
    while i < amount_of_targets:
        random_points()
        positions.append(random_points())
        i += 1
        check_spawn_points()


def spawning_targets():
    for x in range(len(positions)):
        target(screen, positions[x], 30, "red", mouse_pos, mouse_click)

class UIBar:
    ratio = 0
    def __init__(self, name, x, y, width, height, timer_, colour, fill_colour, bar_thickness):
        self.name = name
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(width, height)
        self.total_timer = timer_
        self.current_timer = timer
        self.bar_thickness = bar_thickness
        # self.ratio = self.current_timer / self.total_timer
        self.colour = colour
        self.fill_colour = fill_colour
        self.bar_rect = pygame.Rect(self.position.x, self.position.y, self.size.x + self.bar_thickness, self.size.y + self.bar_thickness)
        self.bar_fill_rect = pygame.Rect(self.position.x + self.bar_thickness, self.position.y + self.bar_thickness, (self.size.x * UIBar.ratio) - self.bar_thickness, self.size.y - self.bar_thickness)

    def draw(self):
        UIBar.ratio = self.current_timer / self.total_timer
        if self.current_timer >= self.total_timer:
            self.current_timer = self.total_timer
            UIBar.ratio = 1
        pygame.draw.rect(screen, self.colour, self.bar_rect, self.bar_thickness)
        pygame.draw.rect(screen, self.fill_colour, self.bar_fill_rect)
        show_text(self.name, (self.position.x,self.position.y - 20))

def render():
    screen.fill("black")
    show_text(f'Level: {level}', (640, 0))
    show_text(f'Points: {points}', (1200, 0))
    show_text(f'FPS: {str(int(clock.get_fps()))}', (10, 0))

    spawning_targets()
    level_complete_check()

    # test_text.update()
    test_text1.update()
    test_text2.update()
    test_bar.draw()
    # test_text2.single_text()
    pygame.draw.rect(screen, "red", test_space, 1)
    pygame.display.flip()


def get_inputs():
    for event in pygame.event.get():
        mouse_button = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_button[0]:
                global mouse_click
                mouse_click = True
                print("left mouse clicked")
            if mouse_button[1]:
                print("middle clicked")
            if mouse_button[2]:
                print("Right clicked")
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = False
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                print("Space Pressed")
                global next_level
                next_level = True
            if keys[pygame.K_c]:
                print("C pressed")
        if event.type == pygame.QUIT:
            global running
            running = False


spawn_point_generation(increment)
# Main loop
while running:
    # event_system()
    mouse_pos = pygame.mouse.get_pos()
    # Single text
    # test_text = ScrollText(["Test text"], 50, (10, 200))
    # More than 1 Text
    test_text1 = ScrollText(["MESSAGE", "MESSAGE 2"], 15, (10, 300))
    test_text2 = ScrollText(["MESSAGE", "MESSAGE 2"], 15, (10, 400))

    test_bar = UIBar("UI Bar TEST", 100, 500, 400, 10, 20, "blue", "purple", 2)

    # print(test_text2.counter)
    timer += dt

    # RENDER YOUR GAME HERE
    test_space = pygame.Rect(30, 30, 1220, 660)
    render()

    # This is used for the target spawning
    # Area for the circles to spawn in

    get_inputs()
    # used to respawn the targets for the next level
    if next_level:
        next_level = False
        level += 1
        if level >= 100:
            level = 100
            next_level = False
        spawn_point_generation(increment)
        spawning_targets()
        print(increment)

    # flip() the display to put your work on screen
    # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
