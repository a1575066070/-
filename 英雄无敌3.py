print('#########################################')
print('#############欢迎来到英雄无敌############')
print('#############广告位招商中....############')
print('#############广告位招商中....############')
use = str(input('请创建用户名：'))
pw1 = str(input('请创建密码：'))
pw2 = str(input('请再次确认密码:'))
while True:
    if pw1 == pw2:
        print('用户名为：',use)
        print('密码为：',pw1)
        break
    else:
        print('两次密码不同 请重新输入：')
        pw1 = str(input('请输入密码：'))
        pw2 = str(input('请再次确认密码:'))
print('#########################################')
name = str(input('请创建英雄名字：'))
if name == '':
    name = '玩家一'
    print('英雄名称默认为：',name)
else:
    print('英雄名称为：',name)


profess = str(input('请输入对应字母选择英雄职业<A.神枪手 B.鬼剑士 C.魔法师 D.圣职者>:'))
PA = 'HP=2000 MP=300 ATK=600 DEF=500'
PB = 'HP=2000 MP=300 ATK=600 DEF=500'
PC = 'HP=2000 MP=800 ATK=400 DEF=300'
PD = 'HP=2000 MP=400 ATK=500 DEF=600'
while True:
    if profess == 'A':
        print('英雄职业为神枪手',PA)
        break

    elif profess == 'B':
        print('英雄职业为鬼剑士',PB)
        break

    elif profess == 'C':
        print('英雄职业为魔法师',PC)
        break

    elif profess == 'D':
        print('英雄职业为圣职者',PD)
        break
    else:
        print('职业不存在 请重新输入:')
        profess = str(input('请输入对应字母选择英雄职业<A.神枪手 B.鬼剑士 C.魔法师 D.圣职者>:'))

print('###########################')
print('###########################')

print('######人物加载完成 欢迎来到新手村#####')
print('#####英雄可四处移动寻找随机任务#####')
print('#可使用键盘的W、A、S、D、操控英雄移动#')

move = str(input())
while True:
    if move == 'A':
        print('人物向左走')
        break

    elif move == 'W':
        print('人物向前走')
        break

    elif move == 'S':
        print('人物向后走')
        break

    elif move == 'D':
        print('人物向右走')
        break
    else:
        print('憋瞎摁了 快走吧')
        move = str(input())

move = str(input())
while True:
    if move == 'A':
        print('人物向左走')
        break

    elif move == 'W':
        print('人物向前走')
        break

    elif move == 'S':
        print('人物向后走')
        break

    elif move == 'D':
        print('人物向右走')
        break
    else:
        print('憋瞎摁了 快走吧')
        move = str(input())

move = str(input())
while True:
    if move == 'A':
        print('人物向左走')
        break

    elif move == 'W':
        print('人物向前走')
        break

    elif move == 'S':
        print('人物向后走')
        break

    elif move == 'D':
        print('人物向右走')
        break
    else:
        print('憋瞎摁了 快走吧')
        move = str(input())

move = str(input())
while True:
    if move == 'A':
        print('人物向左走')
        break

    elif move == 'W':
        print('人物向前走')
        break

    elif move == 'S':
        print('人物向后走')
        break

    elif move == 'D':
        print('人物向右走')
        break
    else:
        print('憋瞎摁了 快走吧')
        move = str(input())

move = str(input())
while True:
    if move == 'A':
        print('人物向左走')
        break

    elif move == 'W':
        print('人物向前走')
        break

    elif move == 'S':
        print('人物向后走')
        break

    elif move == 'D':
        print('人物向右走')
        break
    else:
        print('憋瞎摁了 快走吧')
        move = str(input())
