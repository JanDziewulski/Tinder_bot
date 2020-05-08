from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from random import  random

from config import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


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
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(4)

        self.driver.switch_to.window(base_window)

        sleep(4)

        popup_1 = self.driver.find_element_by_css_selector('button[aria-label="Zezwól"]')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_css_selector('button[aria-label="Nie interesuje mnie to"]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Polub"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Żegnam"]')
        self.driver.get()
        dislike_btn.click()

    def auto_swipe(self):
        r_counter = 0
        l_counter = 0
        while True:
            sleep(3)
            try:
                rand = random()
                if rand < 0.80:
                    self.like()
                    r_counter += 1
                    print(f"{r_counter}te przesunięcie w prawo")
                else:
                    self.dislike()
                    l_counter += 1
                    print(f"{l_counter}te przesunięcie w lewo")

            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    # def message_all(self):
    #     matches = self.driver.find_element_by_class_name('matchListNoMessages')

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()