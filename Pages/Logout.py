from Pages.WebGeneric import WebGeneric
class HomeScreen(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.logout_btn = '//*[@id="logoutLink"]'
        self.wg = WebGeneric(self.driver)

    def logout(self):
        self.wg.submit("xpath", self.logout_btn)
        print("logout Passed")
        #self.driver.find_element_by_id('logoutLink').click()