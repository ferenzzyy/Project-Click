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

# spawn_timer = 3
# timer = pygame.USEREVENT + 1
# pygame.time.set_timer(timer, 1000)


next_level = False
targets = 0
increment = 7
points = 0
level = 1
max_amount = 500

target_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
target_pos1 = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 4)


# Fucntion for Showing FPS
def update_fps():
    fps = str(int(clock.get_fps()))
    fps_text = font.render("FPS: " + fps, 1, pygame.Color("coral"))
    return fps_text


def show_points():
    # points_ = "Points: " + str(points)
    points_text = font.render(f'Points: {points}', 1, pygame.Color("coral"))
    return points_text


def show_level():
    level_text = font.render(f'Level: {level}', 1, pygame.Color("coral"))
    return level_text

#Texting typing effect for text boxes
def text_scroll(the_string):
    display_string = the_string
    snip = font.render('',1,pygame.Color("coral"))
    counter = 0
    speed = 3
    done = False

    if counter < speed * len(display_string):
        counter +=1

    elif counter >= speed*len(display_string):
        done = True
    snip = font.render(display_string[0:counter//speed],1, pygame.Color("coral"))
    # screen.blit(snip,(100,100))
    return snip
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
                next_level = True
                print("space pressed!")

        # if event.type == timer: # checks for timer event 
        #     if spawn_timer > 0: 
        #         spawn_timer -= 1 # Decrements the timer so its counting down 
        #     if spawn_timer <= 0:
        #         spawning_targets()
        #         spawn_timer = 4 # resets timer
        #     # else:
        #     #     pygame.time.set_timer(timer, 0) #turn off timer event 


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

        # This happens for the first item of the positions list

        # On the 2nd item (that being the positions[1])
        # Take the distance between this position and the position before 
        # If that distance is below 60 
        # Generate another spawn point 
        # Repeat for the new one 

        # if i >= 1:
        #     a = positions[i] - ([i-1])
        #     b = positions[i] - (positions[i-1])
        #     distance = M.sqrt((a*a) + (b*b))

        #     if distance <= 60: # Checks if the distance between centres is smaller or equal to 60 

        i += 1
        check_spawn_points()


def spawing_targets():
    for x in range(len(positions)):
        target(screen, positions[x], 30, "red", mouse_pos, mouse_click)
        # print(positions)


spawn_point_generation(increment)
# Main loop
while running:
    event_system()
    message = ""
    mouse_pos = pygame.mouse.get_pos()
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # spawning_targets()
    # This is used for the target spawning

    test_space = pygame.Rect(30, 30, 1220, 660)
    pygame.draw.rect(screen, "red", test_space, 1)

    spawing_targets()

    level_complete_check()
    # used to respawn the targets for the next level
    if next_level == True:
        level += 1
        if level >= 100:
            level = 100
            # message = "YOU'RE DONE ENOUGH!"
            screen.blit(text_scroll("YOU'RE DONE ENOUGH!"), (100, 100))
            next_level = False
        next_level = False
        # increment += 3
        spawn_point_generation(increment)
        spawing_targets()
        print(increment)

    screen.blit(update_fps(), (10, 0))  # Shows FPS
    screen.blit(show_points(), (1200, 0))  # Shows Points
    screen.blit(show_level(), (640, 0))  # Shows Levels


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
