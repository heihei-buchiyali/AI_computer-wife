#实例属性与类属性

class Car:
    #类属性（所有实例对象共享的）
    wheel=4 #轮胎数量
    tax_rate=0.1#购置税税率


    def __init__(self,c_color,c_name,c_brand,c_price):

        #实例属性
        self.color=c_color
        self.brand=c_brand
        self.price=c_price
        self.name=c_name
        self.wheel=2

    def running(self):
         print(f"{self.brand}{self.name}正在高速行驶中.....")

    def total_coat(self,discount,rate=0.1):

        total_cost=self.price*discount+rate*self.price
        return total_cost

    # 测试
c1 = Car("红色", "宝马", "BMW", 800000)
print(c1.wheel)
#通过实例对象，查找属性时，会先查找实例属性，实例属性不存在，再查找类属性

#通过类名访问类属性
print(Car.wheel)

# c2 = Car("红色", "宝马", "BMW", 1800000)
# print(c2)