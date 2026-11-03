#集合 set ---->特点：无序，不可重复，可修改
#定义
s1={5,3,2,0,90,44,4,5,0}
print(s1)
#空集合
s2=set()


#集合set常用方法

a1={100,200,300,400,500,600}

#add()   添加元素到集合中
a1.add(700)
print(a1)

#remove()   移除集合中的指定元素（指定元素不存在将报错）
a1.remove(600)
print(a1)

#pop()   随机删除集合中的元素并返回
q=a1.pop()
print(q)
print(a1)

#clear()   清空集合
a1.clear()
print(a1)

#difference()   求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）
a2={"A","B","C","D","E"}
a3={"B","C","Y","X"}
print(a2.difference(a3) )
print(a3.difference(a2) )

#union()   求取两个集合的并集
print(a2.union(a3) )

#intersection()   求取两个集合的交集
print(a2.intersection(a3))
