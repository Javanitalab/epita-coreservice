import requests


class ContactServiceConnector():

    def send_ping(self, endpoint):

        response = requests.get(url=endpoint)

        if response.status_code == 200:
            return True
        else:
            return False
