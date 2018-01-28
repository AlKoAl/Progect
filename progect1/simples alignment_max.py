# К величайшему сожалению, это частный случай.
# здесь у меня уже есть две последовательности в виде строк
# вариант с наибольшем, наименьшим:
s1 = 'ATAT'
s2 = 'TATA'   # НИКОГДА НЕ ЗАБЫВАТЬ, ЧТО ПЕРВОЙ КОДИРУЕСТЯ СТРОКА МАТРИЦЫ
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
for i in range(1, (len(s1) + 2)):
    matrix[1][i] = (i - 1) * d
for i in range(1, (len(s2) + 2)):
    matrix[i][1] = (i - 1) * d
for i in range(2, len(s1) + 2):       # Не смотреть на то как я это реализовал, а не то запутаюсь
    for j in range(2, len(s2) + 2):
        if matrix[j][0] == matrix[0][i]:
            s = 1
        else:
            s = -1
        a = [matrix[j-1][i] + d, matrix[j][i - 1] + d, (matrix[j-1][i-1] + s)]
        a.sort()
        matrix[j][i] = a[2]
j = len(s1) + 1
i = len(s2) + 1
s1 = ''
s2 = ''
def comeback (matrix):
    global s1, s2, i, j
    if matrix[i][0] == matrix[0][j]:
        s = 1
    else:
        s = -1
    if i == 0 and j == 0:
        s1 = s1
        s2 = s2
    elif j >= 2 and matrix[i][j] == matrix[i][j - 1] + d:
        s2 = matrix[0][j] + s2
        s1 = '-' + s1
        j -= 1
        comeback(matrix)
    elif i >= 2 and j >= 2 and matrix[i][j] == matrix[i - 1][j - 1] + s:
        s2 = matrix[0][j] + s2
        s1 = matrix[i][0] + s1
        i -= 1
        j -= 1
        comeback(matrix)
    elif i >= 2 and matrix[i][j] == matrix[i - 1][j] + d:
        s2 = '-' + s2
        s1 = matrix[i][0] + s1
        i -= 1
        comeback(matrix)
comeback(matrix)
print(s2, s1)
