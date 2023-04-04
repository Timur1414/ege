"""
Дана последовательность натуральных чисел. Рассматриваются все её
непрерывные подпоследовательности, такие что сумма элементов каждой из них
кратна K = 73. Найдите наибольшую сумму такой подпоследовательности.
"""
with open('27_B.txt', 'r') as f:
    n = int(f.readline())
    k = 73
    arr = [10 ** 10] * k  # суммы, которые будут вычитаться из общей
    arr[0] = 0  # здесь будет ответ
    summa = 0
    for _ in range(n):
        item = int(f.readline())
        summa += item
        ost = summa % k
        if ost == 0:
            arr[0] = max(arr[0], summa)
        else:
            tmp = summa - arr[ost]
            arr[0] = max(arr[0], tmp)
            arr[ost] = min(arr[ost], summa)
    print(arr[0])
