import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl import *
from data import Credentials
from pages.request_metods import RequestMetods


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Url.MAIN_SITE)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(driver):

    with allure.step('Создать пользователя'):
        user_data = Credentials.generate_user_data()
        create_user=RequestMetods.create_user(user_data)
        access_token = create_user.json()["accessToken"]
        headers = {"Authorization": access_token}
    with allure.step('Авторизовать пользователя'):
        auth_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        RequestMetods.auth_user(auth_data)
    yield {"driver": driver, "access_token": access_token}
    with allure.step('Удалить пользователя'):
        RequestMetods.delete_user(headers)

