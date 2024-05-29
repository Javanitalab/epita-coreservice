import requests



class ContactServiceConnector():

    def __init__(self):

        self.url = 'http://localhost:8001'

    def send_ping(self, endpoint: str):

        response = requests.get(url=endpoint)

        if response.status_code == 200:
            return True
        else:
            return False

    def create_contact(self, data: dict):

        response = requests.post(url=self.url, data=data)

        return response

    def update_contact(self, data: dict):

        response = requests.patch(url=self.url, data=data)

        return response

    def delete_contact(self):

        response = requests.delete(url=self.url)

        return response

    def retrieve_contact(self, params: dict):

        response = requests.get(url=self.url, params=params)

        return response

    def get_authorization_url(self):
        response = requests.get(
            url=self.url + '/outlook/get_authorization_url'
        )

        return response
