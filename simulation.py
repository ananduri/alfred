import numpy as np
import random
from collections import namedtuple
import time
import importlib

from moves import *
from display import *

State = namedtuple('State', ['batman', 'alfred', 'field', 'socks'])

size = 8

# could also make this periodic
field = np.ones([size, size], dtype='bool')

batman = (0, 0)
alfred = (0, 1)

socks = [(1, 1), (3, 3)]

state = State(batman, alfred, field, socks)


# associate moves_knight with batman
# and moves_king with alfred
# at a higher level
# does that imply objects??


# Run simulation

moves_king = list(king_moves())
moves_knight = list(knight_moves())
while True:
    print_field(state)

    # get batman's move
    possible1 = keep_moves_on_board(state, batman, moves_knight)
    random_move = random.choice(list(possible1))

    # get alfred's move
    possible2 = keep_moves_on_board(state, alfred, moves_king)
    possible3 = keep_moves_without_collision(state, alfred, possible2)
    best_move = pick_best_move(state, possible2)

    # determine if batman leaves socks behind
    sock = dropped_sock(state)
    if sock:
        print('dropped sock')
        state.socks.append(sock)

    # detect if alfred picked up socks
    potential_sock = picked_up_sock(state, alfred)
    if potential_sock:
        print('picked up sock')
        state.socks.remove(potential_sock)


    # update state
    batman = random_move(batman)
    alfred = best_move(alfred)
    state = State(batman, alfred, field, socks)
    
    time.sleep(1)
    print('\n')
