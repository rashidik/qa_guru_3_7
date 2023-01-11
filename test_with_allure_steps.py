import allure
import pytest
from selene.support.shared import browser
from selene.support import by
from selene import be, have
from allure_commons.types import Severity


@pytest.fixture()
def set_browser_size_window():
    with allure.step('Устанавливаем размер страницы'):
        browser.config.window_height = 720
        browser.config.window_width = 1280


@pytest.fixture()
def open_browser(set_browser_size_window):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')


@allure.tag('qa_guru')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Rashid')
@allure.feature('Задачи')
@allure.story('Чистый тест без степов')
@allure.link('https://github.com', name='Testing')
def test_allure_steps(open_browser):
    with allure.step('ищем репозиторий'):
        browser.element('[name="q"]').type('rashidik/qa_guru_3_7').press_enter()

    with allure.step('Переходим по найденной ссылке'):
        browser.element(by.link_text('rashidik/qa_guru_3_7')).click()

    with allure.step('Открываем таб issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие issue с номером 1'):
        browser.element(by.partial_text('#1 opened')).should(be.visible)
