def by100mc():
    def approximate(x, y):
        # Приписывает после координат точек (всех, кроме последней по оси Ox) значения
        # линейных функций (A, B, C: Ax+By+C = 0) между ней и первой точкой (по Ox), встерчающейся справа
        x1, y1 = x
        x2, y2 = y
        return [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]

    def return_y(x, points):  # x - координата по х
        # Возвращение f(x)
        for i in range(len(points[:-1])):
            if points[i + 1][0] > x > points[i][0]:
                return (points[i][2] * x + points[i][4]) / (-points[i][3])
            elif x == points[i][0]:
                return points[i][1]
            elif x == points[i + 1][0]:
                return points[i + 1][1]

    # график rr - интервалов
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

    counting = []
    k = 0
    while k * 100 < result[-1][0]:
        counting.append(round(return_y(k * 100, result)))
        k += 1
    return counting  # отсчёты через 100 мс начиная с 0


def fft(n, lenght):  # Быстрое преобразование Фурье
    # возвращает комплексные числа, для находления "амплитудного спектра", возмите модуль.
    if len(n) >= 2:
        answer = []
        S0 = fft([n[2*i] for i in range(round(len(n) / 2))], lenght / 2)
        S1 = fft([n[2*i + 1] for i in range(round(len(n) / 2))], lenght / 2)
        answer += [S0[k] + math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
        answer += [S0[k] - math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
        return answer
    else:
        # k  = 0
        return [n[0] / 1000]


def HF():
    answer = 0
    for k in range(1, 2048):
        if 0.4 > k * 2 * math.pi / 204.8 > 0.15:
            answer += (fft_res[k])**2 / 204.8
    return answer

def LF():
    answer = 0
    for k in range(1, 2048):
        if 0.15 > k * 2 * math.pi / 204.8 > 0.04:
            answer += (fft_res[k])**2 / 204.8
    return answer

def VLF():
    answer = 0
    for k in range(1, 2048):
        if 0.04 > k * 2 * math.pi / 204.8 > 0.003:
            answer += (fft_res[k])**2 / 204.8
    return answer


by100mc_res = by100mc()
fft_res = []
for i in fft(by100mc()[:2048], 2048):
    fft_res.append(abs(i))



print(HF(), LF(), VLF())
print(LF()/HF())
print((HF()+LF())/VLF())
print(LF()/VLF())


def dff(graph, lenght):
    answer = []
    for j in range(lenght):
        answer.append(0)
        for n in range(lenght):
            answer[-1] += graph[n]*math.e**(-1j * 2 * math.pi * j/ length)
print(dff(by100mc(), len(by100mc)))
