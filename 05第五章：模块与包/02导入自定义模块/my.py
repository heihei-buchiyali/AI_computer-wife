# #导入自定义的模块
# import mine
#
#
# #使用模块中的功能
# print(mine.PI)
# print(mine.log_separator1())
# print(mine.NAME)




#导入自定义的模块中的功能
#from mine import log_separator1,log_separator2,PI,NAME
from mine import *
# * 是导入模块中的所有功能，当导入的*模块中有__all__时
#代表只能导入__all__中的所有功能



#使用模块中的功能

print(PI)
print(NAME)
log_separator1()
log_separator2()
