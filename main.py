opr1=0
opr2=0
operator=0
again = "y"
while again == "y":
    try:
        print("\n\n\n\n")
        opr1 = int (input("\nenter first value : "))
        
        opr2 = int (input("\nenter second value : "))

        operator = int (input("\nenter \n1. to add \n2. to minus \n3 to multiply \n4 to divide \n  >>> "))

        print("result : ")
        if(operator == 1 ):
            print(opr1+opr2)

        elif(operator == 2 ):
            print(opr1-opr2)

        elif(operator == 3 ):
            print(opr1*opr2)

        elif(operator == 4 ):
            print(opr1/opr2)
        else:
            print("please enter correct value")

        print("do you want to continue")
        again =input()
    except:
        input(" you have enter a wrong value press any key to break")
        break







  