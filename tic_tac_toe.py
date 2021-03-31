initial = ' ' * 9


def return_grid(initial):
    counter = 0
    res = []
    for i in range(3):
        res.append([])
        for j in range(3):
            res[i].append(initial[counter])
            counter += 1
    return res


def print_grid(grid):
    print('---------')
    for ls in grid:
        print('|', ' '.join(ls), '|')
    print('---------')


def print_initial_grid(grid):
    counter = 0
    res = []
    for i in range(3):
        res.append([])
        for j in range(3):
            res[i].append(grid[counter])
            counter += 1
    print('---------')
    for ls in res:
        print('|', ' '.join(ls), '|')
    print('---------')


def horizontal_winner(grid, string):
    another_string = 'X'
    if string == 'X':
        another_string = 'O'
    res = None
    for i in grid:
        if " " not in i and another_string not in i:
            res = True
            break
        else:
            res = False
    return res


def vertical_winner(grid, string):
    res = []
    winner = False
    postion = 0
    if string == 'X':
        for i in range(len(grid)):
            for ls in grid:
                res.append(ls[postion])
            if " " not in res and 'O' not in res:
                winner = True
                break
            else:
                postion += 1
                res = []
                continue
    else:
        for i in range(len(grid)):
            for ls in grid:
                res.append(ls[postion])
            if " " not in res and 'X' not in res:
                winner = True
                break
            else:
                postion += 1
                res = []
                winner = False
                continue

    return winner


def line_winner(grid, string):
    if grid[0][0] == string and grid[1][1] == string and grid[2][2] == string:
        return True
    elif grid[0][2] == string and grid[1][1] == string and grid[2][0] == string:
        return True
    else:
        return False


def is_empty_sels(grid, empty=' '):
    res = []
    for ls in grid:
        res.extend(ls)
    if empty in res:
        return True
    else:
        return False


def count_inputs(grid, string):
    res = 0
    for ls in grid:
        for el in ls:
            if el == string:
                res += 1
    return res


def is_winner(grid, string):
    if horizontal_winner(grid, string) or vertical_winner(grid, string) or line_winner(grid, string):
        return True
    else:
        return False


def count_diff(grid, x='X', o='O'):
    return abs(count_inputs(grid, 'X') - count_inputs(grid, 'O'))


def result(grid, user_char):
    print(is_winner(grid, 'O'))
    print(is_winner(grid, 'X'))
    print(is_empty_sels(grid))
    if is_winner(grid, 'X') and is_winner(grid, 'O'):  # or count_diff(grid) > 1:
        print('Impossible')
    elif is_winner(grid, 'X'):
        print('X wins')
        return True
    elif is_winner(grid, 'O'):
        print('O wins')
        return True
    elif (is_winner(grid, 'X') or is_winner(grid, 'O')) and is_empty_sels(grid):
        print("Game not finished")
    elif not (is_empty_sels(grid)):
        print("Draw")
        return True
    else:
        return False


def check_for_chars(input):
    ts = [i for i in input.replace(' ', '')]
    for i in ts:
        while i.isalpha():
            return False
    return ts, True


def check_wor_big_numbers(input):
    ts = [i for i in input.replace(' ', '')]
    for i in ts:
        while int(i) > 3:
            return False
    return ts, True


def is_occupied(grid, ts, firsr_input):
    second_input = None
    if firsr_input == 'X':
        second_input = 'O'
    else:
        firsr_input = 'O'
        second_input = 'X'

    first = int(ts[0]) - 1
    second = int(ts[1]) - 1
    emp = grid[first][second] == ' '
    if grid[first][second] != firsr_input and grid[first][second] == second_input:
        return True
    else:
        return False


def replace_in_grid(grid, ts, first_input):
    first = int(ts[0]) - 1
    second = int(ts[1]) - 1
    res = []
    grid[first][second] = first_input
    res = grid
    test = res
    print_grid(res)
    return test


def input_checks(user_input, ts, grid, first_input):
    ts = [i for i in user_input.replace(' ', '')]
    res = False
    while not (res):
        if not check_for_chars(user_input):
            print('You should enter numbers!')
            user_input = input('Enter the coordinates: ')
            ts = [i for i in user_input.replace(' ', '')]
            res = False
            continue
        elif not check_wor_big_numbers(user_input):
            print('Coordinates should be from 1 to 3!')
            user_input = input('Enter the coordinates: ')
            ts = [i for i in user_input.replace(' ', '')]
            res = False
            continue
        elif is_occupied(grid, ts, first_input):
            print('This cell is occupied! Choose another one!')
            user_input = input('Enter the coordinates: ')
            ts = [i for i in user_input.replace(' ', '')]
            res = False
            continue
        else:
            res = True
    return res, ts


def run():
    print_initial_grid(initial)
    grid = return_grid(initial)
    counter = 0
    first_input = 'X'
    check = None
    while not check:
        if counter % 2 == 0:
            first_input = 'X'
        else:
            first_input = 'O'
        user_test = input('Enter the coordinates: ')
        input_as_list = [i for i in user_test.replace(' ', '')]
        ts = input_checks(user_test, input_as_list, grid, first_input)[1]
        new_grid = replace_in_grid(grid, ts, first_input)
        check = result(new_grid, first_input)
        grid = new_grid
        counter += 1


run()
