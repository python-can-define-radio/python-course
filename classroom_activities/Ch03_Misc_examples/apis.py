##Application Programming Interface example. Open API from the FCC for mobile broadband spectrum use authorization, no api key required.
## Contributed by Github user @apistronaut  



##Import the libraries we need
import requests
import json
import time

print("**NOTE**")
print("As of 2023 August 29, this API on the FCC website appears to be inaccessible.")
print("The code is still useful for demonstrating how to use APIs.")
print("")
time.sleep(3)

startfreq = input("Enter start of frequency range in MHz, minimum 225: ")
endfreq = input("Enter end of frequency range in MHz, maximum 3700: ")

##Make API Request to retrieve the user-entered frequencies.
response = requests.get(f"http://data.fcc.gov/api/spectrum-view/services/advancedSearch/getSpectrumBands?frequencyFrom={startfreq}&frequencyTo={endfreq}&pageNum=1&sortColumn=lowerBand&sortOrder=asc&pageSize=1000&limit=100&format=json")

##Extract the response data
content = response.text

print("Raw response content:")
print(content)

##Convert to squashed JSON
uglycontent = json.loads(content)

##Prettify JSON
prettycontent = json.dumps(uglycontent, indent = 4)

print("Prettified response content:")
print(prettycontent)
