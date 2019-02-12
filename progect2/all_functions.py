import math
from sympy import *
x = symbols('x')


def main_part():

    def mean():  # - математическое ожидание вычисляемое как среднее
        return sum(rr_intervals)/len(rr_intervals)


    def SDNN():  # SDNN стандартное отклонение NN интервалов
        return sqrt(D())


    def SDANN():  # стандартное отклонение средних значений SDNN
        return SDNN() / sqrt(len(rr_intervals))


    def RMSSD():  # квадратный корень из суммы квадратов разности величин последовательных RR-интервалов
        return sqrt(sum([(rr_intervals[i] - rr_intervals[i-1]) ** 2 for i
                         in range(1, len(rr_intervals))]) / (len(rr_intervals)))


    def RR50():  # количество пар последовательных NN интервалов, различающихся более, чем на 50 миллисекунд,
        # полученное за весь период записи
        k = 0
        for i in range(1, len(rr_intervals)):
            if rr_intervals[i] - rr_intervals[i - 1] > 0.05:
                k += 1
        return k


    def pRR50():  # процент NN50 от общего количества последовательных пар интервалов, различающихся более, чем на
        # 50 миллисекунд, полученное за весь период записи
        return RR50() / (len(rr_intervals) - 1)


    def CV():  # коэффициент вариации. Представляет собой нормированную оценку СКО
        return 100 * SDNN() / mean()


    def D():
        mean_var = mean()
        sum_rr = 0
        for i in rr_intervals:
            sum_rr += (i - mean_var) ** 2
        return sum_rr/(len(rr_intervals) - 1)


    def As():
        answer = 0
        for i in range(1, len(points)):
            answer += integrate(x**3 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                                (x, points[i - 1][0], points[i][0]))
        return answer / (sqrt(D())**3)


    def Ex():
        answer = 0
        for i in range(1, len(points)):
            answer += integrate(x**4 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                                (x, points[i - 1][0], points[i][0]))
        return (answer / D() ** 2) - 3


    def mode2():
        mode = []  # 0 - число интервалов в промежутке, 1 - начение моды
        k = 0
        count = 0
        for i in points:
            if k * 0.05 < (i[0]*1000 - 50) / 1000:
                mode.append([k, count])
                count = 0
                while k * 0.05 < (i[0]*1000 - 50) / 1000:
                    k += 1
                count += i[1]
            else:
                count += i[1]
        mode.append([k, count])
        just_variable = sorted(mode, key=lambda x: x[1], reverse=True)[0]
        try:
            mode = [round(just_variable[1]*1000/length)/10,
                    round(((just_variable[0])*0.05 + 0.05*((just_variable[1] - mode[mode.index(just_variable)-1][1])
                                                           /((just_variable[1] - mode[mode.index(just_variable)-1][1])
                                                             +(just_variable[1] - mode[mode.index(just_variable)+1][1]))))*1000)
                    / 1000]
        except IndexError:
            mode = [round(just_variable[1]*1000/length)/10, round(((just_variable[0])*0.05 + 0.025)*1000) / 1000]
        return mode



    def variation_scale():
        return max(rr_intervals) - min(rr_intervals)


    def tension_index():  # индекс напряжённости Баевского
        return (mode2()[0]) / (2*mode2()[1]*variation_scale())


    def autonomic_balance_index():
        return mode2()[0] / variation_scale()


    def vegetative_rhythm_indicator():
        return 1 / (mode2()[1] * variation_scale())


    def papr():
        return mode2()[0] / mode2()[1]


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
            S0 = fft([n[2*g] for g in range(round(len(n) / 2))], lenght)
            S1 = fft([n[2*g + 1] for g in range(round(len(n) / 2))], lenght)
            answer += [S0[k] + math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
            answer += [S0[k] - math.e ** (-1j * 2 * math.pi * k / lenght) * S1[k] for k in range(round(len(n) / 2))]
            return answer
        else:
            # k  = 0
            return [(n[0] / 1000)]


    def HF(spectrum):
        answer = 0
        for k in range(1, len(spectrum)):
            if 0.4 > k / (len(spectrum) / 10) > 0.15:
                answer += (spectrum[k])**2 / (len(spectrum))
        return answer


    def LF(spectrum):
        answer = 0
        for k in range(1, len(spectrum)):
            if 0.15 > k / (len(spectrum) / 10) > 0.04:
                answer += (spectrum[k])**2 / (len(spectrum))
        return answer


    def VLF(spectrum):
        answer = 0
        for k in range(1, len(spectrum)):
            if 0.04 > k / (len(spectrum) / 10) > 0.003:
                answer += (spectrum[k])**2 / (len(spectrum))
        return answer


    def TP(spectrum):
        return VLF(spectrum) + HF(spectrum) + LF(spectrum)

    by100mc_res = by100mc()
    fft_res = []
    for i in fft(by100mc()[:2048], 2048):
        fft_res.append(abs(i))


    def norm(spectrum):
        return [round(VLF(spectrum)/TP(spectrum)*1000) / 10, round(LF(spectrum)/TP(spectrum)*1000) / 10,
               round(HF(spectrum)/TP(spectrum)*1000) / 10]
    
    
    def RR_histogram():
    # не по ГОСТу в обе стороны
    # Потом разберёмся графическим выведением гистогаммы
    # Ну и кодище-чудовище
    # Сделал путём множественного пробегания по исходному массиву
    def append_in_histogram(i):
        histogram["{:.3f}".format(i)] = [j for j in rr_intervals if i <= j and j < i + 0.05]
        i = float("{:.3f}".format(i + 0.05))
        return i
    histogram = {}
    if min(rr_intervals) < 0.4 and max(rr_intervals) >= 1.3:
        if math.floor(min(rr_intervals) * 10) == round(min(rr_intervals) * 10):
            if round(max(rr_intervals)*10) == math.ceil(max(rr_intervals)*10):
                i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10))
                while i < 1.4:
                    append_in_histogram(i)
            else:
                i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10))
                while i < 1.35:
                    i = append_in_histogram(i)
        else:
            if round(max(rr_intervals)*10) == math.ceil(max(rr_intervals)*10):
                i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10 - 0.05))
                while i < 1.4:
                    i = append_in_histogram(i)
            else:
                i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10 - 0.05))
                while i < 1.35:
                    i = append_in_histogram(i)
    elif min(rr_intervals) < 0.4:
        if math.floor(min(rr_intervals) * 10) == round(min(rr_intervals) * 10):
            i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10))
            while i < 1.3:
                i = append_in_histogram(i)
        else:
            i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10 - 0.05))
            while i < 1.3:
                i = append_in_histogram(i)
    elif max(rr_intervals) > 1.3:
        if round(max(rr_intervals) * 10) == math.ceil(max(rr_intervals) * 10):
            i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10 - 0.05))
            while i < 1.4:
                i = append_in_histogram(i)
        else:
            i = float("{:.3f}".format(round(min(rr_intervals) * 10) / 10 - 0.05))
            while i < 1.35:
                i = append_in_histogram(i)
    else:
        i = 0.4
        while i < 1.3:
            i = append_in_histogram(i)
    return histogram



