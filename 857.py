import random
a = random.randint(1,100)
b = int(input('请输入数字：'))
i = 0
while True:
    i++;
    if b > a:
        print('输入数字太大')
    elif b < a:
        print('输入数字太小')
    elif b == a:
        print('随机数字为：',str(a)+'\n猜的次数为：'+str(i))
