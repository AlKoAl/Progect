from math import sqrt
from random import uniform


def metric(a, b):  # a, b - точки, одна из которых  центроид, а другая точка выборки
    count = 0
    for i in range(len(a)):
        count += (a[i] - b[i]) ** 2
    return sqrt(count)


#  надо будет потом реализовать k-means++
def k_means(X, k=5):
    new = []
    while len(new) != k:
        new = new + [[[]]]
        for i in range(len(X[0])):
            chose = uniform(0.9 * min([j[i] for j in X]), 1.1 * max([j[i] for j in X]))
            new[len(new) - 1][0].append(chose)
    # выбрал случайные k точек из выборки, а надо было просто случайных
    # обернуть всё нижележащее в цикл
    while True:
        for i in X:
            distanses = [metric(i, x) ** 2 for x in [j[0] for j in new]]
            new[distanses.index(min(distanses))].append(i)
        #  распределил по класстерам находя рассттояния (метрики) ** 2
        to_new_cycle = []
        for i in new:
            if len(i) == 1:
                to_new_cycle.append(i)
            else:
                sum = [0 for i in range(len(i[0]))]
                for j in i[1:]:
                    for g in range(len(i[0])):
                        sum[g] = sum[g] + j[g]
                to_new_cycle.append([[g / len(i[1:]) for g in sum]])
        # нашёл новые центры масс
        if any([to_new_cycle[i][0] != new[i][0] for i in range(len(to_new_cycle))]):
            new = to_new_cycle
            continue
        else:
            return to_new_cycle  # выводит только центры кластеров
        # поставил проверку. если есть хотя бы один отличный центроид, пересчитываем всё снова

X = [[1, 5], [35, 4], [16, 32], [3, 10], [86, 47], [37, 90], [50, 97]]
print(k_means(X))
