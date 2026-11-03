#变量定义 — 指定类型注解
import math


# a2:int=596
# score2:float=96.3
# hobby2:str="python"
# flag2:bool=True
# pic2:None=None
#
# names2:list[str]=["A","B","C","D","E"]
# phones2:set[str]={"123456","456789","987654"}
# options2:dict[str,int]={"count":1,"total":2}
# goods2:tuple[str,int,int]=("手机",6999,2)
#
# names2.append("F")
# print(names2)







#函数类型注解
def circle_area_len(r:float):
    return round(3.14*r*r,1),round(3.14*r,1)

al=circle_area_len(20)
print(al)
