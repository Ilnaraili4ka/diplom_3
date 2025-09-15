import allure
import requests
from curl import Url
from pages.base_page import BasePage

class RequestMetods(BasePage):

    @staticmethod
    def create_user(data):
        return requests.post(Url.CREATE_USER, data=data)

    @staticmethod
    def delete_user(data):
        return requests.delete(Url.CHANGING_USER, headers=data)

    @staticmethod
    def auth_user(data):
        return requests.post(Url.AUTH_USER, data=data)

    @staticmethod
    def create_order(headers=None, data=None):
        return requests.post(Url.CREATE_ORDERS, headers=headers, data=data)
