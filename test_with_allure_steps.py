
import allure
from selene.support.shared import browser
from selene.support import by
from selene import be, have
from selene.support.shared.jquery_style import s

def test_clear(open_browser):
   with allure.step('ищем репозиторий'):
      browser.element('[name="q"]').type('rashidik/qa_guru_3_7').press_enter()

   with allure.step('Переходим по найденной ссылке'):
      browser.element(by.link_text('rashidik/qa_guru_3_7')).click()

   with allure.step('Открываем таб issues'):
      browser.element('#issues-tab').click()

   with allure.step('Проверяем наличие issue с номером 1'):
      browser.element(by.partial_text('#1 opened')).should(be.visible)