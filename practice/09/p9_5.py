def a1(b, c):
    d1 = b + c
    print(f'{b}+{c}={d1}')

def a2(b, c):
    d1 = b - c
    print(f'{b}-{c}={d1}')

def a3(b, c):
    d1 = b * c
    print(f'{b}*{c}={d1}')

def a4(b, c):
    d1 = b / c
    print(f'{b}/{c}={d1}')

def a5(b, c):
    d1 = b % c
    print(f'{b}%{c}={d1}')

x = int(input('整数を入力してください:'))
y = int(input('整数を入力してください:'))
a1(x, y)
a2(x, y)
a3(x, y)
a4(x, y)
a5(x, y)