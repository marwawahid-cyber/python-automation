a = int(input("enter the a number:"))
b = int(input("enter the b number:"))
c = int(input("enter the c number:"))

if a > b and a > c:
    print(f"a is big a={a}")
elif b > a and b > c:
    print(f"b is big b={b}")
else:
    print(f"c is big c={c}")
