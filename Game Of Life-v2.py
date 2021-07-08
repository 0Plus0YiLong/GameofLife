import pygame  # gui
import numpy as np  # array/list


# initialise pygame
pygame.init()

# count neighbours function
def is_neighbours(x, y):
    neighs = 0
    if x > 0 and y > 0 and cells[x - 1][y - 1] == 1:
        neighs += 1
    if y > 0 and cells[x][y - 1] == 1:
        neighs += 1
    if y > 0 and x < user_input_Horizontal - 1 and cells[x + 1][y - 1] == 1:
        neighs += 1
    if x > 0 and cells[x - 1][y] == 1:
        neighs += 1
    if x < user_input_Horizontal - 1 and cells[x + 1][y] == 1:
        neighs += 1
    if y < user_input_Vertical - 1 and x > 0 and cells[x - 1][y + 1] == 1:
        neighs += 1
    if y < user_input_Vertical - 1 and cells[x][y + 1] == 1:
        neighs += 1
    if y < user_input_Vertical - 1 and x < user_input_Horizontal - 1 and cells[x + 1][y + 1] == 1:
        neighs += 1
    return neighs


def in_box_x():
    for i in range(user_input_Horizontal):
        for j in range(user_input_Vertical):
            if mouseX >= 1 + i * 20 and mouseX < 1 + i * 20 + 20 - 2 * 1 and mouseY >= 1 + j * 20 + 80 and mouseY < 1 + j * 20 + 20 + 80 - 2 * 1:
                return i
    return -1


def in_box_y():
    for i in range(user_input_Horizontal):
        for j in range(user_input_Vertical):
            if mouseX >= 1 + i * 20 and mouseX < 1 + i * 20 + 20 - 2 * 1 and mouseY >= 1 + j * 20 + 80 and mouseY < 1 + j * 20 + 20 + 80 - 2 * 1:
                return j
    return -1


# initialise variables
pause = True
option = False
textfield_active_1 = False
textfield_active_2 = False
user_text_1 = ''
user_text_2 = ''

color_active = (255, 255, 255)
color_passive = (153, 153, 153)
display_color_1 = color_passive
display_color_2 = color_passive

# start pygame(loop -> keep updating)
running = False
main_page_running = True
rule_page_running = False

input_Horizontal = "30"
input_Vertical = "30"
user_input_Horizontal = int(input_Horizontal)
user_input_Vertical = int(input_Vertical)

