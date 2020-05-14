
def send_msg(self):
    maches = self.driver.find_elements_by_class_name('matchListItem')
    maches[1].click()

