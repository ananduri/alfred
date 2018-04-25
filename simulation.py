"""
It is better to have 100 functions that act on 1 data structure
than to thave 10 functions that act on 10 data structures.
"""

import numpy as np
from functools import partial
import random
from collections import namedtuple
import time

State = namedtuple('State', ['alfred', 'field', 'batman'])

size = 10

# could also make this periodic
field = [[True for _ in range(size)] for _ in range(size)]
field = np.array(field)

agent = (0, 0)
agent2 = (0, 1)

state = State(agent, field, agent2)


def get_square_from_move(state, move):
    field = state.field
    agent = state.agent
    c = move(agent)
    if c[0] < 0 or c[1] < 0:
        return False
    elif c[0] >= field.shape[0] or c[1] >= field.shape[1]:
        return False
    else:
        return field[c[0], c[1]]


def king_moves():
    return ((lambda dx, dy: (lambda loc: (loc[0] + dx, loc[1] + dy)))(dx, dy) 
        for dx in [-1, 0, 1] 
        for dy in [-1, 0, 1])

def knight_moves():
    return ((lambda dx, dy: (lambda loc: (loc[0] + dx, loc[1] + dy)))(dx, dy) 
        for dx, dy in 
        [(1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1)])

def test_king_moves():
    loc = (0, 0)
    for x in king_moves():
        print(x(loc))

"""
(filter on-board? moves)
"""
def keep_moves_on_board(agent, field, moves):
    return filter(partial(get_square_from_move, field, agent), moves)


# for now, best move is defined as the one that
# takes you closest to agent2
"""
(highest (map utility moves))
"""
def pick_best_move(agent, field, agent2, moves):
    f = partial(utility, state)
    return max(moves, key=f)

def utility(state, move):
    relative_position = find_diff(state.agent, state.agent2)
    return dot(relative_position, move((0, 0)))

def find_diff(agent1, agent2):
    return (agent1[0] - agent2[0], agent1[1] - agent2[1])

def dot(position1, position2):
    return sum(position1[x] * position2[x] for x in range(len(position1)))



# -----------------------------
# Display functions

def print_field(field, agent):
    for x, row in enumerate(field):
        for y, square in enumerate(row):
            if (x == agent[0] and y == agent[1]):
                print('+', end='')
                continue
            print('#', end='') if square else print(' ', end='')
        print('\n', end='')

# generalize to a function that will print the field and
# a list of objects that we provide
def print_field2(field, agent, agent2):
    for x, row in enumerate(field):
        for y, square in enumerate(row):
            if (x == agent[0] and y == agent[1]):
                print('+', end='')
                continue
            elif (x == agent2[0] and y == agent2[1]):
                print('K', end='')
                continue
            print('#', end='') if square else print(' ', end='')
        print('\n', end='')

def print_empty_field(field):
    for x in field:
        for y in x:
            print('#', end='') if y else print(' ', end='')
        print('\n', end='')


# -----------------------------
# Run simulation

moves_king = list(king_moves())
moves_knight = list(knight_moves())
while True:
    print_field2(field, agent, agent2)
    possible1 = keep_moves_on_board(agent, field, moves_knight)
    random_move = random.choice(list(possible1))

    possible2 = keep_moves_on_board(agent2, field, moves_king)

    best_move = pick_best_move(agent, field, agent2, possible2)

    agent = random_move(agent)
    agent2 = best_move(agent2)
    state = State(agent, field, agent2)
    
    time.sleep(1)
    print('\n')
