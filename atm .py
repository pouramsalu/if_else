print("welcome to SBI")
print("swipe yoir card")
pin=input ("enter the pin")
amount=600000
if pin:
    transaction="balance enquiry","withdraw money","deposit"
    print("chose your transaction")
    print("1 balance enquiry")
    print("2 withdraw money")
    print("3 deposit")
    print("4change your pin")
    print("5 transfer money")
    print("6 quit")
    trans =input("transaction")
    if trans=="balance enquiry":
        balance=input("enter the current or saving")
        if balance=="saving":
            print("your account balance is",amount)
        else:
            print("zero balance")
    elif trans=="withdraw money":
        amount=int(input("enter your money to proceed"))
        if amount<=600000:
            print("collect your cash! now your money amount,amount is left")
            print("thanks for visiting SBI")
    elif trans=="change your pin":
        change =input("enter new pin")
        if change=="change":
            print("your pin has been successfully change")
        else:
            print("enter a valid pin")
    elif trans=="transfer money":
        transfer=int(input("enter the amount"))
        if transfer<=300000:
            print("your transaction is successfully",amount-transfer,"is left in your account")
        else:
            print("enter valid amount for transaction")
    elif trans=="quit":
        quit=input("press yes to quit")
        if quit==("yes"):
            print("quit")
        else:
            print("choose any transaction please")
    else:
        print("wrong password")