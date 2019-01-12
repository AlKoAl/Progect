""" Считывает первые пять минут из любой записи PhysioNet на основе файлов с аннотациями
Не учитывает экстрасистолы. Как я понял premature beat - это они
Необходима дальнейшая оптимизация..."""
import wfdb
from IPython.display import display
import math
annotation2 = wfdb.rdann('100', 'atr', pb_dir='mitdb')
display(annotation2.__dict__)
qrs_locs = []
i, j = 0, 0
while annotation2.fs * 300 > annotation2.sample[j]:
    # вычисляем в пятиминутном интервале RR-интервалы
    if annotation2.symbol[j] in ['N', 'L', 'R', 'B', 'A', 'a', 'J', 'S', 'V', 'r', 'F', 'e', 'j', 'n', 'E', 'f', 'Q']:
        qrs_locs.append(annotation2.sample[i])
    i, j = i + 1, j + 1
print(qrs_locs, len(qrs_locs))
rr_intervals = []
for i, j in zip(qrs_locs[1:], qrs_locs):
    rr_intervals.append(round((i - j)/annotation2.fs, 3))
print(rr_intervals)
print(len(rr_intervals))
# отлично, теперь у меня есть наюор интервалов. Настало время статистики.


def RR_histogram():
    # не по ГОСТу в обе стороны
    # Потом разберёмся графическим выведением гистогаммы
    # Ну и кодище-чудовище
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
