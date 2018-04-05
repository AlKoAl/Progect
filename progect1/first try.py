def open_files(x):
    with open(x) as x:
        y = ''
        for line in x:
            y += line.strip()
    x.close()
    return y.upper()      # вернул длинную строку


def Needleman_Wunsch_max(s1, s2):
    matrix = [['' for j in range(len(s1) + 2)] for i in range(len(s2) + 2)]  # i - строчки, j - стольбцы [i][j]
    k = 2
    for symbol in s1:
        matrix[0][k] = symbol
        k += 1
    k = 2
    for symbol in s2:
        matrix[k][0] = symbol
        k += 1  # задал строку и столбец с буквами
    print(' Введите штраф за разрыв: ')
    d = int(input())
    print(' Введите штраф за совпадение: ')
    coincidence = int(input())
    print(' Введите штраф за несовпадение: ')
    discrepancy = int(input())
    for j in range(1, (len(s1) + 2)):
        matrix[1][j] = (j - 1) * d  # задал первую строку
    for i in range(1, (len(s2) + 2)):
        matrix[i][1] = (i - 1) * d  # задал первый столбец
    for j in range(2, len(s1) + 2):
        for i in range(2, len(s2) + 2):
            if matrix[i][0] == matrix[0][j]:
                s = coincidence
            else:
                s = discrepancy  # s - штраф за совпадение/несовпадение
            a = [matrix[i - 1][j] + d, matrix[i][j - 1] + d, (matrix[i - 1][j - 1] + s)]
            a.sort()
            matrix[i][j] = a[2]  # Выбрал максимальный счёт
    j = len(s1) + 1
    i = len(s2) + 1
    s1 = ''
    s2 = ''

    def comeback():
        nonlocal s1, s2, i, j
        if matrix[i][0] == matrix[0][j]:
            s = coincidence
        else:
            s = discrepancy  # s - штраф за совпадение/несовпадение
        if i == 1 and j == 1:
            s1 = s1         # я не помню зачем мне это условие, но наверное так надо
            s2 = s2
        elif i >= 2 and matrix[i][j] == matrix[i - 1][j] + d:
            s1 = '-' + s1
            s2 = matrix[i][0] + s2
            i -= 1  # если стрелочка вверх, то я в верхнюю последовательность записываю -
        elif i >= 2 and j >= 2 and matrix[i][j] == matrix[i - 1][j - 1] + s:
            s2 = matrix[i][0] + s2
            s1 = matrix[0][j] + s1
            i -= 1
            j -= 1
        elif j >= 2 and matrix[i][j] == matrix[i][j - 1] + d:
            s1 = matrix[0][j] + s1
            s2 = '-' + s2
            j -= 1

    while i != 1 or j != 1:
        comeback()
    print(' ' + s1, '\n', s2)
    return()


