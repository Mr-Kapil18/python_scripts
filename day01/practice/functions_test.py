def sum_of_num():      # Function definition
    num1 = int (input ("Enter num1: "))
    num2 = int (input ("Enter num2: "))

    sum = num1 + num2
    print (sum)

env = input ("Enter the environment ")
print ("the user input environment is ", env)

if env == "prod":
    sum_of_num()  # Function calling

#def take_backup():
#    print ("backup startedd....")

#    if day == "Monday":
#    take_backup()