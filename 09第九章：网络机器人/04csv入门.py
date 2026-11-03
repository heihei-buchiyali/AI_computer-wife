#csv操作—— 方式一：文件操作原始方式
#写

# with open("cas_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,年龄,性别,爱好\n")
#     f.write("小王,18,男,Python\n")
#     f.write("小李,19,女,化学\n")
#     f.write("小张,20,男,Java\n")
#     f.write("小赵,21,女,Python\n")
#



#
# #读
# with open("cas_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())



#csv操作——方式二：csv
import csv
from os import write

with open ("cas_data/02.csv","w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()#写入表头
    writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"Python"})
    writer.writerow({"姓名":"小李","年龄":19,"性别":"女","爱好":"化学"})
    writer.writerow({"姓名":"小张","年龄":20,"性别":"男","爱好":"Java"})
    writer.writerow({"姓名":"小赵","年龄":21,"性别":"女","爱好":"Python"})







