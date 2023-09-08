import requests
import json
from datetime import datetime


class SomeWebClient:
    def __init__(self, url):
        self.url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f'{self.url}/sdapi/user.api/users/{user_id}?v=0.5016547602272422')
        json_data = json.loads(resp.text)

        return json_data

    def get_user_registration_date(self, user_id):
        get_date = self.__user_get_status(user_id)
        date_time_obj = " ".join([get_date['registration_date'][:10], get_date['registration_date'][11:-6]])
        date_time_obj = datetime.strptime(date_time_obj, '%Y-%m-%d %H:%M:%S')
        result = f"{date_time_obj - datetime.utcnow()} ago user was created!"

        return result


# some_resource_client = SomeWebClient('https://profile.onliner.by')
# print(some_resource_client.get_user_registration_date(3671980))
