import requests 

from config import TOKEN


class CatClient:

    def __init__(self) -> None:
        self.base_url = 'https://api.thecatapi.com'
        self.token = TOKEN

    def get_random_cat(self) -> str:
        url = f"{self.base_url}/v1/images/search"
        headers = {
            'x-api-key': self.token
        }

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            cat_url = data[0]['url']

            return cat_url
        else:
            raise Exception("No Cat")
    

cat_client = CatClient()
print(cat_client.get_random_cat())

