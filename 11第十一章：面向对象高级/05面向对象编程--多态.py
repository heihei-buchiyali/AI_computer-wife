"""

多态：同一个方法，不同的实现方式，不同的对象，调用同一个方法，结果不同


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


#电车
class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电")


#补充燃料函数
def handle_charge(car:Car):#函数参数类型声明----指定是父类型
    car.charge()





if __name__ == '__main__':
    handle_charge(FuelCar("BWM","X5","黑色","张三"))
    handle_charge(ElectricCar("奥迪","A6","黑色","李四"))
