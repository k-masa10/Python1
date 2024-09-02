# for i in range(3):
#     answer.append(randint(0, 9))

# while a == 1:
#     for i in range(1,4):
#         prediction.append(int(input(f'{i}桁目の予想を入力(0~9)>>')))
#     print(answer)
#     print(prediction)
#     answer2 = []
#     for n in answer:
#         answer2.append(n)
#     for j in range(3):
#         if answer2[j] == prediction[j]:
#             h += 1
#             answer2[j] == 10
#     for k in range(3):
#         if prediction[k] in answer2:
#             b += 1
#             answer2.remove(prediction[k])
#     print(f'{h}ヒット！{b}ボール！')
#     if h == 3:
#         print('正解です！')
#     else:
#         a = int(input('続けますか？1:続ける 2:終了>>'))
#         prediction = []
from random import randint

answer = []
prediction = []
answer2 = []

h = 0
b = 0
c = 1

while len(answer) < 3:
    a = randint(0, 9)
    if a not in answer:
        answer.append(a)
print(answer)

while c == 1:
    for i in range(1, 4):
        prediction.append(int(input(f'{i}桁目の予想を入力(0~9)>>')))
    for n in answer:
        answer2.append(n)
    print(answer2)
    for j in range(3):
        if answer2[j] == prediction[j]:
            h += 1

    for y in range(3):
        if prediction[y] in answer2:
                b += 1
    b -= h
    print(f'{h}ヒット！{b}ボール！')
    if h == 3:
        print('正解です！')
    else:
        a = int(input('続けますか？1:続ける 2:終了>>'))
        prediction = []