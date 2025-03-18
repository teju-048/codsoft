while True:
    print("Choose an option from below:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    operation=int(input("Enter your choice:"))
    if operation==5:
        print("Exiting")
        break
    else:
        print("Enter two nubers:")
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if(operation in [1,2,3,4,]):
            if operation==1:
                result=num1+num2
                print("Sum:",result)
            elif operation==2:
                result=num1-num2
                print("Difference:",result)
            elif operation==3:
                result=num1*num2
                print("Product:",result)
            elif operation==4:
                if num2!=0:
                    result=num1/num2
                    print("Quotient:",result)
                else:
                    print("Cannot divide by zero")
        else:
            print("Invalid choice")