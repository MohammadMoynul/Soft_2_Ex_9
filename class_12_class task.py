import json
import requests
keyword = input("Enter the country name:")
request = "https://restcountries.com/v3.1/name/" + keyword
response = requests.get(request).json()

try:
    response = requests.get(request)

    if response.status_code==200:
        json_response = response.json()
        if len(json_response)==0:
            print(f"No countries exist with name: {keyword}")
        else:
            #country name
            #capital city
            #population

            for country in json_response:
            name = country["name"]["common"]
            capital = country["capital"][0]
            population = country["population"]

            print("\n--- country found ---")
            print(f"country : {name}")
            print(f"capital : {country}")
            print(f"population : {population}")

    else:
    print(f"Error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Request could not completed.")
