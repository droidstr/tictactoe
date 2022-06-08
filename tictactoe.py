#tictactoe

def print_field(field):
    print('\n-------\n')
    print ('  0 1 2')
    i = 0
    for row_ in field:
        print(str(i)+' '+' '.join(row_))
        i += 1
    print('\n-------\n')


def get_user_turn(field):
    while True:
        turn_input = input('Введите строку и столбец через пробел ')
        if turn_input.lower() == 'ничья':
            return 3, 3
        turn_input = turn_input.split()
        try:
            if any(
                    [len(turn_input) != 2,
                     turn_input[0] not in ['0', '1', '2'],
                     turn_input[1] not in ['0', '1', '2']]
            ):
                print('введите два числа от 0 до 2')
                continue
        except:
            print('введите два числа от 0 до 2')
            continue
        row_, column_ = map(int, turn_input)
        if field[row_][column_] == '-':
            return row_, column_
        print('Эта клетка занята')


def check_win(field, row, column, turn):
    if all([field[i][column] == turn for i in range(3)]) \
            or all([field[row][i] == turn for i in range(3)]):
        return True
    elif (row == 1 or column == 1) and row != column:
        return False
    else:
        return all([field[i][i] == turn for i in range(3)]) \
               or all([field[2-i][i] == turn for i in range(3)])


def check_tie(field):
    return all(['-' not in row_ for row_ in field])


def main():
    while True: # основной цикл
        print ('Если захотите начать заново, введите "ничья"')
        field = [['-' for i in range(3)] for i in range(3)]
        turn = ''
        while True: # ход
            print_field(field)
            turn = 'O' if turn == 'X' else 'X'
            print (f'ход {turn}\n')
            row, column = get_user_turn(field)
            try:
                field[row][column] = turn
            except:
                print('Ничья\n')
                break
            if check_win(field, row, column, turn):
                print_field(field)
                print (f'{turn} выиграл\n')
                break
            if check_tie(field):
                print_field(field)
                print ('Ничья\n')
                break
        if input('Сыграть ещë раз? Введите "да" ').lower() != 'да':
            print()
            break
        print()
    print ('\nигра окончена')


if __name__ == '__main__':
    main()