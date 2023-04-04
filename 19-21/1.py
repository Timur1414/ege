"""
1 куча
>= 30 в куче - победа
ходы: +2, +3, *2
"""


def f(a, c, m):
    if a >= 30:
        return c % 2 == m % 2
    if c == m:
        return 0
    variants = [
        f(a + 2, c + 1, m), f(a + 3, c + 1, m), f(a * 2, c + 1, m)
    ]
    return any(variants) if (c + 1) % 2 == m % 2 else all(variants)  # если (в 19) неудачный или минимально возможный, то all заменить на any


for s in range(1, 30):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 2:  # для задания 19 m = 2, 20 - m = 3, 21 - m = 4
                print(s)
            break
