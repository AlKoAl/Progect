'''Раскидать по разным группам
Функции с заданным массивом
мода не дописана
Странные показатели эксцесса и асимметрии'''
#  Нашёл математическое ожидание
from sympy import *
x = symbols('x')
rr_intervals = [0.814, 0.811, 0.789, 0.792, 0.789, 0.817, 0.653, 0.994, 0.844, 0.811, 0.789, 0.772, 0.839, 0.856, 0.822, 0.828, 0.822, 0.794, 0.797, 0.792, 0.822, 0.869, 0.822, 0.786, 0.792, 0.775, 0.786, 0.811, 0.817, 0.828, 0.844, 0.806, 0.775, 0.8, 0.789, 0.858, 0.842, 0.825, 0.803, 0.836, 0.792, 0.789, 0.819, 0.844, 0.881, 0.822, 0.778, 0.803, 0.811, 0.797, 0.836, 0.831, 0.825, 0.811, 0.789, 0.781, 0.808, 0.842, 0.833, 0.831, 0.806, 0.778, 0.797, 0.781, 0.792, 0.856, 0.847, 0.822, 0.783, 0.786, 0.786, 0.817, 0.811, 0.85, 0.833, 0.811, 0.783, 0.772, 0.786, 0.803, 0.842, 0.825, 0.811, 0.778, 0.8, 0.789, 0.8, 0.817, 0.858, 0.831, 0.786, 0.783, 0.792, 0.831, 0.825, 0.831, 0.831, 0.822, 0.797, 0.778, 0.794, 0.814, 0.858, 0.847, 0.811, 0.794, 0.786, 0.797, 0.811, 0.825, 0.847, 0.853, 0.808, 0.767, 0.8, 0.803, 0.817, 0.836, 0.819, 0.828, 0.797, 0.781, 0.778, 0.814, 0.822, 0.864, 0.831, 0.789, 0.786, 0.803, 0.792, 0.819, 0.831, 0.839, 0.819, 0.772, 0.753, 0.794, 0.819, 0.814, 0.836, 0.822, 0.783, 0.744, 0.831, 0.781, 0.831, 0.864, 0.822, 0.803, 0.778, 0.786, 0.8, 0.797, 0.814, 0.847, 0.825, 0.775, 0.761, 0.781, 0.772, 0.825, 0.828, 0.797, 0.786, 0.789, 0.778, 0.761, 0.786, 0.819, 0.847, 0.808, 0.769, 0.778, 0.792, 0.786, 0.797, 0.819, 0.819, 0.806, 0.772, 0.775, 0.772, 0.806, 0.811, 0.822, 0.8, 0.769, 0.778, 0.775, 0.783, 0.786, 0.831, 0.819, 0.783, 0.753, 0.772, 0.783, 0.792, 0.811, 0.828, 0.828, 0.803, 0.769, 0.769, 0.8, 0.819, 0.836, 0.839, 0.8, 0.794, 0.803, 0.786, 0.789, 0.833, 0.847, 0.839, 0.789, 0.758, 0.797, 0.806, 0.814, 0.819, 0.828, 0.806, 0.794, 0.778, 0.769, 0.825, 0.522, 0.939, 0.844, 0.817, 0.775, 0.819, 0.811, 0.811, 0.847, 0.867, 0.814, 0.769, 0.789, 0.794, 0.828, 0.831, 0.831, 0.85, 0.814, 0.775, 0.794, 0.819, 0.842, 0.861, 0.833, 0.792, 0.797, 0.789, 0.608, 0.961, 0.833, 0.839, 0.831, 0.783, 0.75, 0.803, 0.811, 0.825, 0.808, 0.825, 0.8, 0.792, 0.767, 0.794, 0.842, 0.839, 0.831, 0.814, 0.792, 0.789, 0.797, 0.808, 0.833, 0.847, 0.836, 0.808, 0.783, 0.786, 0.839, 0.858, 0.844, 0.839, 0.836, 0.814, 0.769, 0.806, 0.836, 0.853, 0.839, 0.831, 0.792, 0.8, 0.803, 0.808, 0.828, 0.844, 0.836, 0.794, 0.783, 0.792, 0.828, 0.844, 0.819, 0.847, 0.808, 0.778, 0.792, 0.811, 0.819, 0.864, 0.839, 0.8, 0.806, 0.772, 0.814, 0.828, 0.842, 0.839, 0.856, 0.797, 0.772, 0.775, 0.822, 0.844, 0.828, 0.822, 0.811, 0.811, 0.778, 0.781, 0.819, 0.828, 0.547, 0.975, 0.8, 0.772, 0.792, 0.806, 0.806, 0.811, 0.8, 0.814, 0.783, 0.769, 0.781, 0.825, 0.828, 0.819, 0.825, 0.789, 0.792, 0.8, 0.803, 0.833, 0.856, 0.831, 0.794, 0.783, 0.769, 0.817, 0.825, 0.819, 0.825, 0.836, 0.786, 0.758, 0.797, 0.794, 0.844, 0.828, 0.831, 0.806, 0.781, 0.778, 0.794, 0.828, 0.825, 0.847, 0.806, 0.781, 0.781, 0.8, 0.811, 0.794, 0.8, 0.789, 0.778, 0.742, 0.744, 0.747, 0.792, 0.792, 0.792, 0.761, 0.781, 0.756, 0.772, 0.775, 0.789, 0.844, 0.844, 0.817, 0.783, 0.794, 0.831, 0.833, 0.872, 0.861, 0.844, 0.792, 0.781, 0.806, 0.806, 0.833, 0.861, 0.844, 0.756, 0.792, 0.794, 0.744, 0.792, 0.819, 0.814, 0.772, 0.769, 0.758, 0.75, 0.775, 0.8, 0.806, 0.803, 0.536, 0.939, 0.764, 0.722, 0.756, 0.803, 0.775, 0.719, 0.725, 0.694, 0.694, 0.708, 0.703, 0.717, 0.742, 0.753, 0.719, 0.689, 0.706, 0.692, 0.717, 0.756, 0.753, 0.733, 0.739, 0.761, 0.703, 0.703, 0.725, 0.767, 0.781, 0.803, 0.778, 0.747, 0.753, 0.775, 0.778, 0.775, 0.822, 0.817, 0.806, 0.767, 0.767, 0.775, 0.806, 0.814, 0.825, 0.783, 0.753, 0.753, 0.725, 0.719, 0.733, 0.756, 0.744, 0.731, 0.708, 0.694, 0.697, 0.719, 0.725, 0.753, 0.764, 0.775, 0.75, 0.739, 0.708, 0.744, 0.764, 0.811, 0.767, 0.769, 0.764, 0.742, 0.742, 0.733, 0.761, 0.775, 0.8, 0.789, 0.778, 0.728, 0.758, 0.756, 0.761, 0.758, 0.792, 0.814, 0.761, 0.731, 0.758, 0.753, 0.794, 0.819, 0.783, 0.772, 0.753, 0.769, 0.753, 0.744, 0.783, 0.825, 0.769, 0.742, 0.731, 0.703, 0.717, 0.728, 0.728, 0.736, 0.736, 0.758, 0.711, 0.669, 0.678, 0.697, 0.706, 0.719, 0.731, 0.719, 0.686, 0.689, 0.694, 0.692, 0.681, 0.736, 0.753, 0.758, 0.736, 0.728, 0.717, 0.747, 0.742, 0.75, 0.786, 0.775, 0.75, 0.722, 0.708, 0.703, 0.714, 0.767, 0.747, 0.747, 0.753, 0.75, 0.722, 0.75, 0.753, 0.775, 0.814, 0.833, 0.806, 0.764, 0.778, 0.772, 0.817, 0.817, 0.622, 0.986, 0.825, 0.781, 0.747, 0.772, 0.783, 0.819, 0.808, 0.789, 0.772, 0.772, 0.747, 0.764, 0.794, 0.794, 0.833, 0.792, 0.747, 0.744, 0.783, 0.753, 0.769, 0.758, 0.764, 0.761, 0.728, 0.714, 0.728, 0.731, 0.767, 0.753, 0.761, 0.736, 0.708, 0.725, 0.728, 0.719, 0.756, 0.797, 0.8, 0.758, 0.747, 0.753, 0.756, 0.792, 0.817, 0.842, 0.814, 0.806, 0.8, 0.789, 0.778, 0.825, 0.883, 0.858, 0.808, 0.803, 0.8, 0.794, 0.794, 0.819, 0.853, 0.839, 0.783, 0.778, 0.797, 0.817, 0.847, 0.831, 0.836, 0.808, 0.811, 0.786, 0.775, 0.842, 0.844, 0.817, 0.797, 0.789, 0.769, 0.778, 0.808, 0.797, 0.814, 0.817, 0.8, 0.75, 0.764, 0.769, 0.806, 0.811, 0.797, 0.792, 0.783, 0.753, 0.736, 0.761, 0.778, 0.797, 0.789, 0.772, 0.739, 0.764, 0.742, 0.758, 0.778, 0.775, 0.772, 0.761, 0.725, 0.725, 0.756, 0.764, 0.783, 0.794, 0.794, 0.758, 0.778, 0.772, 0.764, 0.778, 0.844, 0.836, 0.772, 0.775, 0.756, 0.775, 0.769, 0.794, 0.808, 0.842, 0.778, 0.758, 0.753, 0.761, 0.772, 0.811, 0.808, 0.806, 0.786, 0.772, 0.764, 0.767, 0.775, 0.806, 0.825, 0.769, 0.761, 0.764, 0.781, 0.744, 0.778, 0.8, 0.797, 0.789, 0.758, 0.742, 0.764, 0.786, 0.797, 0.808, 0.806, 0.775, 0.778, 0.772, 0.775, 0.769, 0.828, 0.817, 0.797, 0.747, 0.761, 0.786, 0.789, 0.792, 0.814, 0.833, 0.794, 0.764, 0.764, 0.769, 0.769, 0.817, 0.808, 0.792, 0.767, 0.778, 0.767, 0.733, 0.781, 0.814, 0.817, 0.778, 0.769, 0.753, 0.781, 0.756, 0.769, 0.806, 0.781, 0.786, 0.764, 0.758, 0.731, 0.772, 0.811, 0.794, 0.783, 0.789, 0.767, 0.772, 0.753, 0.767, 0.825, 0.831, 0.781, 0.764, 0.769, 0.747, 0.758, 0.789, 0.792, 0.797, 0.797, 0.767, 0.733, 0.747, 0.764, 0.806, 0.828, 0.781, 0.778, 0.783, 0.761, 0.731, 0.772, 0.806, 0.8, 0.797, 0.758, 0.742, 0.761, 0.758, 0.767, 0.789, 0.775, 0.75, 0.764, 0.744, 0.711, 0.703, 0.75, 0.742, 0.719, 0.719, 0.719, 0.686, 0.703, 0.711, 0.708, 0.736, 0.786, 0.75, 0.744, 0.708, 0.728, 0.747, 0.767, 0.761, 0.797, 0.819, 0.8, 0.739, 0.744, 0.758, 0.764, 0.786, 0.794, 0.811, 0.778, 0.764, 0.758, 0.783, 0.792, 0.792, 0.833, 0.839, 0.781, 0.747, 0.789, 0.808, 0.831, 0.789, 0.808, 0.825, 0.792, 0.747, 0.756, 0.842, 0.85, 0.775, 0.786, 0.792, 0.803, 0.744, 0.769, 0.8, 0.825, 0.783, 0.753, 0.711, 0.722, 0.7, 0.719, 0.744, 0.764, 0.725, 0.75, 0.736, 0.717, 0.697, 0.742, 0.778, 0.792, 0.758, 0.772, 0.758, 0.764, 0.758, 0.758, 0.8, 0.808, 0.806, 0.794, 0.783, 0.758, 0.806, 0.811, 0.825, 0.822, 0.808, 0.806, 0.797, 0.789, 0.767, 0.844, 0.831, 0.783, 0.789, 0.775, 0.775, 0.783, 0.792, 0.808, 0.825, 0.814, 0.753, 0.758, 0.767, 0.794, 0.822, 0.811, 0.803, 0.85, 0.789, 0.753, 0.781, 0.811, 0.825, 0.822, 0.811, 0.775, 0.756, 0.744, 0.772, 0.794, 0.781, 0.8, 0.828, 0.794, 0.725, 0.761, 0.8, 0.853, 0.822, 0.789, 0.789, 0.539, 0.95, 0.808, 0.839, 0.842, 0.822, 0.811, 0.778, 0.758, 0.769, 0.781, 0.8, 0.819, 0.814, 0.786, 0.756, 0.756, 0.764, 0.797, 0.819, 0.806, 0.806, 0.786, 0.761, 0.767, 0.769, 0.8, 0.839, 0.839, 0.803, 0.781, 0.781, 0.794, 0.789, 0.825, 0.817, 0.844, 0.794, 0.781, 0.764, 0.822, 0.828, 0.803, 0.817, 0.808, 0.792, 0.772, 0.775, 0.8, 0.836, 0.831, 0.792, 0.792, 0.767, 0.792, 0.775, 0.822, 0.822, 0.85, 0.811, 0.772, 0.778, 0.781, 0.8, 0.817, 0.839, 0.814, 0.814, 0.794, 0.769, 0.758, 0.819, 0.858, 0.839, 0.772, 0.75, 0.789, 0.797, 0.783, 0.789, 0.825, 0.842, 0.814, 0.731, 0.75, 0.811, 0.822, 0.772, 0.789, 0.8, 0.794, 0.589, 0.906, 0.839, 0.844, 0.839, 0.808, 0.778, 0.642, 0.881, 0.797, 0.767, 0.797, 0.844, 0.831, 0.736, 0.756, 0.778, 0.817, 0.8, 0.792, 0.803, 0.819, 0.775, 0.736, 0.772, 0.611, 1.022, 0.875, 0.833, 0.783, 0.786, 0.808, 0.8, 0.814, 0.822, 0.839, 0.814, 0.775, 0.772, 0.797, 0.794, 0.817, 0.625, 1.0, 0.814, 0.808, 0.783, 0.589, 1.008, 0.883, 0.836, 0.8, 0.814, 0.794, 0.831, 0.811, 0.847, 0.853, 0.828, 0.786, 0.783, 0.797, 0.847, 0.872, 0.822, 0.836, 0.8, 0.794, 0.778, 0.797, 0.85, 0.853, 0.842, 0.8, 0.806, 0.806, 0.811, 0.808, 0.842, 0.836, 0.842, 0.786, 0.778, 0.814, 0.844, 0.856, 0.819, 0.847, 0.797, 0.814, 0.792, 0.806, 0.858, 0.858, 0.839, 0.778, 0.803, 0.8, 0.811, 0.819, 0.833, 0.847, 0.819, 0.778, 0.769, 0.792, 0.817, 0.833, 0.839, 0.806, 0.808, 0.786, 0.797, 0.8, 0.847, 0.839, 0.853, 0.811, 0.775, 0.797, 0.8, 0.819, 0.844, 0.847, 0.806, 0.811, 0.781, 0.764, 0.814, 0.817, 0.822, 0.806, 0.789, 0.769, 0.797, 0.794, 0.794, 0.853, 0.819, 0.808, 0.8, 0.578, 0.953, 0.853, 0.847, 0.844, 0.844, 0.808, 0.767, 0.797, 0.781, 0.839, 0.856, 0.828, 0.783, 0.8, 0.792, 0.6, 0.944, 0.817, 0.836, 0.819, 0.764, 0.753, 0.806, 0.792, 0.822, 0.828, 0.808, 0.828, 0.797, 0.769, 0.775, 0.853, 0.828, 0.819, 0.797, 0.783, 0.786, 0.806, 0.794, 0.822, 0.85, 0.828, 0.775, 0.747, 0.747]
points = []
length = len(rr_intervals)
for i in sorted(list(set(rr_intervals))):
    points.append([i, rr_intervals.count(i)])
