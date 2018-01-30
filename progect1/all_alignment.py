# здесь у меня уже есть две последовательности в виде строк
# вариант со всеми:
s1 = 'AGC'
s2 = 'AAAC'
matrix = [['' for j in range(len(s1) + 2)] for i in range(len(s2) + 2)]  # i - строчки, j - стольбцы [i][j]
k = 2
for symbol in s1:
    matrix[0][k] = symbol
    k += 1
k = 2
for symbol in s2:
    matrix[k][0] = symbol
    k += 1
print(' Введите штраф за разрыв: ')
d = int(input())
print(' Введите штраф за совпадение: ')
coincidence = int(input())
print(' Введите штраф за несовпаление: ')
discrepancy = int(input())
matrix[1][1] = [0]
for i in range(2, len(s1) + 2):
    matrix[1][i] = [(i-1)*d, [1, i-1]]
for i in range(2, len(s2) + 2):
    matrix[i][1] = [(i-1)*d, [i-1, 1]]
for i in range(2, len(s2) + 2):
    for j in range(2, len(s1) + 2):
        if matrix[i][0] == matrix[0][j]:
            s = coincidence
        else:
            s = discrepancy
        a = [(matrix[i-1][j])[0] + d, (matrix[i][j-1])[0] + d, (matrix[i-1][j-1])[0] + s]
        a.sort()
        k = a[2]
        if k == (matrix[i-1][j])[0] + d:
            matrix[i][j] = [k, [i-1, j]]
        elif k == (matrix[i-1][j-1])[0] + s:
            matrix[i][j] = [k, [i-1, j-1]]
        else:
            matrix[i][j] = [k, [i, j-1]]
        if a[2] == a[1]:
            if k == (matrix[i][j-1])[0] + d:
                (matrix[i][j]).append([i, j-1])
            else:
                (matrix[i][j]).append([i-1, j-1])
        if a[0] == a[1] == a[2]:
            (matrix[i][j]).append([i-1, j-1])
i = len(s2)+1
j = len(s1)+1
s1 = ''
s2 = ''
def take_all(i, j, s1, s2):
    if len(matrix[i][j]) != 1:
        for k in range(1, len(matrix[i][j])):
            if ((matrix[i][j])[k])[0] == i - 1 and ((matrix[i][j])[k])[1] == j - 1:
                take_all(i - 1, j - 1, matrix[0][j] + s1, matrix[i][0] + s2)
            elif ((matrix[i][j])[k])[0] == i - 1 and ((matrix[i][j])[k])[1] == j:
                take_all(i - 1, j, '-' + s1, matrix[i][0] + s2)
            else:
                take_all(i, j, matrix[0][j] + s1, '-' + s2)
    else:
        print(' ' + s1 + '\n', s2, '\n')
take_all(i, j, s1, s2)
