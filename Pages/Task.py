from Pages.WebGeneric import WebGeneric


class TaskScreen(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.driver = driver
        self.user_name = '//input[@class="inputFieldWithPlaceholder newNameField inputNameField"]'
        self.user_descrip = "//textarea[@placeholder='Enter Customer Description']"
        self.wg = WebGeneric(self.driver)

    def task(self):
        self.wg.submit("xpath",'//*[@id="topnav"]/tbody/tr[1]/td[3]/a/div[1]')
        self.wg.submit("xpath", '//div[text()="Add New"]')
        self.wg.submit("xpath", "//div[text()='+ New Customer']")
        self.wg.text("xpath",self.user_name, 'Akshay121')
        self.wg.text("xpath", self.user_descrip, 'good one11')
        self.wg.submit("xpath","//div[@class='emptySelection']")
        import time
        time.sleep(5)
        #self.wg.submit("xpath", '//*[@id="customerLightBox_content"]/div[3]/div[2]/div[2]')
        self.wg.alert()
        #time.sleep(2)
        #var1.accept()
