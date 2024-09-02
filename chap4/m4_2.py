count = 1
print('カレーを召し上がれ')
print(f'{count}皿のカレーを食べました')
key = input(f'おかわりはいかがですか？(y/n) >>')
while key == 'y':
    count += 1
    print(f'{count}皿のカレーを食べました')
    key = input(f'おかわりはいかがですか？(y/n) >>')
    if key == 'n':
        print('ごちそうさまでした')