import requests


def get_data(url):
    return requests.get(url).json()
