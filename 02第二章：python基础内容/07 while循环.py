# #while循环：一句话打印十遍
#
# i=1
# while i<=10:
#     i+=1
#     print("我是你爹")
# else:
#     print("打印结束，退出循环")


#计算1--100之间所有的偶数的累加之和
a=0
i=1
while i<=100:
    if i%2==0:
        a+=i
    i+=1
print(a)