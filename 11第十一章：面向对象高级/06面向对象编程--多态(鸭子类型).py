"""

鸭子类型：如果它走起路来像鸭子，叫起来像鸭子，那么它就是鸭子。——动态类型语言的多态

"""


class Duck:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def swimming(self):
        print(f"Duck:{self.age}岁的{self.name}正在游泳。。。")


class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def swimming(self):
        print(f"Dog:{self.age}岁的{self.name}正在游泳。。。")


class Pig:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def swimming(self):
        print(f"Pig:{self.age}岁的{self.name}正在游泳。。。")



def go_swimming(duck:Duck):
    duck.swimming()



#测试代码
if __name__ == '__main__':
    go_swimming(Duck("小鸭",1))
    go_swimming(Dog("小狗",2))
    go_swimming(Pig("小猪",3))












