a = [100,200,3.0,True]  # list 1st option
print (type (a))
a.append (500)
print (a)


clouds = list()        # List 2nd option
print (type (clouds))

clouds.append ("AWS")
clouds.append ("Azure")
clouds.append ("GCP")
clouds.append ("Alibaba")
clouds.append ("Utho")
print (clouds)

print ("length of cloud is: ",len (clouds))
print ("world leader for cloud service provider list is: ",clouds [0])
print ("indian cloud service provider: ", clouds [-1])

#print (dir(clouds))
print (clouds.count.__doc__)

# iterate a list
for cloud in clouds:
    if cloud == "AWS":
        print (f"{cloud} Market Leader")
    elif cloud == "Azure" or cloud == "GCP":
        print (f"{cloud} 2nd Leader")
    elif cloud == "Utho":
        print (f"{cloud} Indian Leader")
    else:
        print (f"{cloud} it is in dubai")


