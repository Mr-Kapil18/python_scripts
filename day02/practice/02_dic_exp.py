info = {
    "name" : "Kapil", #str
    "city" : "Mumbai",
    "age" : 28, #int
    "education" : "BE",
    "salary" : 22.5, #float
    "Married" : False, #Boolean
    "favourites" : ["teaching","movies", 18 ], #list
}

print ("i live in",info["city"])
print("i love ", info.get("favourites"))


#when u want to update the above data use update

info.update({"car": "Virtus"})

print (info)
#iterate a dictionary
for key,value in info.items():
    print(key,value)