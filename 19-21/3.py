"""
2 кучи
68 <= сумма <= 80 - победа игрока, сделавшего последний ход
сумма > 80 - проигрыш игрока, сделавшего последний ход
ходы: +1, *3
в 1 куче - 6, во 2 - s
"""


def f(a, b, c, m):
    if 68 <= a + b <= 80:
        return c % 2 == m % 2
    if a + b > 80:
        return c % 2 != m % 2
    if c == m:
        return 0
    variants = [
        f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m),
        f(a * 3, b, c + 1, m), f(a, b * 3, c + 1, m)
    ]
    return any(variants) if (c + 1) % 2 == m % 2 else all(variants)  # если (в 19) неудачный или минимально возможный, то all заменить на any


for s in range(1, 62):
    for m in range(1, 5):
        if f(6, s, 0, m):
            if m == 2:  # для задания 19 m = 2, 20 - m = 3, 21 - m = 4
                print(s)
            break
