#开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能
#系统使用字典结构存储商品数据，通过控制台与用户交互，具体功能如下：
#1、添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存到购物车
#2、修改购物车：要求用户输入要修改的购物车商品名称、然后再提示商品的价格数量，输入完成后修改该商品信息
#3、删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品
#4、查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格xxx，商品数量：xxx”
#5、退出购物车


import os,time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

name={}

while True:
 clear()
 print("##########购物车系统###########")
 print("#         1、添加购物车        #")
 print("#         2、修改购物车        #")
 print("#         3、删除购物车        #")
 print("#         4、查询购物车        #")
 print("#         5、退出购物车        #")
 print("#############################")


 chance=input("请输入您的选择(1~5)")

 match chance:
    case "1":#添加购物车
       names=input("请输入商品名称：")
       money=float(input("请输入商品价格："))
       num=int(input("请输入商品数量："))
       name[names]={money:num}



    case "2":#修改购物车
#字典名称[key]=value
      names=input("请输入需要修改的商品：")
      #判断商品在字典中是否存在
      if names in name:
        money=float(input("请输入新的商品价格："))
        num=int(input("请输入新的商品数量："))
        name[names] = {money: num}
        print("修改成功")

      else:
          print("该商品不存在，请重新输入")

    case "3":#删除购物车
      names = input("请输入需要删除的商品：")
      # 判断商品在字典中是否存在
      if names in name:
        del name[names]
        print("已成功删除")


    case "4":#查询购物车
      name.items()
      print(name.items())


    case "5":#退出购物车
        print("已成功退出购物车系统")
        break
    case _:
     print("输入错误，请重新输入")

