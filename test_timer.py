import pygame
import itertools
pygame.init()
font = pygame.font.SysFont("Arial", 18)
screen = pygame.display.set_mode((450, 600))

timer_font = pygame.font.SysFont("Arial", 18)
timer_sec = 3 # Amount of time that will be count down
timer_text = timer_font.render("00:03", True, (255, 255, 255)) # text that will be used to render

snip = font.render('',1,pygame.Color("coral"))
done = False
counter = 0
speed = 1
offset = -10
current_location = 10

display_string = "Test Text for scrolling text (so much text omg!IJLSKJLAKSJD)"
# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1                                                
pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds


# def text_scroll(the_string):
#     display_string = the_string
#
#
#     if counter < speed * len(display_string):
#         counter +=1
#
#     elif counter >= speed*len(display_string):
#         global done
#         done = True
#     snip = font.render(display_string[0:counter//speed],1, pygame.Color("coral"))
#     # screen.blit(snip,(100,100))
#     return snip


running = True
while running:
    screen.fill((0, 0, 0))

    # if counter < speed * len(display_string):
    #     counter +=1
    #
    #
    # elif counter >= speed*len(display_string):
    #     done = True
    #     snip = font.render(display_string[0], 1, pygame.Color("coral"))

    # for element in range(0, len(display_string)):
    #     # print(display_string[element])
    #     snip = font.render(display_string[element], 1, pygame.Color("coral"))
    #     screen.blit(snip, (100, ))
    char_iter = itertools.islice(display_string, 0, None)

    # for char in char_iter:
    for i in display_string:
        # print(char)
        snip = font.render(i, 1, pygame.Color("coral"))
        current_location +=10
        screen.blit(snip, (100, current_location))
        # current_location += 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == timer:    # checks for timer event
            if timer_sec > 0: 
                timer_sec -= 1 # Decrements the timer so its counting down
                timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 255)) # Renders the timer text
            if timer_sec <= 0:
                timer_sec = 3 # resets timer
                timer_text = timer_font.render("00:%02d" % timer_sec, True, (255, 255, 255))
            # else:
            #     pygame.time.set_timer(timer, 0)    # turns off timer event

# add another "if timer_sec > 0" here if you want the timer to disappear after reaching 0
    screen.blit(timer_text, (300, 20)) # Renders the timer text on the screen
    # screen.blit(text_scroll("Test Text for scrolling effect!"),(300,100))

    pygame.display.update()