a = int(input('第一个数字:'))
b = int(input('第二个数字:'))
c = str(input('输入计算符号:'))
if c == '+':
    print('计算结果为：'+str(a+b))
elif c == '-':
    print('计算结果为：'+str(a-b))
elif c == '*':
    print('计算结果为：'+str(a*b))
elif c == '/':
    print('计算结果为：'+str(a/b))
else:
    print('输入错误 无结果')
