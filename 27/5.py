"""
 На вход программе подается последовательность целых чисел. Рассматриваются все непрерывные подпоследовательности
 исходной последовательности, такие что произведение элементов каждой из них является делителем числа M = 4 043 520.
 Найдите количество таких подпоследовательностей.
"""
with open('', 'r') as f:
    n = int(f.readline())
    arr = [int(i) for i in f]
    all = sum(range(n + 1))
    errors = 0
    m = 4_043_520
    left = 0
    mul = 1
    for right in range(n):
        mul *= arr[right]
        while m % mul != 0:
            errors += n - right
            mul //= arr[left]
            left += 1
    print(all - errors)
