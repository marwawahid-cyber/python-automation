a = int(input("enter the a number:"))
b = int(input("enter the b number:"))
c = int(input("enter the c number:"))

if a > b:
    if a > c:
        print(f"a is big a={a}")
    else:
        print(f"c is big c={c}")
else:
    if b > c:
        print(f"b is big b={b}")
    else:
        print(f"c is big c={c}")
        