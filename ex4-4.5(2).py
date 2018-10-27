from random import *
x=1
n=randint(0,100)
s=eval(input("输入一个0到100的整数："))
try:
    num=eval(input("请输入一个整数"))
except NameError:
    print("输入错误，请输入一个整数")
while s!=n:
    x=x+1
    if s<n:
        print("遗憾，太小了")
    if s>n:
        print("遗憾，太大了")
    s=eval(input("再输入一个0到100的整数："))
print("预测{}次，猜对了".format(x))
