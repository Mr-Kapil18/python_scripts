env = input ("Enter the environment ")
print ("the user input environment is ", env)

# conditional statement if else : is then in the below example
if env == "prod":
    print ("dont deploy on friday")
elif env == "stage":
    print ("do testing in the staging environment")
else:
    print ("safe to deploy today")

# == >= <= != 
# = assignment operator, == equality operator, === not in python but it is Javascript

# typecasting
# converting from one data type to another data type 
a = int (input ("Enter the num 1 "))
b = int (input ("Enter the num 2 "))
x = int (input ("enter ur login details "))
y = int (input ("enter the password "))
type (x)
c = a * b
d = a + b
e = a / b

print ("Multiplication is: ", c )
print ("Addition is: ", d )
print ("Dision is: ", e )
print ("login id is ", x )
print ("password is ", y)

