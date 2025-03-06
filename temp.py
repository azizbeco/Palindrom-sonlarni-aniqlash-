

def check(number):
    reverse_number=str(number)[::-1]

    if 0<number:
        if int(number) == int(reverse_number):
            print("True")
        else:
            print("False")
    else:
        print("False")



number =int(input("Enter a number \n>>>"))
check(number)





#   str(num)[::-1]