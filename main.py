import pygame, random

pygame.init()
#game constants
white = (255, 255, 255)
black = (0, 0, 0)
grey = (120, 120, 120)

WIDTH = 400
HEIGHT = 500
player = pygame.transform.scale(pygame.image.load("head.png"), (90, 70))
background = "white"
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
dt = 0
# create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('From The Depths')

#game variables
player_x = 170
player_y = 350

platform = []
running = True
y_change = 0
draw_platforms_boolean = True
platform_y = 0
show_starting_platform = True
starting_platform_y = 490
starting_platform_rect = 170, starting_platform_y, 70, 10

playing = False
show_title_screen = True
game_over = False

# movement
velocity_LR = 15
velocity_y_jump = 10
jump = False
spawn_platform = 10

def platform_randomizer():
    global platform, platform_y
    for i in range(7):
        platform_y = random.randrange(0, HEIGHT)
        platform.append([])
        platform[i].append(random.randrange(0, WIDTH))
        random.randrange(0, HEIGHT)
        platform[i].append(platform_y)
        platform[i].extend((70, 10)) # will have to be a variable
    print(platform)
    return platform

def update_player(y_pos):
    global y_change, jump
    gravity = .4
    jump_height = 10
    if jump:
        y_change = -jump_height
        jump = False
    y_change += gravity
    y_pos += y_change
    return y_pos

def check_collision(rect_list):
    global player_x, player_y, y_change
    jump = False
    for i in range(len(rect_list)):
        if (rect_list[i].colliderect([player_x, player_y, 70, 60]) and y_change > 0) or starting_platform_draw.colliderect([player_x, player_y, 70, 60]) and y_change > 0:
            jump = True
    return jump
def update_platforms(my_list, y_pos, change):
    global starting_platform_y
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
            starting_platform_y -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10]
def check_if_game_over(y_pos, screen_height):
    global game_over
    if y_pos > screen_height:
        game_over = True
    else:
        pass
    return game_over
def reset():
    global player_x, player_y, platform, running, y_change, draw_platforms_boolean, platform_y, show_starting_platform, starting_platform_rect
    player_x = 170
    player_y = 350

    platform = []
    running = True
    y_change = 0
    draw_platforms_boolean = True
    platform_y = 0
    show_starting_platform = True
    starting_platform_y = 490
    starting_platform_rect = 170, starting_platform_y, 70, 10



title_text = font.render("FROM THE DEPTHS", True, black)
starting_text = font.render("Press Space To Begin", True, black)
game_over_text = font.render("GAME OVER", True, black)
return_title_text = font.render("Press 't' to return to main menu", True, black)

title_text_rect = title_text.get_rect()
starting_text_rect = starting_text.get_rect()
game_over_text_rect = game_over_text.get_rect()
return_title_text_rect = return_title_text.get_rect()

game_over_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
title_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 100)
starting_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)
return_title_text_rect.center = (WIDTH // 2, HEIGHT // 2 - 50)
# check collision with blocks
# def check_collision(rect_list, j):
#     global player_x
#     global player_y
#     global y_change
#     for i in range(len(rect_list)):
#         if rect_list[i].colliderect([player_x, player_y + 60, 90, 10]) and jump == False and y_change > 0:
#             jump = True
#     return j

# update player y position
# def update_player(y_pos):
#     global jump_boolean
#     global y_change
#     jump_height = 10
#     gravity = .4
#     if jump_boolean:
#         y_change -= jump_height
#         jump_boolean = False
#     y_pos += y_change
#     y_change += gravity
#     return y_pos
while running == True:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []
    keys = pygame.key.get_pressed()
    # adds to list one time
    if playing == False and game_over == False:
        screen.blit(title_text, title_text_rect)
        screen.blit(starting_text, starting_text_rect)
    if keys[pygame.K_SPACE]:
        playing = True
    if playing and not game_over:
        if spawn_platform >= 10:
            platform = platform_randomizer()
            spawn_platform -= 10

        # draws platforms
        for i in range(len(platform)):
            block = pygame.draw.rect(screen, black, platform[i])
            blocks.append(block)
        # draws initial platform
        if show_starting_platform:
            starting_platform_draw = pygame.draw.rect(screen, black,(170, starting_platform_y , 70, 10))
        # moves within bounds of screen

        if keys[pygame.K_LEFT] and (player_x > -20):
            player_x -= velocity_LR
        if keys[pygame.K_RIGHT] and (player_x < WIDTH - 70):
            player_x += velocity_LR

        if check_if_game_over(player_y, HEIGHT):
            playing = False

        # if keys[pygame.K_SPACE]:
        #     jump = True
        #     falling = False



        jump = check_collision(blocks)

        player_y = update_player(player_y)

        update_platforms(platform, player_y, y_change)



    if game_over:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(return_title_text, return_title_text_rect)
        if keys[pygame.K_t]:
            game_over = False
            playing = False
            player_y = 350
            player_x = 170
            starting_platform_y = 490







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()