# if条件判断：如果分数超过680，我就去上清华

score=float(input("请输入你的高考分数："))
if 680 <= score <= 750:
    print("恭喜你考入清华大学")
if score < 680:
    print("不好意思您与清华失之交臂")
if score > 750:
    print("滚你丫的会不会好好输")


#if....else...条件判断
zhanghao=int(input("请输入您的账号："))
mima=int(input("请输入您的密码："))

if zhanghao==1888888 and mima==666666 :
        print("登录成功")
else :
    print("账号或密码不正确")


#if...elif...else 条件判断

num=float(input("请输入一个数："))
if num>0:
    print("此数是正数")
elif num<0:
    print("此数为负数")
else:
    print("这个数是0")


#案例判断三角形是什么三角形
a=float(input("请输入三角形边长："))
b=float(input("请输入三角形边长："))
c=float(input("请输入三角形边长："))

if (a+b>c and a+c>b and b+c>a) and a==b==c:
    print("此三角形为等边三角形")
elif  (a+b>c and a+c>b and b+c>a) and a==b or b==c or c==a:
    print("此三角形为等腰三角形")
elif  a+b>c and a+c>b and b+c>a:
    print("此三角形为普通三角形")
else :
    print("这个图形不能构成三角形")


