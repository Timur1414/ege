"""
На каждом километре кольцевой автодороги с двусторонним движением установлены контейнеры для мусора.
Длина кольцевой автодороги равна N километров. Нулевой километр и N-й километр автодороги находятся в одной точке.
Известно количество мусора, которое накапливается ежедневно в каждом из контейнеров. Из каждого пункта мусор вывозит отдельный мусоровоз.
Стоимость доставки мусора вычисляется как произведение количества мусора на расстояние от пункта до центра переработки.
Определите разницу между минимальной возможной и максимальной возможной стоимостями перевозки мусора.
"""


with open('', 'r') as f:
    n = int(f.readline())
    arr = [int(i) for i in f]
    summa = 0
    res = [0] * n
    for i in range(n):
        dist = min(i, n - i)
        summa += arr[i] * dist
    res[0] = summa
    index = n // 2
    right = sum(arr[index:])
    left = sum(arr[1: index])
    for i in range(1, n):
        right += arr[i - 1] - arr[index]
        left += arr[index]
        res[i] = res[i - 1] - left + right
        left -= arr[i]
        index = (index + 1) % n
    print(max(res) - min(res))


"""
другая задача
"""


with open('', 'r') as f:
    n = int(f.readline())
    arr = [int(i) for i in f]
    left = sum(arr[n // 2:])
    right = sum(arr[:n // 2])
    res = 10 ** 10
    summa = 0
    for i in range(n):
        dist = min(i, n - i)
        summa += dist * arr[i]
    res = summa
    for center in range(1, n):
        right += arr[(center + n // 2 - 1) % n] - arr[center - 1]
        left += ar[center - 1] - arr[(center + n // 2 - 1) % n]
        summa += left - right
        res = min(res, summa)
    print(res)
