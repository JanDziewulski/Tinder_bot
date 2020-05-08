from selenium import webdriver
from time import sleep
from config import username, password


# Tworzenie klasy TinderBot
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

        # Metoda login umożliwia automatyczna zalogowanie do swojego konta
        #

    def login(self):
        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None
            return element

        self.driver.get('https://tinder.com')

        sleep(4)

        # Wybieranie logowania za pomocą facebook'a

        fb_lc = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_lc.click()

        # Zatwierczenie plików cookie's

        # Przełączenie się na drugie okno w celu logowania

        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        # Wprowadzanie maila oraz hasla

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        # Logowanie do platformy
        login_bnt = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_bnt.click()

        # Zatwierdzanie wtyczki pozwalającej na zaktualizwowanie lokalizacji
        self.driver.switch_to_window(base_window)
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
