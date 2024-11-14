# Daily Challenge : Modules

import time
import requests

def load_time(site):
    try:
        start = time.time()
        response = requests.get(site)
        end = time.time()
        loading = end - start
        if response.status_code == 200:
            print(f'Success.{site} loaded in {loading:.5f} seconds')
        else:
            print(f'Fail to load {site}')

        return loading
    
    except requests.exceptions.RequestException as error:
        print(f'{error}')
        return None
    

websites_to_check = ["https://www.stackoverflow.com",
                     "https://www.youtube.com", 
                     "https://www.google.com",
                     "https://www.w3schools.com"
                      ]
for sites in websites_to_check:
    load_time(sites)
