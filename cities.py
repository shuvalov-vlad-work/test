import os
from dotenv import load_dotenv 
from dadata import DadataAsync

load_dotenv() 

token = os.getenv("DADATA_KEY")
secret = os.getenv("DADATA_SECRET_KEY")

async def get_city(source: str) -> str:
    async with DadataAsync(token, secret) as dadata:
        resp = await dadata.clean(name="address", source=source)
        city = resp['region']
        return str(city)
    
async def suggest_city(city: str):
    async with DadataAsync(token, secret) as dadata:
        resp = await dadata.suggest("address", city)

        cities = []
        for item in resp:
            #print(item)
            cities.append(
                {'title': item['value'], 
                 'lat': item['data']['geo_lat'], 
                 'lon': item['data']['geo_lon'],
                 'fias_id': item['data']['fias_id']}
                 )
        return cities