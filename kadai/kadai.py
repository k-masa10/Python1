import datetime

hour = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute
task_list = []
deadline_list =[]
end_list = []
menu = 0
end_point = 0

# タスクの表示
def display_tasks():
    if task_list == []:
            print('現在タスクはありません')
    else:
        print('現在のタスク一覧')
        for i in range(len(task_list)):
            print(f'{i+1}.{task_list[i]}-締め切り:{deadline_list[i]}-状態:{end_list[i]}')
        i = 0

# タスクの追加
def add_task():
    task_name = input('タスク名を入力してください:')
    task_list.append(task_name)
    deadline_list.append(input('締切りを入力してください:'))
    end_list.append('未完了')
    print(f'タスク’{task_name}’が追加されました。')

# タスクの進捗率の計算
def calculate_completion(end_point):
    for i in range(len(end_list)):
        if end_list[i] == '完了':
            end_point += 1
    try:
        print(f'タスクの進行率は{end_point*100/len(end_list)}%です。')
    except ZeroDivisionError:
        print('現在タスクはありません')
    end_point = 0
    i = 0

# タスクの完了をマーク
def mark_task_complete():
    print('現在のタスク一覧です')
    for i in range(len(task_list)):
        print(f'{i+1}.{task_list[i]}-締め切り:{deadline_list[i]}-状態:{end_list[i]}')
        i = 0
    try:
        end = int(input('\n完了にするタスクの番号を入力してください:'))
        if end > len(task_list):
            print(f'{end}番のタスクは存在しません')
        else:
            end_list[end-1] = '完了'
            print(f'タスク’{task_list[end-1]}’を完了にしました。')
    except ValueError:
        print('整数を入力してください')

print(f'タスク管理システムへようこそ。現在の時刻は、{hour}時{minutes}分です。\n')
while menu != 5:
    print('\nメニュー')
    print('1:タスクを表示')
    print('2:タスクを追加')
    print('3:タスクの進捗率を計算')
    print('4:タスクの完了をマーク')
    print('5:終了')
    try:
        menu = int(input('選択してください:'))
    except ValueError:
        print('選択されていません')

    if menu == 1:
        display_tasks()

    if menu == 2:
        add_task()

    if menu == 3:
        calculate_completion(end_point)

    if menu == 4:
        mark_task_complete()

    if menu == 5:
        print('プログラムを終了します。')