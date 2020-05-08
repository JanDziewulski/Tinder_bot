from selenium import webdriver


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

# bot = TinderBot()
# bot.driver.get('https://tinder.com')

    def login(self):
        self.driver.get('https://tinder.com')
"""Logowanie się do aplikacji desktopowej"""
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_btn.click()

"""Akceptowanie plików cookies"""
        accept = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept.click()

"""Wybieranie logowania za pomocą facebook'a"""

        fb_lc = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_lc.click()

"""Wybranie okna do logowania"""

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
"""Wprowadzanie maila oraz hasla"""

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('jasto@vp.pl')
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('dziewulszczak123')

"""Logowanie do platformy"""
        login_bnt = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        log_in.click()




bot = TinderBot()
bot.login()