while main_page_running:
    main_screen = pygame.display.set_mode((720, 400))
    pygame.display.set_caption("Settings")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_page_running = False

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    main_screen.fill((255, 255, 255))
    if mouseX > 235 and mouseX < 485 and mouseY > 100 and mouseY < 150:
        pygame.draw.rect(main_screen, (153, 153, 153), [235, 100, 250, 50])
    else:
        pygame.draw.rect(main_screen, (255, 255, 255), [235, 100, 250, 50])
    if mouseX > 235 and mouseX < 485 and mouseY > 250 and mouseY < 300:
        pygame.draw.rect(main_screen, (153, 153, 153), [235, 250, 250, 50])
    else:
        pygame.draw.rect(main_screen, (255, 255, 255), [235, 250, 250, 50])
    if mouseX > 235 and mouseX < 485 and mouseY > 175 and mouseY < 225:
        pygame.draw.rect(main_screen, (153, 153, 153), [235, 175, 250, 50])
    else:
        pygame.draw.rect(main_screen, (255, 255, 255), [235, 175, 250, 50])

    option_font = pygame.font.SysFont(None, 60)

    title_img = pygame.image.load("IMG/Capture.png")
    title_img_resize = pygame.transform.scale(title_img, (240, 60))
    main_screen.blit(title_img_resize, (240, 10))

    option_img = option_font.render("SETTINGS", True, (0, 0, 0))
    main_screen.blit(option_img, (255, 105))
    generate_img = option_font.render("GENERATE", True, (0, 0, 0))
    main_screen.blit(generate_img, (245, 258))
    rules_img = option_font.render("RULES", True, (0, 0, 0))
    main_screen.blit(rules_img, (285, 182))

    main_event = pygame.event.poll()
    if main_event.type == pygame.QUIT:
        main_page_running = False
    elif main_event.type == pygame.MOUSEBUTTONDOWN and main_event.button == 1:
        if not option:
            if mouseX > 235 and mouseX < 485 and mouseY > 250 and mouseY < 300:
                running = True
                main_page_running = False
            elif mouseX > 235 and mouseX < 485 and mouseY > 175 and mouseY < 225:
                rule_page_running = True
                main_page_running = False

    if option == True:
        if textfield_active_1:
            display_color_1 = color_active
        else:
            display_color_1 = color_passive
        if textfield_active_2:
            display_color_2 = color_active
        else:
            display_color_2 = color_passive
        main_screen.fill((255, 255, 0))
        pygame.draw.rect(main_screen, display_color_1, [280, 100, 250, 50])
        pygame.draw.rect(main_screen, display_color_2, [280, 250, 250, 50])
        pygame.draw.rect(main_screen, (255, 255, 255), [0, 0, 130, 40])
        arrow_font = pygame.font.SysFont(None, 60)
        arrow_img = arrow_font.render("BACK", True, (0, 0, 0))
        main_screen.blit(arrow_img, (0, 0))
        if main_event.type == pygame.MOUSEBUTTONDOWN and main_event.button == 1:
            if mouseX > 0 and mouseY > 0 and mouseX < 130 and mouseY < 40:
                option = False
        width_font = pygame.font.SysFont(None, 60)
        width_img = width_font.render("WIDTH", True, (0, 0, 0))
        main_screen.blit(width_img, (100, 108))
        length_font = pygame.font.SysFont(None, 60)
        length_img = length_font.render("LENGTH", True, (0, 0, 0))
        main_screen.blit(length_img, (100, 258))

        # txt field
        if main_event.type == pygame.MOUSEBUTTONDOWN and main_event.button == 1:
            if mouseX > 280 and mouseX < 530 and mouseY > 100 and mouseY < 150:
                textfield_active_1 = True
            else:
                textfield_active_1 = False
            if mouseX > 280 and mouseX < 530 and mouseY > 250 and mouseY < 300:
                textfield_active_2 = True
            else:
                textfield_active_2 = False

        if textfield_active_1:
            if main_event.type == pygame.KEYDOWN:
                if main_event.type == pygame.K_BACKSPACE:
                    user_text_1 = user_text_1[:-1]
                else:
                    user_text_1 += main_event.unicode
        if textfield_active_2:
            if main_event.type == pygame.KEYDOWN:
                if main_event.type == pygame.K_BACKSPACE:
                    user_text_2 = user_text_2[:-1]
                else:
                    user_text_2 += main_event.unicode
        user_input_font = pygame.font.Font(None, 60)
        user_input_img_1 = user_input_font.render(user_text_1, True, (0, 0, 0))
        main_screen.blit(user_input_img_1, (285, 105))
        user_input_img_2 = user_input_font.render(user_text_2, True, (0, 0, 0))
        main_screen.blit(user_input_img_2, (285, 255))

        input_Horizontal = user_text_1
        input_Vertical = user_text_2
        # validation
        if input_Horizontal.isdigit():
            pygame.draw.rect(main_screen, (255, 255, 0), [150, 150, 400, 100])
            user_input_Horizontal = int(input_Horizontal)
        else:
            valid_img_h = user_input_font.render("Please input an integer!", True, (0, 0, 0))
            main_screen.blit(valid_img_h, (235, 150))
        if input_Vertical.isdigit():
            pygame.draw.rect(main_screen, (255, 255, 0), [150, 300, 400, 100])
            user_input_Vertical = int(input_Vertical)
        else:
            valid_img_v = user_input_font.render("Please input an integer!", True, (0, 0, 0))
            main_screen.blit(valid_img_v, (235, 300))

    if main_event.type == pygame.MOUSEBUTTONDOWN and main_event.button == 1:
        if mouseX > 235 and mouseX < 485 and mouseY > 100 and mouseY < 150:
            option = True

    pygame.display.update()

