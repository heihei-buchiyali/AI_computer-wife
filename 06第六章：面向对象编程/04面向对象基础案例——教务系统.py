"""
采用面向对象的思想,完成教务系统的开发可以管理在校学生的成绩信息
具体功能如下：
1、添加学生成绩：根据输入的学生姓名、语文、数学、英语成绩，记录在系统中
1.1、输入学生姓名、语文、数学、英语成绩
1.2、检查学生姓名是否已存在，如果学生不存在，再添加（存在则不添加）
1.3、验证成绩范围（0~100分）
1.4、创建学生对象并添加到系统中
2、修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
2.1、输入要修改的学生姓名
2.2、根据姓名查找该学生，显示该学生当前的学生成绩
2.3、输入新的学生语文、数学、英语成绩
2.4、更新学生成绩数据
3、删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4、查询指定的学生成绩：根据输入的学生姓名，查找对应的学生成绩并输出
4.1、输出格式为："姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
5、展示全部学生成绩：展示出系统中所有学生的成绩
"""


class Student:

    #学生姓名以及成绩的定义
    def __init__(self,z_name,z_Chinese,z_Math,z_English):
        self.name=z_name
        self.Chinese=z_Chinese
        self.Math=z_Math
        self.English=z_English

    #学生总分计算
    def z_score(self):
        return self.Chinese+self.Math+self.English

    #学生格式化输出
    def z_show(self):
        print(f"姓名：{self.name},语文成绩：{self.Chinese},数学成绩：{self.Math},英语成绩：{self.English}，总分：{self.z_score()}")




class GradeManager:

    def __init__(self):
# 用字典保存学生，key 是姓名，value 是 Student 对象
        self.students={}


    #添加学生成绩
    def add_student(self):
        name=input("请输入学生的姓名:")
        if name  in self.students:
            print("名字已存在了不能添加")
            return


        chinese=self.get_score("语文")
        math=self.get_score("数学")
        english=self.get_score("英语")

        student=Student(name,chinese,math,english)
        self.students[name]=student
        print("添加成功")


    #验证学生成绩是否符合逻辑
    def get_score(self,subject):
        while True:
            try:
                score=float(input(f"请输入{subject}成绩："))
            except ValueError:
                print("输入的成绩有误，请重新输入！")
                continue

            if 0<=score<=100:
                return score
            else:
                print("成绩必须在0~100以内，请重新输入！")



#修改学生成绩
    def modify_student(self):
        name = input("请输入需要修改的学生姓名：")
        if name not in self.students:
            print("不好意思没有找到该学生，请重新输入")
            return

        # 取出已有的学生对象
        student = self.students[name]

        # 显示当前学生成绩
        student.z_show()

        # 输入新成绩
        chinese = self.get_score("语文")
        math = self.get_score("数学")
        english = self.get_score("英语")

        # 新成绩覆盖旧成绩
        student.Chinese = chinese
        student.Math = math
        student.English = english

        print("修改成功")


#删除学生成绩

    def delete_student(self):
        name = input("请输入需要删除的学生姓名：")
        if name not in self.students:
            print("不好意思没有找到该学生，请重新输入")
            return

        del self.students[name]

        print("删除成功")

#查询指定的学生成绩
    def find_student(self):
        name = input("请输入需要查询的学生姓名：")
        if name not in self.students:
            print("不好意思没有找到该学生，请重新输入")
            return
        find = self.students[name]
        find.z_show()


#展示全部成绩
    def show_all(self):
        if not self.students:
            print("暂无学生数据")
            return

        for student in self.students.values():
            student.z_show()


#主菜单
    def main(self):
        while True:
            print("###########################")
            print("         教 务 系 统         ")
            print("#       1、添加学生成绩      #")
            print("#       2、修改学生成绩      #")
            print("#       3、删除学生成绩      #")
            print("#       4、查询学生成绩      #")
            print("#       5、展示全部成绩      #")
            print("###########################")

            chance = input("请选择所需要的功能编号：")
            if chance == "1":
                self.add_student()
            elif chance == "2":
                self.modify_student()
            elif chance == "3":
                self.delete_student()
            elif chance == "4":
                self.find_student()
            elif chance == "5":
                self.show_all()
            elif chance == "0":
                print("再见，欢迎下次使用")
                break
            else:
                print("输入错误请重新输入")



if __name__ == "__main__":
    manager = GradeManager()
    manager.main()
