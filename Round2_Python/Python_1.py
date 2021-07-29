'''
【简答题】一个Python编程练习，根据题干要求，在【拉勾系统】的答题框提交gitee或者github代码链接。
- 每行代码，或每个方法要求添加注释（基础不好的同学）
题目内容：
1. ⼀个回合制游戏，有两个英雄，分别以两个类进⾏定义。分别是Timo和Jinx。每个英雄都有 hp 属性和 power属性，hp 代表⾎量，power 代表攻击⼒
2. 每个英雄都有⼀个 fight ⽅法， fight ⽅法需要传⼊“enemy_hp”（敌⼈的⾎量），“enemy_power”（敌⼈的攻击⼒）两个参数。需要计算对打一轮过后双方的最终血量，
英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp-英雄的power属性
3. 对⽐英雄最终的⾎量和敌⼈最终的⾎量，⾎量剩余多的⼈获胜。如果英雄赢了打印 “英雄获胜”，如果敌⼈赢了，打印“敌⼈获胜”
4. 使用继承、简单工厂方法等各种方式优化你的代码
'''

class Hero:
    hp=0  #hp 代表⾎量
    power=0   #power 代表攻击⼒
    name=''

    def fight(self,enemy_hp,enemy_power,enemy_name):
        last_hp=self.hp-enemy_power
        last_enemy_hp=enemy_hp-self.power
        if last_hp>last_enemy_hp:
            print(f'{self.name}获胜')
        elif last_hp==last_enemy_hp:
            print('平局')
        else:
            print(f'{enemy_name}赢了')

class Jinx(Hero):
    hp=1200
    power=500
    name='jinx'

class Timo(Hero):
    hp = 1200
    power = 600
    name = 'Timo'

if __name__ == '__main__':
    Jx=Jinx()
    Jx.fight(1200,800)







