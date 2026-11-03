#函数的参数类型
# #加
# def add(x,y):
#     return x+y
#
# #减
# def subtract(x,y):
#     return x-y
#
# #乘
# def multiply(x,y):
#     return x*y
#
# #除
# def divide(x,y):
#     return x/y
#
#
# #计算
# def calc(x,y,oper):
#     return oper(x,y)
#
# print(calc(10,20,add))



#
# #匿名函数  lambda 参数列表:函数体
# #需求一：打印一个分割线
# out_line=lambda :print("---------------------------")
# out_line()
#
#
# #需求二：打印两个数之和
#
# add=lambda x,y:x+y
# print(add(1,2))
#
#
# #需求三：按照每一个元素的字符个数，从小到大排序
# data_list=["c++","c#","go","python"]
# print(data_list)
#
# data_list.sort()
#
# print(data_list)
#
# #匿名函数典型的应用场景
# data_list.sort(key=lambda item:len(item))
# print(data_list)
#
#
#
#




#案例：计算n的阶乘
#递归调用：指的是在函数中自己调用自己的情况-->一定要有终结点
"""
jc(10)=10*jc(9)
jc(9)=9*jc(8)
jc(8)=8*jc(7)
jc(7)=7*jc(6))

"""

def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)

n=jc(3)
print(n)













