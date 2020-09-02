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

    
    
