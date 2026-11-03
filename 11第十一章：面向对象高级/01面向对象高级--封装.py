"""
封装：将数据（属性）和操作数据的方法绑定在一起，形成一个独立的单元（类）
     保护数据，不被外部访问和修改，通过访问修饰符实现封装
     1、私有属性：在属性名前加__，只能在类的内部访问，外部不能访问
     2、私有方法：在方法名前加__，只能在类的内部调用，外部不能调用

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


if __name__ == '__main__':
    car = Car("奥迪","A6","黑色","河南彭于晏")

    print(car.brand)
    print(car.model)
    print(car.color)
    #print(car.__owner)



    car.start()
    car.run()
    car.stop()
    #car.__get_owner()
    print(car.get_owner())

