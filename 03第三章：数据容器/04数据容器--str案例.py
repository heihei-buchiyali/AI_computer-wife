#邮箱格式验证：输入一个邮箱，验证是否正确（包含一个@和一个.）
#            输入正确，输出“邮箱格式正确”，否则反之


while True:
  email = input(str("请输入您的邮箱："))
  a = email.count("@")
  b = email.count(".")
  if a==1 and b>=1:
      print("邮箱格式正确")
      break
  else:
      print("邮箱格式错误请重新输入")

