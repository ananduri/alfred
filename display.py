

# Display functions

# def print_field(field, agent):
#     for x, row in enumerate(field):
#         for y, square in enumerate(row):
#             if (x == agent[0] and y == agent[1]):
#                 print('+', end='')
#                 continue
#             print('#', end='') if square else print(' ', end='')
#         print('\n', end='')


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


def print_field(state):
    socks = state.socks
    field = state.field
    batman = state.batman
    alfred = state.alfred

    for x, row in enumerate(field):
        for y, square in enumerate(row):
            if (x == batman[0] and y == batman[1]):
                print('B', end='')
                continue
            elif (x == alfred[0] and y == alfred[1]):
                print('A', end='')
                continue
            elif len(list(filter(lambda p: (x == p[0]) and (y == p[1]), socks))) > 0:
                print('.', end='')
                continue
            print('#', end='') if square else print(' ', end='')
        print('\n', end='')

def print_empty_field(field):
    for x in field:
        for y in x:
            print('#', end='') if y else print(' ', end='')
        print('\n', end='')
