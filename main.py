def main(): #main function
    #variables 
    opr1=0
    opr2=0
    operator=0
    again = "y"
    while again == "y": #validation
        try: # error and exception 

            print("\n\n\n\n")    # print new line
            opr1 = int (input("\nenter first value : "))   # input variables and also calling variable to assign to them
            validator(opr1)  
            opr2 = int (input("\nenter second value : "))
            validator(opr2)
            operator = int (input("\nenter \n1. to add \n2. to minus \n3 to multiply \n4 to divide \n5 modulo \n6 exponitial \n  >>> "))
            validator(opr2)
             # if statement for different calculation

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
 # exception if  is greater than one the leng 
        except Exception as e :
            if(len(e.args)>0):
               input(e.args[0])
               break
            else:# input to continue 
              validator(input(" you have enter a wrong value press any key to restart"))
              continue


def validator(value):
    if(value == -1):
         raise ValueError("You have chosen to exit the app") # function validator if is minus 1


main() # function to print