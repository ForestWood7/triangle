a = int(input("请输入第一条边："))
b = int(input("请输入第二条边："))
c = int(input("请输入第三条边："))
3
if a + b <= c:
    print("不能构成")
elif b + c <= a:
    print("不能构成")
elif a + c <= b:
    print("不能构成")
else:
    print("可以构成")
