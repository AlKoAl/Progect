# чтение последовательностей из двух файлов.
def open_files(x, y):
    with open(x) as x:
        y = ''
        for line in x:
            y += line.strip()
    x.close()
    return y.upper()      # вернул длинную строку
print(' Введите имя первого файла и имя, которое вы для него хотите:')
open_files(input(), input())
print(' Введите имя второго файла и имя, которое вы для него хотите:')
open_files(input(), input())
