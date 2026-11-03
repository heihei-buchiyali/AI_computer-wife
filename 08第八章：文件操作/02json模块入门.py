import json


#写入json数据文件
user={
    "name":"张三",
    "age":18,
    "sex":"男",
    "hobbies":["抽烟","喝酒","烫头"]
}

with open("001文件练习收藏/user.json","w",encoding="utf-8") as f:
    json.dump(user,f,ensure_ascii=False,indent=4)

#ensure_ascii=False:会在输出的json数据中保留中文字符
#indent:会在输出的json数据中添加缩进（格式化），使json数据更易读

#读取json数据文件
with open("001文件练习收藏/user.json","r",encoding="utf-8") as f:
    user=json.load(f)
    print(user)













