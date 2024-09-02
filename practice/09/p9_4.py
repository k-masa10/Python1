def a(b):
    b *= 3
    return b

c = int(input('整数を入力してください:'))
b = a(c)
b = a(b)
print(f'{c}の9倍は{b}です。')