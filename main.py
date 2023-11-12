print("Available options:\n1.a+b\n2.a-b\n3.a*b\n4.a/b\n5.Fibonacci number\n6.Exit")
s = input("Enter option ")

if s == '1':
     print("1.a+b")
     a = int(input("a = "))
     b = int(input("b = "))
     c=a+b
     print("Answer a+b=",c)
elif s == '2':
    print("2.a-c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = a - b
    print("Answer a-b=", c)
elif s == '3':
        print("3.a*b")
        a = int(input("a = "))
        b = int(input("b = "))
        c = a * b
        print("Answer a*b=", c)
elif s == '4':
        print("4.a/b")
        a = int(input("a = "))
        b = int(input("b = "))
        c = a / b
        print("Answer a/b=", c)
elif s == '5':
        print("5.Fibbonachi number")
        f1, f2 = 1, 1
        n = int(input())
        print(f1, f2, end=' ')
        while n > 2:
            f1, f2 = f2, f1 + f2
            print(f2, end=' ')
            n -= 1
elif s == '6':
        print("Thanks")



