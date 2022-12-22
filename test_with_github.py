

from selene.support.shared import browser
from selene.support import by
import pytest
from selene import be, have
from selene.support.shared.jquery_style import s
def test_clear(open_browser):
   browser.element('[name="q"]').type('rashidik/qa_guru_3_7').press_enter()
   browser.element(by.link_text('rashidik/qa_guru_3_7')).click()
   browser.element('#issue-tab').click()
