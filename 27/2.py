"""
Дана последовательность из N натуральных чисел. Рассматриваются все её непрерывные подпоследовательности, такие
что сумма элементов каждой из них кратна k = 73. Найдите среди них подпоследовательность с максимальной суммой, определите её длину.
Если таких подпоследовательностей найдено несколько, в ответе укажите количество элементов самой короткой из них.
"""
with open('', 'r') as f:
    n = int(f.readline())
    k = 73
    arr = [10 ** 10] * k
    arr[0] = 0
    length = [0] * k
    summa = 0
    s_length = 0
    for _ in range(n):
        item = int(f.readline())
        summa += item
        s_length += 1
        ost = summa % k
        if ost == 0:
            if summa > arr[0]:
                arr[0] = summa
                length[0] = s_length
            elif summa == arr[0]:
                length[0] = min(length[0], s_length)
        else:
            tmp = summa - arr[ost]
            tmp_length = s_length - length[ost]
            if tmp > arr[0]:
                arr[0] = tmp
                length[0] = tmp_length
            elif tmp == arr[0]:
                length[0] = min(length[0], tmp_length)
            if summa < arr[ost]:
                arr[ost] = summa
                length[ost] = s_length
            elif summa == arr[ost]:
                length[ost] = max(length[ost], s_length)
    print(length[0])
