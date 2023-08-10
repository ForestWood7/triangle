def is_valid(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = int(input("第一条边："))
b = int(input("第二条边："))
c = int(input("第三条边："))
if is_valid(a, b, c):
    print("可以构成")
else:
    print("不能构成")