print(points)
expvalue = 0
for i in range(1, len(points)):
    expvalue += integrate(x * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                                 (x, points[i-1][0], points[i][0]))
print(expvalue)  # математическое ожидание
dispersion = 0
for i in range(1, len(points)):
    dispersion += integrate(x**2 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                            (x, points[i-1][0], points[i][0]))
dispersion -= expvalue**2
print(dispersion)  # дисперсия и одновременно "D" - второй статистический момент
print(sqrt(dispersion))  # среднее квадратическое отклонение

def mean(): # - математическое ожидание вычисляемое как среднее
    return sum(rr_intervals)/len(rr_intervals)



def SDNN():  # SDNN стандартное отклонение NN интервалов
    mean = sum(rr_intervals)/len(rr_intervals)
    sumNN = 0
    for i in rr_intervals:
        sumNN += (i - mean) ** 2
    return sqrt(sumNN/(len(rr_intervals) - 1))


def SDANN():  # стандартное отклонение средних значений SDNN
    return SDNN() / sqrt(len(rr_intervals))


def RMSSD():  # квадратный корень из суммы квадратов разности величин последовательных RR-интервалов
    return sqrt(sum([(rr_intervals[i] - rr_intervals[i-1]) ** 2 for i
                     in range(1, len(rr_intervals))]) / (len(rr_intervals) - 2))


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


def CV():  # коэффициент вариации. Представляет собой норированную оценку СКО
    return 100 * sqrt(dispersion) / expvalue


def D():
    dispersion = 0
    for i in range(1, len(points)):
        dispersion += integrate(x ** 2 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                                (x, points[i - 1][0], points[i][0]))
    dispersion -= expvalue ** 2
    return dispersion


def As():
    answer = 0
    for i in range(1, len(points)):
        answer += integrate(x**3 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                            (x, points[i - 1][0], points[i][0]))
    return answer / (sqrt(dispersion)**3)


def Ex():
    answer = 0
    for i in range(1, len(points)):
        answer += integrate(x**4 * ((points[i][1] / length) / (points[i][0] - points[i - 1][0])),
                            (x, points[i - 1][0], points[i][0]))
    return ((answer / dispersion ** 2) - 3)


def mode():
    i = 0
    mode = 0
    while i < 2.45:
        i += 0.05
        print(float("{:.3f}".format(round(i * 100) / 100)))


print(mode())
