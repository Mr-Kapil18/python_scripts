import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

#print(type(response.json()))

for key,value in response.json().items():
    if key == "completed":
        #if values == False:
         #   print("the data is not completed on server")
        if value in [1,2,3,4]:
            print("user found")