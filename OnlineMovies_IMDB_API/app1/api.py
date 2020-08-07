import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"game of thr"}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "0dda550f8amsh68e8fe83be9fac7p14b386jsnd638f08daff6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)