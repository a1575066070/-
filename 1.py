# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


msg = "欢迎来到 英雄无敌的世界......!"
print(msg)
if __name__ =="__main__":
    class hero:
        def __init(self, name = 'hzl', hp = 1000, atk = 500):
            self.name = name
            self.hp = hp
            self.atk = atk
            print('英雄 %s 诞生!!' %self.name)
        def hit(self,name):
            name.hp -= self.atk
        def blood(self):
            pass

class Element:
    def __init__(self,name = 'boss',hp = 1000):
        self.name = name
        self.hp = hp
        print('BOSS %s 诞生!!' %self.name)
        
    def hit(self):
        pass
boss = Element('boss')

print("boss hp:",boss.hp)
print("英雄发起攻击!")
print("boss hp:",boss.hp)
    
    