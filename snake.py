from random import randint
import os


def move_snake(coords, direction):
    row = None
    n = 0
    for coord in coords:
        if row != None:
            if coord[0] > row:
                direction = 'UP'
            elif coord[0] < row:
                direction = 'DOWN'
            elif coord[1] > col:
                direction = 'LEFT'
            else:
                direction = 'RIGHT'
        row = coord[0]
        col = coord[1]
        if direction == 'UP':
            coords[n] = (row - 1, col)
        elif direction == 'DOWN':
            coords[n] = (row + 1, col)
        elif direction == 'LEFT':
            coords[n] = (row, col - 1)
        else:
            coords[n] = (row, col + 1)
        n += 1

    return coords, (row, col), direction


def check_collisions(coords, food, bonus_food, n):
    alive = True
    bonus_eaten = False
    row = coords[0][0]
    col = coords[0][1]
    if row == food[0] and col == food[1]:
        food_eaten = True
    else:
        food_eaten = False
    if bonus_food != None:
        if row == bonus_food[0] and col == bonus_food[1]:
            bonus_eaten = True
    if row < 0 or col < 0 or row >= n or col >= n:
        alive = False
    if alive == True and food_eaten == False:
        for i in range(1, len(coords)):
            if row == coords[i][0] and col == coords[i][1]:
                alive = False

    return food_eaten, alive, bonus_eaten


def new_food(coords, n):
    while True:
        overlap = False
        row = randint(0, n - 1)
        col = randint(0, n - 1)
        for coord in coords:
            if row == coord[0] and col == coord[1]:
                overlap = True
                break
        if overlap == False:
            break

    return (row, col)


def grow_snake(coords, direction):
    coord = coords[len(coords) - 1]
    if direction == 'UP':
        coords.extend([(coord[0] + 1, coord[1])])
    elif direction == 'DOWN':
        coords.extend([(coord[0] - 1, coord[1])])
    elif direction == 'LEFT':
        coords.extend([(coord[0], coord[1] + 1)])
    else:
        coords.extend([(coord[0], coord[1] - 1)])

    return coords


def save_score(name, score):
    pos = 0
    path = 'score_table.txt'
    if os.path.exists(path):
        file = open(path, 'r')
        score_list = []
        for row in file:
            info = row.partition('-')
            saved_score = int(info[2].partition('\n')[0])
            score_list.extend([(info[0], saved_score)])
        new_list = []
        for item in score_list:
            new_list.extend([(name, score)])
            break
        for item in score_list:
            new_list.extend([item])
        file.close()
        file = open(path, 'w')
        print(new_list)
        for item in new_list:
            file.write(item[0] + '-' + str(item[1]) + '\n')
    else:
        file = open(path, 'w')
        file.write(name + '-' + str(score) + '\n')
        file.close()
