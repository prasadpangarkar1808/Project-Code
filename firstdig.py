no=int(input("Enter a Number = "))
if no<100:
    first_no=no//10
    print(first_no)
    second_no=no%10
    print(second_no)
elif no<1000:
    first_no=no//100
    print(first_no)
    second_no=no%100
    print(second_no)
elif no>=1000:
    first_no=no//1000
    print(first_no)
    second_no=no%1000
    print(second_no)