def eat(breakfast, lunch='ラーメン', dinner='カレー', *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

# print('8月1日')
# eat('トースト', 'おにぎり')
# print('8月2日')
# eat('納豆ご飯', 'ラーメン')
# print('8月3日')
# eat('バナナ', 'そば', '焼肉')
# print('8月4日')
# eat('サンドウィッチ', 'シュウマイ弁当')
# eat(breakfast='納豆ごはん', dinner='カレーうどん')
# eat(dinner='カレーうどん', breakfast='納豆ごはん')
# eat('納豆ごはん', dinner='カレーうどん')
eat('トースト', 'パスタ', 'カレー', 'アイス', 'チョコ', 'カレー')