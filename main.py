# Example file showing a basic pygame "game loop"
import pygame
import math as M
import random as R

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
mouse_click = False
hit = False
font = pygame.font.SysFont("Arial", 18)

next_dialouge = False

next_level = False
targets = 0
increment = 7
points = 0
level = 1
max_amount = 500
timer = 0




# Displaying Text
def show_text(text, location):
    display_text = text
    text_location = pygame.Vector2(location)
    display_text = font.render(text, True, pygame.Color("coral"))
    # return display_text
    screen.blit(display_text, (text_location.x, text_location.y))


# Texting typing effect for text boxes
def scroll_text(text, location, timer, speed):
    display_text = text
    text_location = pygame.Vector2(location)
    counter = 0
    timeing = timer
    counter = M.floor(timeing * speed)

    if counter >= len(display_text):
        counter = 0


    show_text(display_text[0:counter], (text_location.x, text_location.y))


# def dialouge_scroll(dialouge, location, timer ):
#     current_index = 0
#     if next_dialouge == True:
#         current_index += 1
#     current_dialouge = dialouge[current_index]
#     scroll_text(current_dialouge, location, timer, 10)


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


def event_system():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # mouse click is used so its reset every frame

    global mouse_click
    mouse_click = False
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # click is detected once
                mouse_click = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = False
        if event.type == pygame.QUIT:
            global running  # main loop needs to access this
            running = False
        # below is for debugging
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global next_level
                next_level = True  #
                print("space pressed!")
            if event.key == pygame.K_c:
                # global next_dialouge
                # next_dialouge = True
                print("pressed C")



def level_complete_check():
    global hit
    global targets
    if hit == True:
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
    global positions  # needs to be accessed by others funtions
    positions = []
    i = 0
    amount_of_targets = R.randint(m_amount - 2, m_amount)
    global targets  # need to be accessed by other funtions
    targets = amount_of_targets
    while i < amount_of_targets:
        random_points()
        positions.append(random_points())
        i += 1
        check_spawn_points()


def spawing_targets():
    for x in range(len(positions)):
        target(screen, positions[x], 30, "red", mouse_pos, mouse_click)


spawn_point_generation(increment)
# Main loop
while running:
    # limits FPS to 60
    dt = clock.tick(60) / 1000
    timer += dt
    event_system()
    mouse_pos = pygame.mouse.get_pos()
    screen.fill("black")

    # dialouge = ["Message 1 woaaaaaaaaaaaah", "Message 2 nuh uh", "OH BROTHER THIS GUY STINK", "WUDAHEEEEEEEEEAAAAAL"]

    # RENDER YOUR GAME HERE

    # This is used for the target spawning
    show_text(f'Level: {level}', (640, 0))
    show_text(f'Points: {points}', (1200, 0))
    show_text(f'FPS: {str(int(clock.get_fps()))}', (10, 0))
    # scroll_text("YOU'RE DONE ENOUGH! SENDING MESSAGE THE LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOONG WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY", (100, 100), timer, 20) # Test for scrolling text
    # dialouge_scroll(dialouge, (100,100), timer)
    scroll_text("HELlO :33333333333", (100, 100), timer, 10)

    test_space = pygame.Rect(30, 30, 1220, 660)
    pygame.draw.rect(screen, "red", test_space, 1)

    spawing_targets()

    level_complete_check()
    # used to respawn the targets for the next level
    if next_level == True:
        level += 1
        if level >= 100:
            level = 100
            scroll_text("YOU'RE DONE ENOUGH!", (100, 100), timer, 20)
            next_level = False
        next_level = False
        spawn_point_generation(increment)
        spawing_targets()
        print(increment)

    # flip() the display to put your work on screen
    pygame.display.flip()
