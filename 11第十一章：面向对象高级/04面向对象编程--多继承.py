"""

多继承：一个类可以继承多个类，从而获取多个类的属性和方法（非私有）
    子类可以继承多个父类的属性和方法（非私有）


注意：当一个类继承了多个父类时，默认优先使用第一个父类中的同名属性或方法
     可以使用 类名.__mro__属性或类名.mro()方法查看调用顺序

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



#华为智驾
class HuaweiZhiJia:
    """华为智能驾驶"""
    def __init__(self,version="1.0"):
        self.version = version


    def run(self):
        print(f"使用华为AI智能驾驶系统{self.version} 正在行驶...")



#问界汽车
class WenJieCar(Car, HuaweiZhiJia):
    def __init__(self, brand, model, color, owner, version="1.0"):
        Car.__init__(brand, model, color, owner)
        HuaweiZhiJia.__init__(self, version)




if __name__ == '__main__':
    c=WenJieCar("BWM","X5","黑色","河南彭于晏")
    print(c.__dict__)
