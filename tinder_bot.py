from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from random import random
from config import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    # Tinder login
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

        """Main part of program, allows login to platform"""

    # Like
    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Polub"]')
        like_btn.click()

    # Dislike
    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Żegnam"]')
        dislike_btn.click()

    # Name searching
    def read_name(self):
        g_name = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span').text
        age = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/span').text
        description = self.driver.find_element_by_class_name('BreakWord').text

    def send_msg(self, count=10):
        w_count = 0
        while w_count < count:
            maches = self.driver.find_elements_by_class_name('matchListItem')
            name = maches[1].text
            maches[1].click()
            self.driver.fullscreen_window()
            """Max size of web browser"""

            sleep(1)
            age = self.driver.find_elements_by_xpath('.//span[@class = "Whs(nw) Fz($l)"]')
            age = age[0].text
            msg = self.driver.find_element_by_class_name('sendMessageForm__input')
            msg.send_keys(
                f'Cześć {name}, mam nadzieję, że lubisz życie na krawędzi i napijesz się piwka w parku bez maseczki ;) Jeśli nie, kasuj ;)')
            sleep(1)
            self.driver.minimize_window()

            element = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            self.driver.execute_script("arguments[0].click();", element)

            sleep(1)
            pairs = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            pairs.click()
            sleep(1)
            if len(maches) < 2:
                break
            print(f'Wysłano {w_count + 1} wiadomość do {name}')
            w_count += 1

        """Automatic sending text msg to matched pairs"""

    def collecting_data(self, count=10):
        w_count = 0
        while w_count < count:
            maches = bot.driver.find_elements_by_class_name('matchListItem')
            maches[1].click()
            bot.driver.fullscreen_window()
            sleep(2)

            try:
                name = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/div[1]/div')
                nametxt = name.text
            except NameError:
                print('Nie można pobrać imienia')

            try:
                age = self.driver.find_elements_by_xpath('.//span[@class = "Whs(nw) Fz($l)"]')
                agetxt = age[0].text
            except NameError:
                print('Nie można pobrać wieku')

            try:
                description = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[2]')
                descriptiontxt = description.text
            except NameError:
                print('Nie można pobrać opisu')

            sleep(2)
            pairs = self.driver.find_element_by_xpath('//*[@id="match-tab"]')
            pairs.click()
            sleep(2)

            if len(maches) < 2:
                break

            print(f"{nametxt}, {agetxt}, {descriptiontxt}")

            w_count += 1

            df = pd.DataFrame({'name': [nametxt],
                               'age': [agetxt],
                               'description': [descriptiontxt]})

            df.to_csv('test_tnd.csv', index=False)


"""Next to update"""


# Auto swaping
def auto_swipe(self, count=10):
    r_counter = 0
    l_counter = 0
    # while True:
    for i in range(count):
        sleep(2)
        try:
            rand = random()
            if rand < 0.73:
                self.like()
                r_counter += 1
                print(f"{r_counter}te przesunięcie w prawo")
                i += 1
            else:
                self.dislike()
                l_counter += 1
                print(f"{l_counter}te przesunięcie w lewo")
                i += 1
        except Exception:
            try:
                self.close_popup()
            except Exception:
                self.close_match()


"""Automatic swiping and counting swipes"""


def close_popup(self):
    popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    popup_3.click()


def close_match(self):
    match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
    match_popup.click()


bot = TinderBot()
bot.login()
