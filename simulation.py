import numpy as np
import random
from collections import namedtuple
import time
import importlib

from moves import *
from display import *

State = namedtuple('State', ['batman', 'alfred', 'field', 'socks'])

size = 10

# could also make this periodic
field = np.ones([size, size], dtype='bool')

batman = (0, 0)
alfred = (0, 1)

socks = [(4, 4), (3, 3)]

state = State(batman, alfred, field, socks)


# associate moves_knight with batman
# and moves_king with alfred
# at a higher level


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
    best_move = pick_best_move(state, possible2)

    # update state
    batman = random_move(batman)
    alfred = best_move(alfred)
    state = State(batman, alfred, field, socks)
    
    time.sleep(1)
    print('\n')


