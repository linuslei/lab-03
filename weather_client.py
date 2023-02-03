import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "9ac23eb5f96ca314ad6197bc8f2e9f8f"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
def get_hot():
    auth = requests.auth.HTTPBasicAuth('uQe-30ZUwaKjhsBxzcUyFg', 'uDRtltzMz-On4GcReyKJOXC5HAg5-A')
    data = {'grant_type': 'password',
        'username': 'Affectionate-Mind758',
        'password': 'Linus_331066'}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    resq = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
    TOKEN = resq.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    res1 = requests.get("https://oauth.reddit.com/r/python/hot", headers = headers)
    return res1.json()

def main():
    temp = get_weather("London")
    print(temp)
    temp1 = get_hot()
    print(temp1)

if __name__ == "__main__":
    main()