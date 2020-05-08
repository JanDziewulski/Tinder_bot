from selenium import webdriver
from time import sleep
from config import password, login

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

# bot = TinderBot()
# bot.driver.get('https://tinder.com')

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
# """Logowanie się do aplikacji desktopowej"""
#         fb_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
#         fb_btn.click()

# """Akceptowanie plików cookies"""
#         accept = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
#         accept.click()
# """Wybieranie logowania za pomocą facebook'a"""


        fb_lc = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')

        fb_lc.click()

# """Wybranie okna do logowania"""

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
# """Wprowadzanie maila oraz hasla"""

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(login)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

# """Logowanie do platformy"""
        login_bnt = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_bnt.click()

# """Zatwierdzenie lokalizacji """
        loc_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_popup.click()

        np_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        np_popup.click()


        self.driver.switch_to_window(base_window)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        np_popup.click()

        """ Przełączenie na kolejne okienko dialogowe oraz
         potwierdzenie wtyczki umożliwiającej zaczytanie lokalizacji 
        """



