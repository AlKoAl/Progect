"""
Производит интерполяцию исходной последовательности RR-интервалов, и выводит значения графика через каждые
100 миллисекунд.
Интерполяция проводится путём линейных сплайнов, мировые стандарты - кубическая интерполяция, поэтому нужно переделать
"""


def approximate(x, y):
    # Приписывает после координат точек (всех, кроме последней по оси Ox) значения
    # линейных функций (A, B, C: Ax+By+C = 0) между ней и первой точкой (по Ox), встерчающейся справа
    x1, y1 = x
    x2, y2 = y
    return [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]


def return_y(x, points):  # x - координата по х
    # Возвращение f(x)
    for i in range(len(points[:])):
            if points[i+1][0] > x > points[i][0]:
                return (points[i][2]*x + points[i][4]) / (-points[i][3])
            elif x == points[i][0]:
                return (points[i][1])
            elif x == points[i + 1][0]:
               return (points[i + 1][1])


# график rr - интервалов
rr_intervals = [0.965, 0.944, 0.916, 0.98]
print(sum(rr_intervals))
result = []
for i in [int(i * 1000) for i in rr_intervals]:
    if not len(result):
        result.append([0, i])
        continue
    if len(result) == 1:
        result.append([result[0][1], i])
    else:
        result.append([result[-1][0] + result[-1][1], i])

for i in range(len(result[:-1])):
    result[i] += approximate(result[i], result[i + 1])
print(result)

counting = []
k = 0
while k * 100 < result[-1][0]:
    counting.append(return_y(k * 100, result))
    k += 1

print(counting)  # отсчёты через 100 мс начиная с 0
        result.append([result[-1][0] + result[-1][1], i])

for i in range(len(result[:-1])):
    result[i] += approximate(result[i], result[i + 1])
print(result)

counting = []
k = 0
while k * 100 < sum([int(i * 1000) for i in rr_intervals]):
    counting.append((return_y(k * 100, result)))
    k += 1
print(len(counting))  # отсчёты через 100 мс начиная с 0
