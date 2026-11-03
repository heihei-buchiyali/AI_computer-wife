#魔法方法
#Python中提供的__xxx__形式的特殊方法
#魔法方法无需手动调用，Python会在合适的时机自动调用


#---------------------定义类 魔法方法---------------------------------
class Car:
    def __init__(self,c_color,c_name,c_brand,c_price):
        self.color=c_color
        self.brand=c_brand
        self.price=c_price
        self.name=c_name

        print("Car类型的对象初始化完毕，对象属性已经添加完毕")



    def running(self):
         print(f"{self.brand}{self.name}正在高速行驶中.....")

    def total_coat(self,discount,rate=0.1):

        total_cost=self.price*discount+rate*self.price
        return total_cost

    #魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self,other):
        return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price

    def __lt__(self,other):
        return self.price<other.price


#测试
c1=Car("红色","宝马","BMW",800000)
print(c1)

c2=Car("红色","宝马","BMW",1800000)
print(c2)

print(c1==c2)

print(c1<c2)
