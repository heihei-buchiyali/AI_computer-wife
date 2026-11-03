#异常处理
import mmap
try:
    print("---------------------------")

    print(mm)

    print("---------------------------")

except NameError as a:#捕获的是NameError 类型异常
    print("系统运行出错，异常信息：",a)
except Exception as c:#捕获所有的异常
    print("索引出错，错误信息:",c)

#无论程序是否正常运行，finally代码块的代码都会运行
finally:
    print("资源释放")