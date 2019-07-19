from Pages.WebGeneric import WebGeneric


class TaskScreen(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.user_name = '//input[@class="inputFieldWithPlaceholder newNameField inputNameField"]'
        self.user_descrip = "//textarea[@placeholder='Enter Customer Description']"

    def task(self):
        wg = WebGeneric(self.driver)
        wg.submit("xpath",'//*[@id="topnav"]/tbody/tr[1]/td[3]/a/div[1]')
        wg.submit("xpath", '//div[text()="Add New"]')
        wg.submit("xpath", "//div[text()='+ New Customer']")
        wg.text("xpath",self.user_name, 'Akshay121')
        wg.text("xpath", self.user_descrip, 'good one11')
        wg.submit("xpath","//div[@class='emptySelection']")
        wg.submit("xpath", '//*[@id="customerLightBox_content"]/div[3]/div[2]/div[2]')
        import time
        time.sleep(5)
        self.driver.switch_to_alert().accept()
