# #定义类
#
# class Car:
#     pass
#
# #创建对象
#
# c1=Car()
#
# #动态的为对象添加属性
#
# c1.color="blue"
# c1.brand="BMW"
# c1.name="X5"
# c1.price=50000
#
# print(c1.color)
# print(c1.brand)
#
# print(c1.__dict__)#会将对象中的所有属性以字典的形式输出出来
#
#




#
# #类的定义
# #一般状态下上边的一般不用大部分用下边的
#
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     #self：是第一个参数，表示当前所创建出来的实例对象
#     def __init__(self,c_brand,c_name,c_price):
#         self.c_brand=c_brand
#         self.c_name=c_name
#         self.c_price=c_price
#
#
# #创建对象
# c1=Car("BWM","X5",500000)
# c2=Car("奔驰","A6",800000)
# print(c1.__dict__)
# print(c2.__dict__)
#





#---------------------定义类 实例方法---------------------------------
class Car:
    def __init__(self,c_color,c_name,c_brand,c_price):
        self.color=c_color
        self.brand=c_brand
        self.price=c_price
        self.name=c_name

        print("Car类型的对象初始化完毕，对象属性已经添加完毕")


#定义实例方法
    def running(self):
         print(f"{self.brand}{self.name}正在高速行驶中.....")

    def total_coat(self,discount,rate=0.1):
        """
    计算提车的总费用，包含两个部分：车的价格、税费
    :param self:
    :param discount:折扣
    :param rate:税率
    :return:提车的总费用
    """

        total_cost=self.price*discount+rate*self.price
        return total_cost


#测试
c1=Car("红色","宝马","BMW",800000)

#调试对象中的方法
c1.running()

total=c1.total_coat(0.9,0.1)
print("提车的总费用为",total)












