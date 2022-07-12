num1=int(input("enter the number"))
num2=int(input("enter the number"))
operator=input("enter the number")
if operator=="%":
    print("num1%num2")
elif operator=="+":
    print("num1+num")
elif operator=="-":
    print("num1-num2")
elif operator=="/":
    print("num1/num2")
elif operator=="*":
    print("num*num2")
elif operator=="**":
    print("num1**num2")
else:
    print("num1//num2")
