


"""
路径写法
1、相对路径：从当前文件出发，找到目标文件所要经过的路径，从左到右，一级一级的写，每级之间用/连接
2、绝对路径：从根目录开始，找到目标文件所要经过的路径，从左到右，一级一级的写，每级之间用/连接
3、.表示当前目录
4、..表示上一级目录（可以叠代写法，表示多级目录）
5、/表示根目录



"""














# #读取文件
#
# #1、打开文件
# f = open("./01文件操作基础练习.txt","r",encoding="utf-8")
#
#
# #2、读取文件内容
# # content=f.read()#读取文件全部内容
# # print(content)
#
# content_list=f.readlines()#readlines()读取文件全部内容，返回一个列表,readline()只读取文件一行内容
# for line in content_list:
#     print(line.strip())
#
# #3、关闭文件
#
# f.close()





#--------------释放资源正确的操作方式------------------------
#try...finally...语句
# #写入文件
#
# #1、打开文件
# f = open("./001文件练习收藏/静夜思.txt","w",encoding="utf-8")
#
# #2、写入文件内容
# try:
#     f.write("静夜思\n\n")
#     f.write("床前明月光，疑是地上霜。\n")
#     f.write("举头望明月，低头思故乡。\n")
#
# finally:
# #3、关闭文件
#     f.close()




#（做项目时最佳推荐方式）
#方式二:with语句
with open("./001文件练习收藏/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思\n\n")
    f.write("床前明月光，疑是地上霜。\n")
    f.write("举头望明月，低头思故乡。\n")

