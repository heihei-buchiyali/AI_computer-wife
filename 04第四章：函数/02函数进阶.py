#-------------------------函数-变量的作用域-------------------------
#全局变量：在函数外部还是内部都可以使用
# num=100
#
# #定义函数
# def circle_area(r):
#     pi=3.14       #局部变量：只能在内部使用
#     area=pi*r**2
#     global num   #global将局部变量改为全局变量
#     num=100000
#     return area
#
# #调用函数
# c_area=circle_area(10)
# print(c_area)



#---------------------------函数--传参方式---------------------------------
#定义函数
# def reg_stu(name,age,gender,city):
# 	print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
# 	return{"name":name,"age":age,"gender":gender,"city":city}
#
# #传参方式一：位置参数
# stu=reg_stu("张三",18,"男","北京")
# print(stu)
#
# #传参方式二：关键字传参
# stu=reg_stu(age=28,name="王琳",city="上海",gender="女")
# print(stu)
#
# #传参方式三：位置参数+关键字传参------>位置参数在前，关键字参数在后，顺序不可变
# stu=reg_stu("李华",30,city="深圳",gender="男")
# print(stu)




#---------------------------函数--默认参数-----------------------------------------
# def reg_stu(name,age,gender="女",city="南京"):
# 	print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
# 	return{"name":name,"age":age,"gender":gender,"city":city}
#
# stu=reg_stu("张三",18,"男","北京")
# print(stu)
#
# stu=reg_stu("李四",30)
# print(stu)



#-------------------------函数--不定长参数（位置参数*args---->元组）--------------------------------------
#需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, avg_data
#
#
# #调用函数
# min_data, max_data, avg_data = calc_data(1, 2, 3, 4,5,6,7,8,9)
# print(min_data, max_data, avg_data)



#-------------------------函数--不定长参数（关键字参数**kwargs---->字典）-----------------------------------------

def calc_data(*args,**kwargs):
    """
    根据传入的这批数据计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
    :round:保留的小数位个数
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round")is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值：{min_data},最大值{max_data},平均值{avg_data}")

    return min_data, max_data, round(avg_data,1)


#调用函数

print(calc_data(1, 2, 3, 4,5,6,7,8,9,round=3,print=True))























