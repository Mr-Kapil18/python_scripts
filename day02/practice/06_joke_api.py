import requests
api_url = "https://official-joke-api.appspot.com/random_joke"

def get_jokes():
    joke=requests.get(url=api_url)
    final_joke = joke.json()["setup"] + joke.json()["punchline"]
    return final_joke

final_joke= get_jokes()

print (final_joke)