#函数定义:函数定义的时候并不会执行，只有在调用函数的时候，函数体的逻辑才会执行
#函数必须先定义后调用
# def out_line():
#     print("---------------------------------------")
#     print("----------------------------------------")
#
#
# #函数调用
# out_line()

#
#
#
#
# #函数的参数和返回值
# #如果返回值有多个，用逗号分离
# #函数1：计算圆的面积
# def ciecle_area(r):
#     area=r*r*3.14
#     return area
#
# area=ciecle_area(10)
#
# print(area)
#
# #函数2：计算长方形的面积----->长，宽
# def rectangle_area(l,d):
#     area=l*d
#     return area
# area=rectangle_area(10,20)
# print(area)





#--------------------函数嵌套调用--------------------

# def function_a():
#     print("a-----before")
#     function_b()
#     print("a-----after")
#
# def function_b():
#     print("b-----before")
#     function_c()
#     print("b-----after")
# def function_c():
#     print("c-----")
#
# function_a()
#
#
# print("函数调用完毕")


#
# #案例一：定义一个函数：根据传入的底和高计算三角形面积的函数
# def sanjiao(d,h):
#     area=d*h/2
#     return area
# print(sanjiao(float(input("请输入三角形的底")),float(input("请输入三角形的高"))))
#
#
#
# #案例二：计算传入的字符串中元音字母的个数
#
# def zifuchuan():
#     num=0
#     a=str(input("请输入一串字符："))
#     for i in a :
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#           num =  num + 1
#         elif i == "A"or i == "E"or i == "I" or i == "O" or i == "U":
#             num = num + 1
#     return num
# zfc = zifuchuan()
# print(f"元音字母的个数为：{zfc}")

#案例三：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分

def calc_score(score_list):
    max_s=max(score_list)
    min_s=min(score_list)
    avg_s=round(sum(score_list)/len(score_list),1)
    return max_s,min_s,avg_s

s_list=[686,676,578,645,555,666,566]
max_s,min_s,avg_s=calc_score(s_list)
print(f"最高分：{max_s},"
      f"最低分：{min_s},"
      f"平均分：{avg_s}")

