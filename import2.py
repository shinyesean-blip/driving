import random
start = input ('請輸入隨機數字範圍值')
end = input ('請決定結束隨機數字範圍值')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
    count += 1  # 每次猜測次數+1
    num = input('使用者輸入數字:')
    num = int(num)
    if num == r:
        print('你猜中!')
        print('總共猜了', count, '次')
        break  # 猜中跳出迴圈
    elif num > r:
        print('比答案大!')
    elif num < r:
        print('比答案小!')
    print('這是你猜的', count, '次')