# первая и вторая функции во многом сопадают. Это можно реализовать через ветвление
def Needleman_Wunsch_min(s1, s2):
    matrix = [['' for j in range(len(s1) + 2)] for i in range(len(s2) + 2)]  # i - строчки, j - стольбцы [i][j]
    k = 2
    for symbol in s1:
        matrix[0][k] = symbol
        k += 1
    k = 2
    for symbol in s2:
        matrix[k][0] = symbol
        k += 1  # задал строку и столбец с буквами
    print(' Введите штраф за разрыв: ')
    d = int(input())
    print(' Введите штраф за совпадение: ')
    coincidence = int(input())
    print(' Введите штраф за несовпадение: ')
    discrepancy = int(input())
    for j in range(1, (len(s1) + 2)):
        matrix[1][j] = (j - 1) * d  # задал первую строку
    for i in range(1, (len(s2) + 2)):
        matrix[i][1] = (i - 1) * d  # задал первый столбец
    for j in range(2, len(s1) + 2):
        for i in range(2, len(s2) + 2):
            if matrix[i][0] == matrix[0][j]:
                s = coincidence
            else:
                s = discrepancy  # s - штраф за совпадение/несовпадение
            a = [matrix[i - 1][j] + d, matrix[i][j - 1] + d, (matrix[i - 1][j - 1] + s)]
            a.sort()
            matrix[i][j] = a[2]  # Выбрал максимальный счёт
    j = len(s1) + 1
    i = len(s2) + 1
    s1 = ''
    s2 = ''

    def comeback():
        nonlocal s1, s2, i, j
        if matrix[i][0] == matrix[0][j]:
            s = coincidence
        else:
            s = discrepancy  # s - штраф за совпадение/несовпадение
        if i == 1 and j == 1:
            s1 = s1
            s2 = s2
        elif j >= 2 and matrix[i][j] == matrix[i][j - 1] + d:
            s1 = matrix[0][j] + s1
            s2 = '-' + s2
            j -= 1
        elif i >= 2 and j >= 2 and matrix[i][j] == matrix[i - 1][j - 1] + s:
            s2 = matrix[i][0] + s2
            s1 = matrix[0][j] + s1
            i -= 1
            j -= 1
        elif i >= 2 and matrix[i][j] == matrix[i - 1][j] + d:
            s1 = '-' + s1
            s2 = matrix[i][0] + s2
            i -= 1  # если стрелочка вверх, то я в верхнюю последовательность записываю -

    while i != 1 or j != 1:
        comeback()
    print(' ' + s1, '\n', s2)
    return ()


def Needleman_Wunsch_all(s1, s2):
    print('''Приносим извинения, но, в связи с особенностями языка, 
    может выдавать ошибку при больших последовательностях''')
    matrix = [['' for j in range(len(s1) + 2)] for i in range(len(s2) + 2)]  # i - строчки, j - стольбцы [i][j]
    k = 2
    for symbol in s1:
        matrix[0][k] = symbol
        k += 1
    k = 2
    for symbol in s2:
        matrix[k][0] = symbol  # Задал строку и столбец с буквами
        k += 1
    print(' Введите штраф за разрыв: ')
    d = int(input())
    print(' Введите штраф за совпадение: ')
    coincidence = int(input())
    print(' Введите штраф за несовпадение: ')
    discrepancy = int(input())
    matrix[1][1] = [0]
    for j in range(2, len(s1) + 2):
        matrix[1][j] = [(j - 1) * d, [1, j - 1]]  # Задаём первую строку с ссылками на клетки
    for i in range(2, len(s2) + 2):
        matrix[i][1] = [(i - 1) * d, [i - 1, 1]]  # Задаём первый столбец с ссылками на клетки
    for i in range(2, len(s2) + 2):
        for j in range(2, len(s1) + 2):
            if matrix[i][0] == matrix[0][j]:  # Проверяем на совпадение нулеотиды
                s = coincidence
            else:
                s = discrepancy
            a = [(matrix[i - 1][j])[0] + d, (matrix[i][j - 1])[0] + d, (matrix[i - 1][j - 1])[0] + s]
            a.sort()
            k = a[2]
            if k == (matrix[i - 1][j])[0] + d:
                matrix[i][j] = [k, [i - 1, j]]
            elif k == (matrix[i - 1][j - 1])[0] + s:
                matrix[i][j] = [k, [i - 1, j - 1]]
            else:
                matrix[i][j] = [k, [i, j - 1]]  # задаём ссылку на максимальный элемент
            if a[2] == a[1]:  # если есть ещё один такой же счёт, то задаём вторую ссылку
                if k == (matrix[i][j - 1])[0] + d:
                    (matrix[i][j]).append([i, j - 1])
                else:
                    (matrix[i][j]).append([i - 1, j - 1])
            if a[0] == a[1] == a[2]:  # Соответственно третью
                (matrix[i][j]).append([i - 1, j - 1])

    def take_all(i, j, s1, s2):
        if len(matrix[i][j]) != 1:  # если у элемента матрицы (списка) длина = 1, то есть нет ссылок, то это - [1][1]
            for k in range(1, len(matrix[i][j])):
                if ((matrix[i][j])[k])[0] == i - 1 and ((matrix[i][j])[k])[1] == j - 1:
                    take_all(i - 1, j - 1, matrix[0][j] + s1, matrix[i][0] + s2)
                elif ((matrix[i][j])[k])[0] == i - 1 and ((matrix[i][j])[k])[1] == j:
                    take_all(i - 1, j, '-' + s1, matrix[i][0] + s2)
                else:
                    take_all(i, j - 1, matrix[0][j] + s1, '-' + s2)
        # эта штука сверху запускает рекурсию. Рекурсия запускается в том случае, если у нас есть два варианта,
        # с помощью которых можно было придти в точку (счёт одинаков)
        else:
            print(' ' + s1 + '\n', s2, '\n')

    take_all(len(s2) + 1, len(s1) + 1, '', '')
    return()

