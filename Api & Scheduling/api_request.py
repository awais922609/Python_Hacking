import requests

url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"format":"json","code":"it"}

headers = {
	"x-rapidapi-key": "Sign Up for Key",
	"x-rapidapi-host": "covid-19-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())