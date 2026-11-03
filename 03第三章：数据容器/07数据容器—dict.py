#字典---->key不能重复(如果重复，后边的值会覆盖前面的值)、key必须是不可变类型(str,int,float)
#定义字典----->（key,value）----->key是唯一的，可修改
#字典是没有索引下标的，不能根据索引获取值，只可以根据key获取value
dic1={"王琳":670,"许力强":666,"刘星":567,"张思":674}

print(dic1)


#访问
print(dic1["王琳"])

dic1["王琳"]=888
print(dic1["王琳"])

#-------------字典的常规操作--------------------

a={"小智":688,"小王":654,"无归":567,"张三":587,"王五":625}



#添加--> 字典名称[key]=value
#往指定字典中添加key-value键值对
a["涛哥"]=565
print(a)


#删除-->字典名称.pop[key] 或者 del 字典名称[key]
#删除字典中指定的key，并返回该key对应的value
score=a.pop("小智")

del a["小王"]
print(a)

#修改-->字典名称[key]=value
#修改字典中指定的key对应的值
a["无归"]=666
print(a)


#查询-->字典名称[key]        根据key获取value
var = a["王五"]
print(var)

#      字典名称.get(key)    根据key获取value
a.get("涛哥")
print(a.get("王五"))

#      字典名称.keys()      获取所有key
a.keys()
print(a.keys())

#      字典名称.values()    获取所有value\
a.values()
print(a.values())

#      字典名称.items()     获取所有的key-value键值对
a.items()
print(a.items())












