#1、导入模块--->调用方式：模块名.功能名/别名.功能名
# #import random as 别名   别名只是方便记忆，可加可不加
# import random as rd
# for i in range(100):
#     print(rd.randint(1,100))


#2、导入模块中的功能 from...import...---->调用方式：功能名/别名
#from random import randint
from random import randint as rint
#已经起了别名调用的时候就要用别名调用
for i in range(100):
    print(rint(1,100))