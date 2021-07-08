import time

import pygame  # gui
import numpy as np  # array/list
import sys

import pygame.display

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

# start pygame(loop -> keep updating)
running = True

input_Horizontal = "30"
input_Vertical = "30"
user_input_Horizontal = int(input_Horizontal)
user_input_Vertical = int(input_Vertical)

# game of life page
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
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption("Game Of Life")

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game_running = False
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

    screen.fill((158, 205, 250))

    # gui
    for x in range(user_input_Horizontal):
        for y in range(user_input_Vertical):
            pygame.draw.rect(screen, (249, 251, 175), [1 + x * 20, 1 + y * 20 + 80, 20 - 2 * 1, 20 - 2 * 1])
            if cells[x][y] == 1:
                pygame.draw.rect(screen, (240, 162, 249), [1 + x * 20, 1 + y * 20 + 80, 18, 18])

    # GOL rules
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

    new_cells[:] = cells[:]

    pygame.display.update()