def BLOSOM62(s1, s2):
    amino_acid_similarity_matrix = \
        [[' ', 'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L',
          'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X'],
         ['A', 4, -1, -2, -2, 0, -1, -1, 0, -2, -1, -1, -1, -1, -2, -1, 1, 0, -3, -2, 0, -2, -1, 0],
         ['R', -1, 5, 0, -2, -3, 1, 0, -2, 0, -3, -2, 2, -1, -3, -2, -1, -1, -3, -2, -3, -1, 0, -1],
         ['N', -2, 0, 6, 1, -3, 0, 0, 0, 1, -3, -3, 0, -2, -3, -2, 1, 0, -4, -2, -3, 3, 0, -1],
         ['D', -2, -2, 1, 6, -3, 0, 2, -1, -1, -3, -4, -1, -3, -3, -1, 0, -1, -4, -3, -3, 4, 1, -1],
         ['C', 0, -3, -3, -3, 9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
         ['Q', -1, 1, 0, 0, -3, 5, 2, -2, 0, -3, -2, 1, 0, -3, -1, 0, -1, -2, -1, -2, 0, 3, -1],
         ['E', -1, 0, 0, 2, -4, 2, 5, -2, 0, -3, -3, 1, -2, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
         ['G', 0, -2, 0, -1, -3, -2, -2, 6, -2, -4, -4, -2, -3, -3, -2, 0, -2, -2, -3, -3, -1, -2, -1],
         ['H', -2, 0, 1, -1, -3, 0, 0, -2, 8, -3, -3, -1, -2, -1, -2, -1, -2, -2, 2, -3, 0, 0, -1],
         ['I', -1, -3, -3, -3, -1, -3, -3, -4, -3, 4, 2, -3, 1, 0, -3, -2, -1, -3, -1, 3, -3, -3, -1],
         ['L', -1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4, -2, 2, 0, -3, -2, -1, -2, -1, 1, -4, -3, -1],
         ['K', -1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5, -1, -3, -1, 0, -1, -3, -2, -2, 0, 1, -1],
         ['M', -1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5, 0, -2, -1, -1, -1, -1, 1, -3, -1, -1],
         ['F', -2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6, -4, -2, -2, 1, 3, -1, -3, -3, -1],
         ['P', -1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7, -1, -1, -4, -3, -2, -2, -1, -2],
         ['S', 1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4, 1, -3, -2, -2, 0, 0, 0],
         ['T', 0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5, -2, -2, 0, -1, -1, 0],
         ['W', -3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11, 2, -3, -4, -3, -2],
         ['Y', -2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7, -1, -3, -2, -1],
         ['V', 0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4, -3, -2, -1],
         ['B', -2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4, 1, -1],
         ['Z', -1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4, -1],
         ['X', 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, 0, 0, -2, -1, -1, -1, -1, -1]]
    # матрица BLOSOM62
    matrix = [['' for j in range(len(s1) + 2)] for i in range(len(s2) + 2)]  # i - строчки, j - стольбцы [i][j]
    k = 2
    for symbol in s1:
        matrix[0][k] = symbol
        k += 1
    k = 2
    for symbol in s2:
        matrix[k][0] = symbol
        k += 1  # задал строку и столбец с буквами
    print(' Введите штраф за разрыв: ')
    d = int(input())
    for j in range(1, (len(s1) + 2)):
        matrix[1][j] = (j - 1) * d  # задал первую строку
    for i in range(1, (len(s2) + 2)):
        matrix[i][1] = (i - 1) * d  # задал первый столбец
    for j in range(2, len(s1) + 2):
        for i in range(2, len(s2) + 2):
            for k in range(1, 25):
                if matrix[0][j] == amino_acid_similarity_matrix[0][k]:
                    column = k  # нахожу аминокислоту в матрице blosom, которая будет номером столбца
                    break
            for k in range(1, 25):
                if matrix[i][0] == amino_acid_similarity_matrix[0][k]:
                    line = k  # нахожу аминокислоту в матрице blosom, которая будет номером строки
                    break
            s = amino_acid_similarity_matrix[line][column]  # взятие штрафа из матрицы blosom
            a = [matrix[i - 1][j] + d, matrix[i][j - 1] + d, (matrix[i - 1][j - 1] + s)]
            a.sort()
            matrix[i][j] = a[2]  # Выбрал максимальный счёт
    j = len(s1) + 1
    i = len(s2) + 1
    s1 = ''
    s2 = ''

    def comeback():
        nonlocal s1, s2, i, j
        # повтор тех же действий на обратном пути
        for k in range(1, 25):
            if matrix[0][j] == amino_acid_similarity_matrix[0][k]:
                column = k
                break
        for k in range(1, 25):
            if matrix[i][0] == amino_acid_similarity_matrix[0][k]:
                line = k
                break
        s = amino_acid_similarity_matrix[line][column]
        if i == 1 and j == 1:
            s1 = s1
            s2 = s2
        elif i >= 2 and matrix[i][j] == matrix[i - 1][j] + d:
            s1 = '-' + s1
            s2 = matrix[i][0] + s2
            i -= 1  # если стрелочка вверх, то я в верхнюю последовательность записываю -
        elif i >= 2 and j >= 2 and matrix[i][j] == matrix[i - 1][j - 1] + s:
            s2 = matrix[i][0] + s2
            s1 = matrix[0][j] + s1
            i -= 1
            j -= 1
        elif j >= 2 and matrix[i][j] == matrix[i][j - 1] + d:
            s1 = matrix[0][j] + s1
            s2 = '-' + s2
            j -= 1

    while i != 1 and j != 1:
        comeback()
    print(' ' + s1, '\n', s2)


print(' Введите имя первого файла с последовательностью:')
first_slice = open_files(input())
print(' Введите имя второго файла с последовательностью:')
second_slice = open_files(input())
print('Программа переведёт ваши последовательности в верхний регистр')
print('Каким методом вы будете варавнивать? Нидлман-Вунш - n, с помощью BLOSOM 62 - b, сложная математика - m')
choice = input()
if choice == 'n':
    print("Какое из выравниваний вы хотите? максимальное - max, минимальное - min, все возможные - all")
    count = input()
    if count == 'max':
        Needleman_Wunsch_max(first_slice, second_slice)
    elif count == 'min':
        Needleman_Wunsch_min(first_slice, second_slice)
    elif count == 'all':
        Needleman_Wunsch_all(first_slice, second_slice)
    else:
        print("Пользователь ошибся")
elif choice == 'b':
    BLOSOM62(first_slice, second_slice)
elif choice == 'm':
    print('Нескоро будет')
else:
    print("Пользователь ошибся")

