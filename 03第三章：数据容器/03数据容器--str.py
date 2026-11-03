# #字符串的基本操作---->不可变的（无法修改）
# a="hello world"
#
# print(a[4])#o  正向索引
# print(a[-7])#o  反向索引
#
#
# #切片操作
# print(a[0:5:1])#hello
# print(a[:5:1])
# print(a[:5:])
# print(a[:5])#hello
#
# #步长--->正数：从前往后截取负数反之
# print(a[5:0:-1])
# print(a[::-1])#反转字符串


#-------------------------字符串常用方法-----------------------------
s="Hello-Python-Hello-World"

#find()  查找指定字符串第一次出现的索引位置
index=s.find("-")
print(index)

#count()  统计字符串在指定字符串中出现的次数
c=s.count("o")
print(c)

#upper()  转为大写
su=s.upper()
print(su)

#lower()  转为小写
sl=s.lower()
print(sl)

#split()  将字符串按照指定字符串切割 -- 列表
ss=s.split("-")
print(ss)

#strip()  去除字符串两端的空格
x=s.strip()
print(x)

#replace()  将字符串中的指定字符串替换为新的内容
sr=s.replace("-","_")#(-old,_new)
print(sr)
#startswith()/endswith()  判断字符是否是以指定的字符串开头/结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))