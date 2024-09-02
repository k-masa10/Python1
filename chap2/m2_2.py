scores={
    'Japanese':int(input('国語の点数を記入 >>')),
    'mass':int(input('算数の点数を記入 >>')),
    'science':int(input('理科の点数を記入 >>')),
    'socitey':int(input('社会の点数を記入 >>')),
    'english':int(input('英語の点数を記入 >>')),
        }
total=sum(scores.values())
avg=total/len(scores)
print(f'合計点:{total}点｜平均点:{avg}点')