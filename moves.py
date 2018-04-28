"""
It is better to have 100 functions that act on 1 data structure
than to thave 10 functions that act on 10 data structures.
"""

from functools import partial

def get_square_from_move(state, agent, move):
    field = state.field
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
def keep_moves_on_board(state, agent, moves):
    return filter(partial(get_square_from_move, state, agent), moves)


# for now, best move is defined as the one that
# takes you closest to agent2
"""
(highest-elem (map utility moves))
"""
def pick_best_move(state, moves):
    f = partial(utility, state)
    return max(moves, key=f)

def utility(state, move):
    relative_position = find_diff(state.batman, state.alfred)
    return dot(relative_position, move((0, 0)))

def find_diff(agent1, agent2):
    return (agent1[0] - agent2[0], agent1[1] - agent2[1])

def dot(position1, position2):
    return sum(position1[x] * position2[x] for x in range(len(position1)))
