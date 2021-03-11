from zeep import Client

# Run below command in terminal
# python -mzeep http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL

client = Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")

print(client.service.CapitalCity("IN"))

lst = client.service.ListOfCountryNamesByCode()

for item in lst:
    if item['sName'] == 'India':
        print(item['sISOCode'])