##Application Programming Interface example. Open API from the FCC for mobile broadband spectrum use authorization, no api key required.
## Contributed by Github user @apistronaut  


##Import the libraries we need
import requests
import json

startfreq = input("Enter start of frequency range in MHz, minimum 225: ")
endfreq = input("Enter end of frequency range in MHz, maximum 3700: ")

##Make API Request to retrieve the user-entered frequencies.
response = requests.get(f"http://data.fcc.gov/api/spectrum-view/services/advancedSearch/getSpectrumBands?frequencyFrom={startfreq}&frequencyTo={endfreq}&pageNum=1&sortColumn=lowerBand&sortOrder=asc&pageSize=1000&limit=100&format=json")

##Extract the response data
content = response.text

##Convert to squashed JSON
uglycontent = json.loads(content)

##Prettify JSON
prettycontent = json.dumps(uglycontent, indent = 4)

print(prettycontent)
