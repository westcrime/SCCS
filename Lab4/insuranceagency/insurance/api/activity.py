import requests


class ActivityService:
    @staticmethod
    def get_random_activity():
        return requests.get('https://www.boredapi.com/api/activity').json()