"""
Дана последовательность натуральных чисел. Рассматриваются все её непрерывные подпоследовательности,
состоящие более чем из ста элементов. Необходимо определить количество таких подпоследовательностей,
сумма элементов которых кратна 999.
"""
with open('', 'r') as f:
    n = int(f.readline())
    k = 999
    arr = [0] * k
    queue = []
    summa = 0
    count = 0
    for i in range(100):
        summa += int(f.readline())
        queue.append(summa)
    for i in range(100, n):
        item = int(f.readline())
        summa += item
        ost = summa % k
        if ost == 0:
            count += arr[ost] + 1  # + 1, т.к если из подпосл. с остатком 0 вычесть подпосл. с остатком 0, то остаток получится 0
        else:
            count += arr[ost]
        arr[queue[i % 100] % k] += 1
        queue[i % 100] = summa
    print(count)
