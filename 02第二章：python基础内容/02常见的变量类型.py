# 常见数据类型
# ---------type()获取指定的字面量或变量的类型
print("hello world")
print(type("hello world"))
print(type(10)) #int
print(type(3.14)) #float
print(type(True)) #bool
print(type(False)) #bool
print(type(None)) #Nonetype

num=-100
print(type(num)) #int



# ------------> isinstance(数据,类型)--->bool值-->绑定数据是否是指定的类型
# 如果是:True,否则:False
print(isinstance(num,int)) #True
print(isinstance(num,float)) #False
print(isinstance(num,bool)) #False


#字符串
#定义字符串的三种方式
s1=("hello") #双引号定义

s2=('hello') #单引号定义

s3=("""
hello
欢迎大家学习
""") #三引号定义（多行字符串）

#转义字符 \'(单引号)  \"（双引号）  \n(换行符)  \t(制表符)


#字符串的拼接  #str(int数字)------>将int类型的数字转化为字符串
a1="生的再平凡" "," "也是限量版"
print(a1)

a2="生的再平凡"
a3="也是限量版"
print("俗话说："+a2+"，"+a3)


#字符串格式化---> 方式一 %s 占位符
a2="生的再平凡"
a3="也是限量版"
print("俗话说：%s，%s" %(a2,a3))

# 方式二  通过f"内容{变量\表达式} 来完成格式化
a2="生的再平凡"
a3="也是限量版"
print(f"俗话说的好：{a2},{a3}")
