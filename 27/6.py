"""
На вход программе подается последовательность целых чисел. Рассматриваются все непрерывные подпоследовательности
исходной последовательности, такие что произведение элементов каждой из них не кратно M = 345600.
Найдите количество таких подпоследовательностей.
"""
with open('', 'r') as f:
    n = int(f.readline())
    arr = [int(i) for i in f]
    all = sum(range(n + 1))
    errors = 0
    m = 345600
    left = 0
    mul = 1
    for right in range(n):
        mul *= arr[right]
        while mul % m == 0:
            errors += n - right
            mul //= arr[left]
            left += 1
    print(all - errors)
