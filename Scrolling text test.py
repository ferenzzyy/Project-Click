import pygame
import time

# --- constants ---  # PEP8: `UPPER_CASE_NAMES`; directly after import

FPS = 30

# --- main ---

pygame.init()
screen = pygame.display.set_mode((960, 720))  # , pygame.FULLSCREEN, vsync=1)
screen_rect = screen.get_rect()

font = pygame.font.SysFont(None, 50)

description = "Welcom to freedy fazbears pizzaria uhh har har har har har har har har har haaaar har har har haaaar haaar"

desc_text = font.render(description, True, (255, 255, 255))
desc_rect = desc_text.get_rect(left=screen_rect.right)
# desc_rect.x = 100

clock = pygame.time.Clock()
running = True
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False

        # --- updates (without draws) ---
        # desc_rect.x == 100
        desc_rect.x -= 5
        if desc_rect.right <= 0:  # if leave on left side
            desc_rect.x = screen_rect.right  # then move to right side

        # --- draws (without updates) ---

        screen.fill((0, 0, 125))

        screen.blit(desc_text, desc_rect)

        pygame.display.update()

        clock.tick(FPS)  # slowdown to 30 FPS
    except KeyboardInterrupt:
        print("Quitting...")
        running = False

pygame.quit()