rr_intervals = [1.514, 0.918, 0.872, 0.829, 0.837, 0.564, 0.568, 0.891, 0.798, 0.864, 1.564, 0.981, 0.895, 0.918, 0.922, 0.903, 0.895, 0.872, 1.51, 0.922, 0.86, 0.833, 0.809, 1.471, 0.887, 0.56, 0.914, 0.872, 0.79, 0.794, 0.798, 0.584, 0.992, 0.821, 1.521, 0.856, 0.56, 0.93, 0.626, 0.887, 0.891, 0.856, 0.809, 0.821, 0.809, 0.541, 0.584, 0.992, 0.949, 0.879, 0.84, 0.84, 0.829, 0.805, 0.84, 0.829, 0.829, 1.525, 0.879, 0.56, 0.911, 0.848, 0.611, 0.949, 0.786, 0.798, 0.782, 0.798, 0.813, 0.829, 0.825, 0.837, 0.837, 0.837, 0.848, 0.844, 0.844, 1.623, 0.883, 0.848, 0.825, 0.829, 0.794, 0.813, 0.813, 0.813, 0.802, 0.798, 0.79, 0.79, 0.774, 0.774, 0.553, 0.553, 0.821, 0.794, 0.782, 0.79, 0.564, 0.603, 0.584, 0.837, 0.58, 0.584, 0.58, 0.588, 0.599, 0.591, 0.595, 0.599, 0.619, 0.634, 0.642, 0.65, 0.654, 0.65, 0.638, 0.63, 0.63, 0.626, 0.619, 0.603, 0.599, 0.588, 0.595, 0.599, 1.035, 0.946, 0.93, 0.953, 0.907, 0.926, 0.918, 1.556, 0.946, 0.864, 0.872, 0.883, 1.479, 0.837, 0.51, 1.004, 0.848, 1.471, 0.864, 0.821, 0.965, 0.969, 0.973, 0.981, 0.984, 1.623, 1.019, 1.603, 1.016, 0.93, 0.537, 1.031, 0.599, 1.23, 0.825, 0.829, 0.84, 0.864, 1.521, 0.922, 0.875, 0.829, 0.825, 1.584, 0.844, 0.868, 0.848, 0.868, 0.879, 0.444, 1.292, 0.879, 0.864, 0.856, 0.837, 0.864, 0.856, 0.837, 0.856, 0.852, 0.848, 0.84, 0.553, 1.082, 0.86, 0.825, 0.833, 0.564, 1.0, 0.848, 0.821, 0.817, 0.813, 0.809, 0.798, 0.821, 0.817, 0.817, 0.821, 0.813, 0.829, 0.833, 0.821, 0.817, 0.821, 0.848, 0.844, 0.576, 1.093, 0.864, 0.833, 0.833, 0.825, 0.821, 0.833, 0.837, 1.56, 0.911, 0.821, 0.829, 0.829, 0.817, 0.829, 0.813, 0.844, 0.84, 0.837, 0.833, 0.833, 0.833, 0.837, 0.84, 1.576, 0.887, 0.837, 0.537, 0.992, 0.899, 0.813, 0.817, 0.817, 0.829, 0.833, 0.833, 0.821, 0.84, 0.848, 0.848, 0.848, 0.844, 0.84, 1.607, 0.86, 0.825, 0.825, 0.556, 0.813, 0.988, 0.848, 0.817, 0.805, 0.809, 0.79, 1.549, 0.852, 0.58, 0.572, 0.852, 0.903, 0.918, 0.887, 0.556, 1.07, 0.829, 1.486, 0.914, 0.829, 0.817, 0.817, 0.825, 0.809, 0.833, 0.844, 0.84, 0.844, 0.852, 0.813, 0.852, 0.626, 1.051, 0.829, 0.825, 0.805, 0.837, 0.825, 0.821, 0.798, 0.821, 0.798, 0.825, 0.825, 0.825, 0.837, 0.837, 0.833, 0.813, 0.84, 0.833, 0.825, 0.549, 1.051, 0.829, 0.56, 0.946, 0.864, 0.556, 0.953, 0.856, 0.805, 0.79, 0.825, 0.817, 0.821, 0.821, 0.809, 0.825, 0.825, 0.833, 0.833, 0.837, 0.833, 0.821, 0.817, 0.813, 0.56, 1.019, 0.821, 0.591, 1.019, 0.833, 0.829, 0.584, 1.016, 0.817, 0.72, 0.891]
points = []
length = len(rr_intervals)
for i in sorted(list(set(rr_intervals))):
    points.append([i, rr_intervals.count(i)])
print(main_part())
