#for循环：遍历输入字符串

# a= "worthiness"
# for i in a:
#     print(i)
# else:
#     print("循环结束")
#
#案例  计算1——100之间所有奇数之和

# num1=0
# for i in range(1,101):
#     if i%2==1:
#         num1+=i
#
# print(num1)
#
# #案例二   计算100——500之间所有3的倍数的数字之和
#
# num2=0
# for i in range(100,500):
#       if i%3==0:
#         num2+=i
# print(num2)


#
# #打印一个10*5的*图
# m=int(input("请输入长方形的长："))
# n=int(input("请输入长方形的宽："))
#
# for j in range(n):
#     for i in range(m):
#         print("*",end=" ")
#     print()


#
# #嵌套循环案例：打印9x9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j} x {i} = {i*j }',end='\t')
#     print()
#
#

# import os
# #清屏函数
# def clear():
#     os.system("cls")
#
# #综合案例：用户名密码登录
# while True:
#     clear()
#     yhm=str(input("请输入您的用户名："))
#     mm=str(input("请输入您的密码"))
#
#     if yhm=="admin" and mm=="666888" or yhm=="zhangsan" and mm=="123456" or yhm=="taoge" and mm=="888666":
#         print("登陆成功，进入B站首页~")
#         break
#     elif yhm=="" or mm=="":
#         print("输入的用户名或密码不能为空，请重新输入")
#     else:
#         print("用户名或密码错误，请重新输入")
#
#

#
# #案例 猜数字
#
# import random
# a=random.randint(1,100)
#
# while True:
#     b = int(input("请输入一个数字："))
#     if a==b:
#         print("恭喜你答对了")
#         break
#     elif a>b:
#         print("不好意思猜小了")
#     else :
#         print("不好意思，猜大了")
#


#统计字符串“adrgkrdgaadgrkadgkdgdadgkfdba”字符串中有多少a和k
num=0
num1=0
zfc="adrgkrdgaadgrkadgkdgdadgkfdba"
for i in zfc:
    if i=="a":
        num=num+1
    elif i=="k":
        num1=num1+1
print(num,num1)








