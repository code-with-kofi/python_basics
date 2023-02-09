opr1=0
opr2=0
operator=0
again = "y"
while again == "y":
    try:
        
        print("\n\n\n\n")
        opr1 = int (input("\nenter first value : "))
        
        opr2 = int (input("\nenter second value : "))

        operator = int (input("\nenter \n1. to add \n2. to minus \n3 to multiply \n4 to divide \n5 modulo \n6 exponitial \n  >>> "))
        
        

        print("result : ")
        if(operator == 1 ):
            print(opr1+opr2)

        elif(operator == 2 ):
            print(opr1-opr2)

        elif(operator == 3 ):
            print(opr1*opr2)

        elif(operator == 4 ):
            print(opr1/opr2)
        elif(operator ==5):
            print(opr1%opr2)
        elif(operator==6):
            print(opr1**opr2)
        else:
            print("please enter correct value")

        print("do you want to continue ? or press -1 to exit")
        again =input()
        if again == -1:
            print("Quiting.....")
            break
    except:
        input(" you have enter a wrong value press any key to break")
        break







  