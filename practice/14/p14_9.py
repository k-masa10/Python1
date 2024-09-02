a = '東京都千代田区神田神保町千代田ビル1階'
b = a.count('千代田')
a = a.replace('千代田','中央')
print(a)
print(f'置換した個数：{b}')