from random import *
seed(0)
p = randint(0,100)
count = 0;
while True:
    try:
        n = int(input('请输入一个0-100之间的整数：'))
    except:
        print("输入错误！")
        break

    while s!=n:
        x=x+1
        if s<n:
            print("遗憾，太小了")
        if s>n:
            print("遗憾，太大了")
        s=eval(input("再输入一个0到100的整数："))
    print("预测{}次，猜对了".format(x))
