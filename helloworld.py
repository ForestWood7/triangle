a = int(input("请输入第一条边："))
b = int(input("请输入第二条边："))
c = int(input("请输入第三条边："))

if a + b > c and b + c > a and a + c > b:
    print("可以构成三角形")
else:
    print("不可以构成三角形")
