x = int(input("Insert: "))
def calc(num):
    if  type(num) is not int:
        print ("Is not number")
    elif num % 3 == 0:
        print("True")
    else:
        print("False")
 #   else:
  #      print ("Incorrect type")
   #     x = input("Insert: ")
calc(x)
