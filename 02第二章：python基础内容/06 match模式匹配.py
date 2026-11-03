# #match...case... 模式匹配
# from unittest import case
#
# #工作日安排
# day=input("请输入星期几(1--7)：")
#
# match day:
#     case "1":
#         print("周一")
#     case "2":
#         print("周二")
#     case "3":
#         print("周三")
#     case "4":
#         print("周四")
#     case "5":
#         print("周五")
#     case "6" | "7":
#         print("周末")
#     case _:
#         print("输入有误请重新输入")
#

# #案例  计时器
# mun1=float(input("请输入数字："))
# nun2=float(input("请输入数字："))
# ysf=input("请输入运算符：")
#
# match ysf:
#     case "+":
#         num=mun1+nun2
#         print(num)
#     case "-":
#         num=mun1-nun2
#         print(num)
#     case "*":
#         num=mun1*nun2
#         print(num)
#     case "/":
#         num=mun1/nun2
#         print(num)
#     case _:
#         print("输入错误")
#

print("===== 游戏角色控制系统 =====")
#print("指令：上/w、下/s、左/a、右/d、跳/空格、攻击/j、退出/esc")
while True:
     # 获取玩家输入，去除首尾空格
     cmd = input("请输入指令：").strip()
     if cmd in ["上", "w", "W"]:
         print("角色向上移动")
     elif cmd in ["下", "s", "S"]:
         print("角色向下移动")
     elif cmd in ["左", "a", "A"]:
         print("角色向左移动")
     elif cmd in ["右", "d", "D"]:
         print("角色向右移动")
     elif cmd in ["跳", " "]:  # 空格
         print("角色跳跃")
     elif cmd in ["攻击", "j", "J"]:
         print("角色发动攻击")
     elif cmd in ["退出", "esc", "ESC"]:
         print("角色退出游戏，程序结束")
         break
     else:
         print("无效指令，请重新输入！")