from selene.support.shared import browser
from selene.support import by
import allure
from selene import be
from allure_commons.types import Severity


@allure.tag('qa_guru')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Rashid')
@allure.feature('Задачи')
@allure.story('Чистый тест без степов')
@allure.link('https://github.com', name='Testing')
def test_lyambda(open_browser):
    search_for_repository('rashidik/qa_guru_3_7')
    go_to_repo('rashidik/qa_guru_3_7')
    open_issues()
    should_see_issue_1('#1 opened')


@allure.step('ищем репозиторий{repo}')
def search_for_repository(repo):
    browser.element('[name="q"]').type(repo).press_enter()


@allure.step('Переходим по найденной ссылке')
def go_to_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем там issues')
def open_issues():
    browser.element('#issues-tab').click()


@allure.step('Ищем issue #1')
def should_see_issue_1(number):
    browser.element(by.partial_text(number)).should(be.visible)
