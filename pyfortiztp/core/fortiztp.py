import requests


class FortiZTP(object):
    """API class for FortiZTP login management.
    """

    def __init__(self, api, **kwargs):
        self.api = api

    def login(self):
        """Login to FortiCloud.
        """

        data = {
            "username": self.api.forticloud_userid,
            "password": self.api.forticloud_password,
            "client_id": "fortiztp",
            "grant_type": "password",
        }

        response = requests.post("https://customerapiauth.fortinet.com/api/v1/oauth/token/", json=data, verify=True)

        # HTTP 200 OK
        if response.status_code == 200:
            if response.json():
                self.api.access_token = response.json()['access_token']
                self.api.expires_in = response.json()['expires_in']
                self.api.refresh_token = response.json()['refresh_token']
                return response.json()
            else:
                self.api.access_token = None
                self.api.expires_in = None
                self.api.refresh_token = None
        
        return response