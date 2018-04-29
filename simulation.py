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

initial_batman = (0, 0)
initial_alfred = (0, 1)

initial_socks = [(1, 1), (3, 3)]
collected_socks = []

state = State(initial_batman, initial_alfred, field, initial_socks)


# associate moves_knight with batman
# and moves_king with alfred
# at a higher level
# does that imply objects? or just structs?


# Run simulation

moves_king = list(king_moves())
moves_knight = list(knight_moves())
while True:
    print_field(state)

    # unpack state tuple
    # is this clean programming? in a functional style?
    batman = state.batman
    alfred = state.alfred
    socks = state.socks

    # get batman's move
    possible1 = keep_moves_on_board(state, batman, moves_knight)
    random_move = random.choice(list(possible1))

    # get alfred's move
    possible2 = keep_moves_on_board(state, alfred, moves_king)
    possible3 = keep_moves_without_collision(state, possible2)
    best_move = pick_best_move(state, possible2)

    # determine if batman leaves socks behind
    potential_dropped_sock = dropped_sock(state)
    if potential_dropped_sock:
        print('dropped sock')
        socks.append(potential_dropped_sock)

    # detect if alfred picked up socks
    potential_picked_up_sock = picked_up_sock(state)
    if potential_picked_up_sock:
        print('picked up sock')
        collected_socks.append(potential_picked_up_sock)
        socks.remove(potential_picked_up_sock)


    # update state

    # do need to reference these guys as state.batman? if not, why not?
    # we don't, because they're both references to the same object.
    # but then... the object being referenced is changing?
    # yes. just replacing the thing being referenced with a new version.
    # is that how functional programming is done?
    batman = random_move(batman)
    alfred = best_move(alfred)
    state = State(batman, alfred, field, socks)
    

    events = [potential_dropped_sock, potential_picked_up_sock]
    print_spacing(events)

    time.sleep(1)
