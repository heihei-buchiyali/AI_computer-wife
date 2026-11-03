#导入包方式
#import 包名.模块名
#from 包名 import 模块名
#from 包名 import *   （要声明__all__变量）
#from 包名.模块名 import 功能名
#form 包名.模块名 import *


#1、导入模块
#
# import package.my
#
# package.my.log_separator1()
# package.my.log_separator2()
# package.my.log_separator3()


# from package import my
#
#
# my().log_separator1()
# my().log_separator2()
# my().log_separator3()

#注意：如果要通过 from package import* 导入包下的所有模块
#需要__init__.py文件中添加__all__

# from package import *
#
# my().log_separator1()
# my().log_separator2()
# my().log_separator3()
#
# print(myself.PI)
# print(myself.NAME)

#2、导入模块中的功能

from package.my import log_separator1,log_separator2

log_separator1()
log_separator2()
