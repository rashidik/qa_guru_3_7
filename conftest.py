from selene.support.shared import browser
import pytest
import allure


@pytest.fixture()
@allure.step('Открываем браузер')
def set_browser_size_window():
    browser.config.window_height = 720
    browser.config.window_width = 1280


@pytest.fixture()
@allure.step('Устанавливаем размер страницы')
def open_browser(set_browser_size_window):
    browser.open('https://github.com/')
