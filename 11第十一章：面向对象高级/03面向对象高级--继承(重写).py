"""
继承：描述的是两个类之间的关系，子类继承父类
    子类就可以获取到父类中的属性和方法（非私有）


注意：如果子类再重写父类的方法时，需要调用父类的方法
    可以通过 父类名.方法名（self）/super.() 调用父类的方法

"""


class Car:
    def __init__(self, brand,model,color,owner):
        self.brand = brand  # 品牌
        self.model = model  # 型号
        self.color = color  # 颜色
        self.__owner = owner    #  拥有者（私有属性）

    def start(self): #启动
        print(f"{self.brand} {self.model}  正在启动。。。")


    def run(self): #行驶
        print(f"{self.__owner} : {self.brand}{self.model}   正在行驶。。。")
        self.__owner_fuel()

    def stop(self): #停止
        print(f"{self.brand}{self.model}   正在停止。。。")


    def __owner_fuel(self): #获取拥有者
        print(f"{self.brand} {self.model} 的拥有者是：{self.__owner}")


    def get_owner(self): #获取拥有者
        return self.__owner[0:1]+"南**"


    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料")





#燃油车
class FuelCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油")

        #方式一：
        super().charge()

        #方式二：
        Car.charge(self)

#电车
class ElectricCar(Car):
    pass


if __name__ == '__main__':
    c1=FuelCar("BMW","X5","黑色","河南彭于晏")
    c1.charge()





