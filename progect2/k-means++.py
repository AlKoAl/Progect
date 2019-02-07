from math import sqrt
import random


def metric(a, b):  # a, b - точки, одна из которых  центроид, а другая точка выборки
    count = 0
    for i in range(len(a)):
        count += (a[i] - b[i]) ** 2  # считает Евклидово расстояние
    return sqrt(count)


#  надо будет потом реализовать k-means++
def k_means(X, k=5):
    new = [[random.choice(X)]]  # начальные центроиды, первый уже выбран

    while len(new) != k:  # пока количество центроидов не достигнет требуемого
        sum_dist = 0
        # расстояние = metric**2
        for i in X:  # пробегаем по всем точкам исходных данных
            distanses = [metric(i, x) ** 2 for x in [j[0] for j in new]]  # список расстояний до центроидов
            sum_dist += min(distanses)  # подсчёт суммы квадратов расстояний
            new[distanses.index(min(distanses))].append(i)  # выбираем наименьшее и добавляем к списку центроида точку
        temp_dist = random.random()*sum_dist  # случайное число от 0 до sum_dist
        growing_amount = 0  # переменная-счётчик суммы квадратов длин
        result = 0  # значение результирующей точки
        for i in [cluster[:] for cluster in new]:  # пробегаем по всем спискам (центроид + точки,
            #  к которым он ближе всего и он сам)
            if growing_amount >= temp_dist:
                break
            for point in i[1:]:
                if growing_amount >= temp_dist:
                    continue
                growing_amount += metric(point, i[0]) ** 2
                result = point
        new = [[j[0]] for j in new] + [[result]]  # снова возвращаемся к списку только центроидов и добавляем новый
        print(new)

    while True:  # просто вторая чать k-means
        for i in X:
            distanses = [metric(i, x) ** 2 for x in [j[0] for j in new]]
            new[distanses.index(min(distanses))].append(i)
        #  распределил по класстерам находя минимальные расстояния (метрики) ** 2
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
