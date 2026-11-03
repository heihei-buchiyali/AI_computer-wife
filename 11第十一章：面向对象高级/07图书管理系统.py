"""

基于面向对象的编程思想完成如下系统开发

某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。
系统中有两种类型的会员：普通会员和 VIP 会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。

核心功能：

1.会员登录：会员通过卡号和密码登录系统
2.借书：会员可以借阅库存中有余量的图书
3.还书：会员可以归还借阅的图书
4.查看我的借阅：展示当前会员已经借阅的图书列表
5.退出系统

借阅规则：

1.普通会员最多可借 3 本
2、VIP 会员最多可借 6+VIP 等级 本（VIP 等级，默认为 1）

注意：

1.登录成功（卡号和密码均正确）后，才可以访问该系统
2.图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

"""
import json
import os


#书籍类
class book():
    def __init__(self,BookId,BookName,Author,BookNumber):
        self.BookId=BookId          #书编号
        self.BookName=BookName      #书名
        self.Author=Author          #作者
        self.BookNumber=BookNumber  #书数量
        self.__RemainingNumber=BookNumber  #书剩余数量



    #借书
    def BorrowBook(self):
        if self.__RemainingNumber>0:
            self.__RemainingNumber-=1
            return True
        return False


    #还书
    def ReturnBook(self):
        self.__RemainingNumber+=1


    #获取可用数量
    def AvailableNumber(self):
        return self.__RemainingNumber



#会员类
class VipPerson():
    def __init__(self,PersonID,PersonName,PersonPassword,PersonType):
        self.PersonID=PersonID              #会员卡号
        self.PersonName=PersonName          #会员姓名
        self.PersonPassword=PersonPassword  #会员密码
        self.PersonType=PersonType          #会员类型
        self.BorrowBooks=[]                 #已借阅的图书列表


    #最大可借阅数量
    def MaxBooksNumber(self):
        return 6+self.PersonType


    #借书
    def BorrowBook(self,book):
        if len(self.BorrowBooks)<self.MaxBooksNumber():
            self.BorrowBooks.append(book)

            #输出借书成功信息
            print(f"{self.PersonName}成功借阅《{book.BookName}》,请您按时归还")
            return True
        elif len(self.BorrowBooks)>=self.MaxBooksNumber():
            print(f"不好意思{self.PersonName}，您已达到最大借书数量，请归还图书后再借新书")
            return False
        else:
            print(f"《{book.BookName}》库存不足，当前无法借阅")
            return False


    #还书
    def ReturnBook(self,book):
        if book in self.BorrowBooks:
            self.BorrowBooks.remove(book)

            #输出还书成功信息
            print(f"{self.PersonName}成功归还《{book.BookName}》")
            return True
        else:
            print(f"不好意思{self.PersonName}，您未借阅过《{book.BookName}》")
            return False

    #查看我的借阅
    def MyBorrowBooks(self):
        if len(self.BorrowBooks)==0:
            print(f"{self.PersonName}当前没有借阅任何图书")
            return
        else:
            print(f"{self.PersonName}已借阅的图书有：")
            for book in self.BorrowBooks:
                print(f"编号：{book.BookId}，书名：{book.BookName}，(作者：{book.Author})")


#超级会员类
class SuperVipPerson(VipPerson):
    def __init__(self,PersonID,PersonName,PersonPassword,PersonType):
        super().__init__(PersonID,PersonName,PersonPassword,PersonType)

    def MaxBooksNumber(self):
        return 6+self.PersonType



# 管理类
class LibraryManager:
    def __init__(self, books_file="library/books.json", vip_file="library/VipPerson.json"):
        self.books_file = books_file
        self.vip_file = vip_file
        self.books = []           # 存储所有书籍对象
        self.vip_persons = []     # 存储所有会员对象
        self.current_user = None  # 当前登录的会员
        self.load_data()          # 初始化时加载数据

    # 加载数据
    def load_data(self):
        # 加载书籍数据
        with open(self.books_file, "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for item in books_data:
                b = book(item["编号"], item["名称"], item["作者"], item["数量"])
                self.books.append(b)

        # 加载会员数据
        with open(self.vip_file, "r", encoding="utf-8") as f:
            vip_data = json.load(f)
            for item in vip_data:
                vp = VipPerson(item["卡号"], item["姓名"], item["会员密码"], item["会员等级"])
                self.vip_persons.append(vp)

    # 登录验证
    def login(self):
        print("=" * 50)
        print("欢迎使用图书馆管理系统")
        card_id = input("请输入您的卡号：")
        password = input("请输入您的密码：")

        for person in self.vip_persons:
            if person.PersonID == card_id and person.PersonPassword == password:
                self.current_user = person
                print(f"登录成功！欢迎您，{person.PersonName}")
                return True

        print("卡号或密码错误，请重新输入")
        return False

    # 根据书名查找书籍
    def find_book(self, book_name):
        for b in self.books:
            if b.BookName == book_name:
                return b
        return None

    # 借书功能
    def borrow_book(self):
        print("\n--- 借书 ---")
        self.show_books()
        book_name = input("请输入要借阅的图书名称：")

        target_book = self.find_book(book_name)
        if target_book is None:
            print(f"未找到《{book_name}》")
            return

        # 检查库存
        if target_book.AvailableNumber() <= 0:
            print(f"《{book_name}》库存不足，无法借阅")
            return

        # 会员借书
        if self.current_user.BorrowBook(target_book):
            target_book.BorrowBook()  # 减少库存

    # 还书功能
    def return_book(self):
        print("\n--- 还书 ---")
        if len(self.current_user.BorrowBooks) == 0:
            print("您当前没有借阅任何图书")
            return

        self.show_my_borrowed()
        book_name = input("请输入要归还的图书名称：")

        target_book = self.find_book(book_name)
        if target_book is None:
            print(f"未找到《{book_name}》")
            return

        if self.current_user.ReturnBook(target_book):
            target_book.ReturnBook()  # 增加库存

    # 查看我的借阅
    def show_my_borrowed(self):
        print("\n--- 我的借阅 ---")
        self.current_user.MyBorrowBooks()

    # 显示所有书籍
    def show_books(self):
        print("\n--- 图书列表 ---")
        for b in self.books:
            print(f"编号：{b.BookId}，书名：{b.BookName}，作者：{b.Author}，库存：{b.AvailableNumber()}")

    # 主菜单
    def run(self):
        while True:
            if not self.login():
                continue

            while True:
                print("\n" + "=" * 30)
                print(f"当前用户：{self.current_user.PersonName}（VIP等级：{self.current_user.PersonType}）")
                print(f"最大可借：{self.current_user.MaxBooksNumber()} 本")
                print("1. 查看所有图书")
                print("2. 借书")
                print("3. 还书")
                print("4. 查看我的借阅")
                print("5. 退出登录")
                print("0. 退出系统")

                choice = input("请选择操作：")

                if choice == "1":
                    self.show_books()
                elif choice == "2":
                    self.borrow_book()
                elif choice == "3":
                    self.return_book()
                elif choice == "4":
                    self.show_my_borrowed()
                elif choice == "5":
                    self.current_user = None
                    print("已退出登录")
                    break
                elif choice == "0":
                    print("感谢使用，再见！")
                    return
                else:
                    print("无效选择，请重新输入")


# 程序入口
if __name__ == "__main__":
    manager = LibraryManager()
    manager.run()












