from selenium import webdriver


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

# bot = TinderBot()
# bot.driver.get('https://tinder.com')

    def login(self):
        self.driver.get('https://tinder.com')