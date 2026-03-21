choice = input ("enter the choice (press q to quit): ")

while choice != "q":
    num = int (input ("enter the number u want table for "))
#for i in range (10):
#        print(num * i)

# string formating "f"
    for i in range (1,13):
        print (f" {num} x {i} = {num * i} ")

    choice = input ("enter the choice (press q to quit): ")   