while rule_page_running:
    rule_screen = pygame.display.set_mode((720, 400))
    pygame.display.set_caption("Rules")
    rule_screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_page_running = True
            rule_page_running = False
    rules_font = pygame.font.SysFont(None, 30)


    rule1 = rules_font.render("These rules, which compare the behavior of the automaton to real life, can be condensed into the following:", True, (0, 0, 0))
    rule_screen.blit(rule1, (10, 10))
    rule2 = rules_font.render("Any live cell with two or three live neighbours survives.", True, (0, 0, 0))
    rule_screen.blit(rule2, (10, 10))
    rule3 = rules_font.render("Any dead cell with three live neighbours becomes a live cell.", True, (0, 0, 0))
    rule_screen.blit(rule3, (10, 10))
    rule4 = rules_font.render("All other live cells die in the next generation. Similarly, all other dead cells stay dead.", True, (0, 0, 0))
    rule_screen.blit(rule4, (10, 10))

cells = np.zeros((user_input_Horizontal, user_input_Vertical))
neighbours = np.zeros((user_input_Horizontal, user_input_Vertical))
new_cells = np.zeros((user_input_Horizontal, user_input_Vertical))

for x in range(user_input_Horizontal):
    for y in range(user_input_Vertical):
        cells[x][y] = 0
        neighbours[x][y] = 0

screen_x = user_input_Horizontal * 20 + 2
screen_y = user_input_Vertical * 20 + 2 + 80

while running:
    # setup window
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Game Of Life")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get mouse position in the screen
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    # initialize screen
    screen.fill((158, 205, 250))


    # set up grid area gui
    for x in range(user_input_Horizontal):
        for y in range(user_input_Vertical):
            pygame.draw.rect(screen, (249, 251, 175), [1 + x * 20, 1 + y * 20 + 80, 20 - 2 * 1, 20 - 2 * 1])
            if cells[x][y] == 1:
                pygame.draw.rect(screen, (240, 162, 249), [1 + x * 20, 1 + y * 20 + 80, 18, 18])

    # calculation base on the rules of GOL
    if not pause:
        for x in range(user_input_Horizontal):
            for y in range(user_input_Vertical):
                neighbours[x][y] = is_neighbours(x, y)
                if cells[x][y] == 1:
                    if int(neighbours[x][y]) < 2 or int(neighbours[x][y]) > 3:
                        new_cells[x][y] = 0
                if cells[x][y] == 0:
                    if int(neighbours[x][y]) == 3:
                        new_cells[x][y] = 1
        cells[:] = new_cells[:]

    # draw pause button
    pygame.draw.rect(screen, (153, 153, 153), [5, 10, 280, 60])
    pause_font = pygame.font.SysFont(None, 60)

    if pause:
        pause_start_img = pause_font.render("START", True, (255, 255, 255))
        screen.blit(pause_start_img, (75, 22))
    elif not pause:
        pause_stop_img = pause_font.render("STOP", True, (255, 255, 255))
        screen.blit(pause_stop_img, (75, 22))

    # mouselistener
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if in_box_x() != -1 and in_box_y() != -1:
            if cells[in_box_x()][in_box_y()] == 0:
                cells[in_box_x()][in_box_y()] = 1
            elif cells[in_box_x()][in_box_y()] == 1:
                cells[in_box_x()][in_box_y()] = 0

        if 5 < mouseX < 285 and 10 < mouseY < 70:
            if pause:
                pause = False
            elif not pause:
                pause = True

    new_cells[:] = cells[:]

    pygame.display.update()