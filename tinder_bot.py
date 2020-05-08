from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

from config import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    @property
    def login(self):
        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None
            return element

        self.driver.get('https://tinder.com')

        sleep(4)

        check_more_options = check_exists_by_xpath('//button[text()="Więcej opcji"]')
        if (check_more_options != None):
            check_more_options.click()

        sleep(2)

        fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Zaloguj się przez Facebooka"]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(4)

        self.driver.switch_to_window(self.driver.window_handles[0])

        sleep(4)

        popup_1 = self.driver.find_element_by_css_selector('button[aria-label="Zezwól"]')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_css_selector('button[aria-label="Nie interesuje mnie to"]')
        popup_2.click()