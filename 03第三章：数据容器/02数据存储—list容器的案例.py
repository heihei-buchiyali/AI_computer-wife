#案例 将用户输入的十个数字存入列表中并进行排序，输出最小值、最大值和平均值

# #while循环版
# b=[]
# while True:
#     num=int(input("请输入数字，输入0停止："))
#     if num==0:
#         break
#     b.append(num)
# print("存入的数字",b)
#
# #排序
# b.sort()
#
# #算平均值--------sum()求和
# num1=0
# for i in b:
#     num1=num1+i
# pjz=num1/len(b)  #len获取元素的个数
#
# print("最小值为：",b[0],"最大值为",b[-1],"平均值为：",pjz)

# #for循环版
# a=[]
# for i in range(10):
#     z=int(input("请输入一个有效的数字："))
#     a.append(z)
#
# #排序
# a.sort()
#
# print("最小值：",a[0])
# print("最大值：",a[-1])
# print("平均值：",sum(a)/len(a))


#
# #案例二： 合并两个列表中的元素并进行去重处理
#
# a=[10,20,30,50,70,80,90]
# b=[20,40,50,60,100]
# c=[]
# #把a,b全部元素挨个加入c重复的不加
# for i in a+b:
#     if i not in c:
#         c.append(i)
# c.sort()
# print(c)


#案例三，生成一个1—20的平方列表

a=[]
for i in range(1,21):
    print(i**2)
    a.append(i)
print(a)
#方式二：列表推导式-->就是按照一定的规则快速生成一个列表的方法-->语法格式：[要插入的值 for i in 序列/列表]
d=[i**2 for i in range(1,21)]
print(d)

#从数字列表中提取所有偶数，并计算平方组成一个新的列表
b=[1,2,3,4,5,6,7,8,9,10]
c=[]
for i in b:
    if i%2==0:
      num=i**2
      c.append(num)
print(c)

#利用列表推导式解决第二个案例--->语法格式：[要插入的值 for i in 序列/列表 if条件]
e=[i**2 for i in b if i%2==0]
print(e)
