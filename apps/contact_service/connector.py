import requests


class ContactServiceConnector():

    def send_ping(self, endpoint : str):

        response = requests.get(url=endpoint)

        if response.status_code == 200:
            return True
        else:
            return False


    def create_contact(self,endpoint : str , data : dict):

        response = requests.post(url=endpoint,data=data)

        return response