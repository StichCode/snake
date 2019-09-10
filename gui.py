# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:33:16 2019
@author: jj
"""

import os
from snake import *
import pygame as py
from random import randint

screen_height = 500
screen_width = int(screen_height * 1.2)
line_width = int(screen_height / 500)
if line_width != 1 and line_width % 2 != 0:
    line_width += 1
screen_height += line_width

box_x = int(screen_width / 11)
box_y = int(screen_height / 9)

bg_color = (110, 120, 255)
bx_color = (0, 0, 0)
ln_color = (200, 180, 210)
tx_color = (0, 0, 0)
sk_color = (200, 200, 50)
sk_outline = (200, 100, 20)
food_color = (0, 255, 100)
food_outline = (200, 50, 0)

n = 20
size = round((screen_height - line_width / 2) / n)
grid = []
for i in range(n):
    grid.append([])
    for j in range(n):
        x = j * size + round(line_width / 2) - (1 - (line_width % 2))
        w = x + size
        y = i * size + round(line_width / 2) - (1 - (line_width % 2))
        h = y + size
        grid[i].extend([(x, y, w, h)])

box1 = (int(screen_height * 1.05), int(screen_height / 5),
        int(screen_height * 0.1), int(screen_height * 0.05))
box2 = (int(screen_height * 1.05), int((screen_height / 5) * 1.5),
        int(screen_height * 0.1), int(screen_height * 0.05))

font_size_1 = int(box1[2] * 0.4)
font_size_2 = int(font_size_1 * 0.7)
font_size_3 = int(font_size_1 * 3)


def draw_grid():
    for row in range(n):
        start = grid[row][0][0:2]
        finish = grid[row][n - 1][2], grid[row][n - 1][1]
        py.draw.line(screen_surf, ln_color, start, finish, line_width)
    start = grid[row][0][0], grid[row][0][3]
    finish = grid[row][n - 1][2:4]
    py.draw.line(screen_surf, ln_color, start, finish, line_width)
    for col in range(n):
        start = grid[0][col][0], grid[0][col][1] - int(line_width / 2)
        finish = grid[n - 1][col][0], grid[n - 1][col][3] + int(line_width / 2)
        py.draw.line(screen_surf, ln_color, start, finish, line_width)
    start = grid[0][col][2], grid[0][col][1] - int(line_width / 2)
    finish = grid[n - 1][col][2], grid[n - 1][col][3] + int(line_width / 2)
    py.draw.line(screen_surf, ln_color, start, finish, line_width)


def update_grid(coord, color, outline):
    x = grid[coord[0]][coord[1]][0]
    y = grid[coord[0]][coord[1]][1]
    w = grid[coord[0]][coord[1]][2]
    h = grid[coord[0]][coord[1]][3]
    py.draw.rect(screen_surf, color, (x, y, w + 1 - x, h + 1 - y))
    start = (x + 1 - int(line_width / 2), y)
    finish = (w + int(line_width / 2), y)
    py.draw.line(screen_surf, outline, start, finish, line_width)
    start = (x, y)
    finish = (x, h)
    py.draw.line(screen_surf, outline, start, finish, line_width)
    start = (w, y)
    finish = (w, h)
    py.draw.line(screen_surf, outline, start, finish, line_width)
    start = (x + 1 - int(line_width / 2), h)
    finish = (w + int(line_width / 2), h)
    py.draw.line(screen_surf, outline, start, finish, line_width)


def draw_box(text, box):
    py.draw.rect(screen_surf, ln_color, box)
    py.draw.rect(screen_surf, bx_color, box, line_width)
    text_surf, text_rect = text_objects(text, font_size_1)
    text_rect.center = (box[0] + int(box[2] * 0.5), box[1] + int(box[3] * 0.55))
    screen_surf.blit(text_surf, text_rect)


def box_label(text, box):
    text_surf, text_rect = text_objects(text, font_size_2)
    text_rect.center = (box[0] + int(box[2] * 0.48), box[1] - int(box[3] * 0.35))
    screen_surf.blit(text_surf, text_rect)


def draw_snake(coords):
    for coord in coords:
        update_grid(coord, sk_color, sk_outline)


def draw_food(coord, color, outline):
    update_grid(coord, color, outline)


def draw_save_screen():
    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              'Enter']
    box_coords = []
    rect1 = (int(box_x * 1.9), int(box_y * 1.3), int(box_x * 7.2), int(box_y * 6.2))
    py.draw.rect(screen_surf, bx_color, rect1)
    rect2 = (int(box_x * 2), int(box_y * 1.4), int(box_x * 7), int(box_y * 6))
    py.draw.rect(screen_surf, ln_color, rect2)
    py.draw.rect(screen_surf, bg_color, (rect2[0], rect2[1], box_x * 7, box_y * 2))
    l = 0
    for i in range(4):
        for j in range(7):
            if i == 3 and j == 5:
                rect = (rect2[0] + box_x * j, rect2[1] + box_y * (i + 2), box_x * 2, box_y)
                py.draw.rect(screen_surf, bg_color, rect, line_width)
                text_surf, text_rect = text_objects(labels[l], font_size_1)
                text_rect.center = rect[0] + int(rect[2] / 2), rect[1] + int(rect[3] / 2)
                screen_surf.blit(text_surf, text_rect)
                box_coords.extend([rect])
            elif i == 3 and j == 6:
                pass
            else:
                rect = (rect2[0] + (box_x * j), rect2[1] + (box_y * 2) + (box_y * i), box_x, box_y)
                py.draw.rect(screen_surf, bg_color, rect, line_width)
                text_surf, text_rect = text_objects(labels[l], font_size_1)
                text_rect.center = rect[0] + int(rect[2] / 2), rect[1] + int(rect[3] / 2)
                screen_surf.blit(text_surf, text_rect)
                box_coords.extend([rect])
                l += 1

    return box_coords, labels


def display_name(text, font_size):
    text_surf, text_rect = text_objects(text, font_size)
    text_rect.left = int(box_x * 2.5)
    text_rect.bottom = int(box_y * 3.2)
    screen_surf.blit(text_surf, text_rect)


def display_high_scores():
    rect1 = (int(box_x * 1.9), int(box_y * 1.3), int(box_x * 7.2), int(box_y * 6.2))
    py.draw.rect(screen_surf, bx_color, rect1)
    rect2 = (int(box_x * 2), int(box_y * 1.4), int(box_x * 7), int(box_y * 6))
    py.draw.rect(screen_surf, ln_color, rect2)
    text_surf, text_rect = text_objects('HIGH SCORES', font_size_2)
    text_rect.center = (int(screen_width / 2), int((screen_height / 4) - (screen_height / 20)))
    screen_surf.blit(text_surf, text_rect)
    score_table = open('score_table.txt', 'r')
    for i, item in enumerate(score_table):
        if i == 0:
            suffix = 'st'
        elif i == 1:
            suffix = 'nd'
        elif i == 2:
            suffix = 'rd'
        else:
            suffix = 'th'
        info = item.partition('-')
        name = info[0]
        score = int(info[2].partition('\n')[0])
        text_surf, text_rect = text_objects(str(i + 1) + suffix, font_size_2)
        text_rect.left = int(screen_width / 2.5)
        text_rect.bottom = int((screen_height / 4) + ((screen_height / 20) * (i + 1)))
        screen_surf.blit(text_surf, text_rect)
        text_surf, text_rect = text_objects(' -      ' + name + ': ' + str(score), font_size_2)
        text_rect.left = int(screen_width / 2.1)
        text_rect.bottom = int((screen_height / 4) + ((screen_height / 20) * (i + 1)))
        screen_surf.blit(text_surf, text_rect)


def key_selector(pos):
    if key == (int(box_x * 7), int(box_y * 6.4)):
        w = box_x * 2
    else:
        w = box_x
    py.draw.rect(screen_surf, sk_outline, (pos[0], pos[1], w, box_y), line_width * 3)


def text_objects(text, font_size):
    font = py.font.Font('freesansbold.ttf', font_size)
    text_surf = font.render(text, True, tx_color)

    return text_surf, text_surf.get_rect()


py.init()

screen = py.display
screen_surf = screen.set_mode((screen_width, screen_height))
clock = py.time.Clock()
fps = 50

high_score = False
save = False
new_game = True
reset = True

while True:
    if save == True:
        if save_screen == True:
            if enter == True:
                for i, label in enumerate(labels):
                    if key[0] == box_coords[i][0]:
                        if key[1] == box_coords[i][1]:
                            if label != 'Enter':
                                if len(name) < 3:
                                    name += label
                            else:
                                save_score(name, score)
                                saved = True
                                save_screen = False
                                break
                enter = False
            if back_space == True:
                name = name[:len(name) - 1]
                back_space = False
            if key_selector_move == 'RIGHT':
                if key[1] < int(box_y * 6.4):
                    if key[0] < int(box_x * 8):
                        key = key[0] + box_x, key[1]
                else:
                    if key[0] < int(box_x * 6):
                        key = key[0] + box_x, key[1]
                    else:
                        key = int(box_x * 7), int(box_y * 6.4)
            elif key_selector_move == 'LEFT':
                if key[0] > int(box_x * 2):
                    key = key[0] - box_x, key[1]
            elif key_selector_move == 'UP':
                if key[1] > int(box_y * 3.4):
                    key = key[0], key[1] - box_y
            elif key_selector_move == 'DOWN':
                if key[0] < int(box_x * 7):
                    if key[1] < int(box_y * 6.4):
                        key = key[0], key[1] + box_y
                else:
                    if key[1] < int(box_y * 5.4):
                        key = key[0], key[1] + box_y
                    else:
                        key = int(box_x * 7), int(box_y * 6.4)
            key_selector_move = None
            box_coords, labels = draw_save_screen()
            key_selector(key)
            display_name(name, font_size_3)
            screen.update()
        else:
            if saved == True:
                high_score = True
                save = False
            else:
                key = (box_x * 2, int(box_y * 3.4))
                key_selector_move = None
                save_screen = True

    elif high_score == True:
        display_high_scores()
        screen.update()
        if enter == True:
            high_score = False
            new_game = True
            reset = True
            enter = False
    else:
        if reset == True:
            if new_game == False:
                if score > 0:
                    path = 'score_table.txt'
                    if os.path.exists(path):
                        file = open(path, 'r')
                        index = None
                        for i, item in enumerate(file):
                            index = i
                            if i == 0:
                                break
                        info = item.partition('-')
                        saved_score = int(info[2].partition('\n')[0])
                        if score > saved_score:
                            save = True
                        else:
                            new_game = True
                            continue
                    else:
                        save = True
                    enter = False
                    reset = False
                else:
                    new_game = True
                    continue
            else:
                mouse_click = False
                game_start = False
                alive = True
                direction = 'UP'
                next_direction = None
                direction_changed = False
                counter = 0
                count = 15.45
                score = 0
                bonus = False
                bonus_food = None
                bonus_points = 0
                save = False
                saved = False
                save_screen = False
                enter = False
                back_space = False
                name = ''
                screen_surf.fill(bg_color)
                draw_grid()
                draw_box('0', box1)
                box_label('Score', box1)
                p = round(n / 2)
                snake_coords = [(p, p), (p + 1, p), (p + 2, p), (p + 3, p)]
                food = new_food(snake_coords, n)
                draw_snake(snake_coords)
                screen.update()
                reset = False

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
                quit()
            if event.key == py.K_RIGHT:
                if save_screen == True:
                    key_selector_move = 'RIGHT'
                else:
                    if direction != 'LEFT':
                        if direction_changed == True:
                            next_direction = 'RIGHT'
                        else:
                            direction = 'RIGHT'
                            direction_changed = True
            if event.key == py.K_LEFT:
                if save_screen == True:
                    key_selector_move = 'LEFT'
                else:
                    if direction != 'RIGHT':
                        if direction_changed == True:
                            next_direction = 'LEFT'
                        else:
                            direction = 'LEFT'
                            direction_changed = True
            if event.key == py.K_UP:
                game_start = True
                if save_screen == True:
                    key_selector_move = 'UP'
                else:
                    if direction != 'DOWN':
                        if direction_changed == True:
                            next_direction = 'UP'
                        else:
                            direction = 'UP'
                            direction_changed = True
            if event.key == py.K_DOWN:
                if save_screen == True:
                    key_selector_move = 'DOWN'
                else:
                    if direction != 'UP':
                        if direction_changed == True:
                            next_direction = 'DOWN'
                        else:
                            direction = 'DOWN'
                            direction_changed = True
            if event.key == py.K_RETURN:
                enter = True
            if event.key == py.K_BACKSPACE:
                back_space = True

    if game_start == True:
        new_game = False
        if bonus == True:
            if bonus_points == 0:
                bonus = False
                update_grid(bonus_food, bg_color, ln_color)
            else:
                bonus_points = round(bonus_points - 0.015, 2)
        if counter == int(count):
            if alive == True:

                snake_coords, grid_update, tail_direction = move_snake(snake_coords, direction)
                food_eaten, alive, bonus_eaten = check_collisions(snake_coords, food, bonus_food, n)
                if food_eaten == True:
                    snake_coords = grow_snake(snake_coords, tail_direction)
                    score += 1
                    if count > 5:
                        count -= 0.075
                    draw_box(str(score), box1)
                    food = new_food(snake_coords, n)
                    if bonus == False:
                        rand = randint(0, 9)
                        if rand == 0:
                            bonus_food = new_food(snake_coords, n)
                            bonus = True
                            bonus_points = randint(5, 10)
                if bonus_eaten == True:
                    bonus_food = None
                    bonus = False
                    score += int(bonus_points) + 1
                    bonus_points = 0
                    draw_box(str(score), box1)
                if alive == True:
                    if bonus == True:
                        draw_food(bonus_food, food_outline, food_color)
                    draw_food(food, food_color, food_outline)
                    update_grid(grid_update, bg_color, ln_color)
                    draw_snake(snake_coords)
                if next_direction != None:
                    direction = next_direction
                    next_direction = None
                direction_changed = False

            else:
                reset = True
                game_start = False
            screen.update()
            counter = 0
        else:
            counter += 1

    clock.tick(fps)
