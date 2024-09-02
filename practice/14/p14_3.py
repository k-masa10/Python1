a = list(input('文字列を入力:'))
print('結果文字列:',end='')
if len(a) >= 10:
    for i in range(10):
        print(f'{a[i]}',end='')
else:
    for i in range(len(a)):
        print(f'{a[i]}',end='')