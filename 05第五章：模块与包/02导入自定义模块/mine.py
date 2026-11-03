#__all__指定from...import * 导入的是那些功能
__all__ = ['log_separator1', 'log_separator2',"PI","NAME"]



#自定义模块

#常量（不会变化的数据；常量的名称全部大写）
PI=3.1415926
NAME = "河南彭于晏"


def log_separator1():
    print("-"*30)

def log_separator2():
    print("+"*30)

def log_separator3():
    print("#"*30)

def log_separator4():
    print("*"*30)



#调用函数
#__name__:Python中内置变量，表示的当前模块的名字
#（直接运行当前模块，__name__的值为"__main__";
# 当该模块被导入时，__name__的值就是模块名称）

#执行当前文件，则会执行如下代码；如果被当做模块导入，如下代码不执行
if __name__ == '__main__':
    log_separator1()