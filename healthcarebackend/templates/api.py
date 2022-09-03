import requests

url = "https://priaid-symptom-checker-v1.p.rapidapi.com/body/locations/15"

querystring = {"language":"en-gb"}

headers = {
	"X-RapidAPI-Key": "5864663690msh5ece893f9fe231fp10ec05jsn009193f8dd78",
	"X-RapidAPI-Host": "priaid-symptom-checker-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)