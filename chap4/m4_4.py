a = 1
b = 1
c = 0
for num in range(9):
    for num in range(9):
        c = a*b
        if a%2==0:
            continue
        if c >=50:
            break
        print(f'{a}×{b}={c}')
        b += 1
    b = 1
    a += 1