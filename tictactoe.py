

# z = str(input('Enter cells: '))
x_list = []
list_1 = []
list_2 = []
list_3 = []
print('---------')
print('| {0} {1} {2} |'.format(' ', ' ', ' '))
print('| {0} {1} {2} |'.format(' ', ' ', ' '))
print('| {0} {1} {2} |'.format(' ', ' ', ' '))
print('---------')
list_1.append(' ')
list_1.append(' ')
list_1.append(' ')

list_2.append(' ')
list_2.append(' ')
list_2.append(' ')

list_3.append(' ')
list_3.append(' ')
list_3.append(' ')

ful_list = []
ful_list.append(list_1)
ful_list.append(list_2)
ful_list.append(list_3)
# print(ful_list)


def input_turn():
    a, b = input('Enter the coordinates :').split()
    return a, b


def X_or_O():
    three_x = False
    three_o = False
    # # count x and o
    x = 0
    o = 0
    for line in ful_list:
        for el in line:
            if el == 'X':
                x += 1
            if el == 'O':
                o += 1

    for line in ful_list:
        if line[0] == line[1] == line[2] == 'X':
            three_x = True
        if line[0] == line[1] == line[2] == 'O':
            three_o = True

    if ful_list[0][0] == ful_list[1][0] == ful_list[2][0] == 'X':
        three_x = True
    elif ful_list[0][1] == ful_list[1][1] == ful_list[2][1] == 'X':
        three_x = True
    elif ful_list[0][2] == ful_list[1][2] == ful_list[2][2] == 'X':
        three_x = True
    elif ful_list[0][0] == ful_list[1][1] == ful_list[2][2] == 'X':
        three_x = True
    elif ful_list[0][2] == ful_list[1][1] == ful_list[2][0] == 'X':
        three_x = True

    if ful_list[0][0] == ful_list[1][0] == ful_list[2][0] == 'O':
        three_o = True
    elif ful_list[0][1] == ful_list[1][1] == ful_list[2][1] == 'O':
        three_o = True
    elif ful_list[0][2] == ful_list[1][2] == ful_list[2][2] == 'O':
        three_o = True
    elif ful_list[0][0] == ful_list[1][1] == ful_list[2][2] == 'O':
        three_o = True
    elif ful_list[0][2] == ful_list[1][1] == ful_list[2][0] == 'O':
        three_o = True


    if three_o and three_x == False:
        print('O wins')
        exit(0)
    elif three_x and three_o == False:
        print('X wins')
        exit(0)
    elif three_o == False and three_x == False and (x + o) == 9:
        print('Draw')
        exit(0)


def make_move_computer():
    hor_line, element = input_turn()
    try:
        hor_line = int(hor_line)
        element = int(element)
    except ValueError:
        print('You should enter numbers!')
        make_move()
        return
    x = hor_line - 1
    y = element - 1
    if 1 > hor_line or hor_line > 3 or 1 > element or element > 3:
        print('Coordinates should be from 1 to 3!')
        make_move()
        return

    elif ful_list[x][y] == 'O' or ful_list[x][y] == 'X':
        print('This cell is occupied! Choose another one!')
        make_move()
        return
    else:
        ful_list[x][y] = 'O'
        print('---------')
        print('| {0} {1} {2} |'.format(ful_list[0][0], ful_list[0][1], ful_list[0][2]))
        print('| {0} {1} {2} |'.format(ful_list[1][0], ful_list[1][1], ful_list[1][2]))
        print('| {0} {1} {2} |'.format(ful_list[2][0], ful_list[2][1], ful_list[2][2]))
        print('---------')
        X_or_O()
        make_move()



def make_move():
    hor_line, element = input_turn()
    try:
        hor_line = int(hor_line)
        element = int(element)
    except ValueError:
        print('You should enter numbers!')
        make_move()
        return
    x = hor_line - 1
    y = element - 1
    if 1 > hor_line or hor_line > 3 or 1 > element or element > 3:
        print('Coordinates should be from 1 to 3!')
        make_move()
        return

    elif ful_list[x][y] == 'O' or ful_list[x][y] == 'X':
        print('This cell is occupied! Choose another one!')
        make_move()
        return
    else:
        ful_list[x][y] = 'X'
        print('---------')
        print('| {0} {1} {2} |'.format(ful_list[0][0], ful_list[0][1], ful_list[0][2]))
        print('| {0} {1} {2} |'.format(ful_list[1][0], ful_list[1][1], ful_list[1][2]))
        print('| {0} {1} {2} |'.format(ful_list[2][0], ful_list[2][1], ful_list[2][2]))
        print('---------')
        X_or_O()
        make_move_computer()


make_move()


#
# list_of_empty = []
#
# # not finished
# for line in ful_list:
#     for el in line:
#         if el == '_':
#             list_of_empty.append(el)
#
# # Impossible
# if three_o == True and three_x == True:
#     print('Impossible')
# elif abs(x - o) > 1:
#     print('Impossible')
# elif three_o:
#     print('O wins')
# elif three_x:
#     print('X wins')
# elif len(list_of_empty) > 0:
#     print('Game not finished')
#
