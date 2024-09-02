def leap_year(year, a):
    if year % 400 == 0:
        a = True
    elif year % 4 == 0 and year % 100 != 0:
        a = True
    if a == True:
        print(f'西暦{year}年は、うるう年です')
    else:
        print(f'西暦{year}年は、うるう年ではありません')

leap_year(int(input('西暦を入力>>')), False)