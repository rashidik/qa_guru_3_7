import allure
from selene.support.shared import browser
from selene.support import by
import pytest
from selene import be
from allure_commons.types import Severity


@pytest.fixture()
def set_browser_size_window():
    browser.config.window_height = 720
    browser.config.window_width = 1280


@pytest.fixture()
def open_browser(set_browser_size_window):
    browser.open('https://github.com/')


@allure.tag('qa_guru')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Rashid')
@allure.feature('Задачи')
@allure.story('Чистый тест без степов')
@allure.link('https://github.com', name='Testing')
def test_clear(open_browser):
    browser.element('[name="q"]').type('rashidik/qa_guru_3_7').press_enter()
    browser.element(by.link_text('rashidik/qa_guru_3_7')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#1 opened')).should(be.visible)
