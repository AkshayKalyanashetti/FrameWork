from Pages.WebGeneric  import WebGeneric
class HomeTime:
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.wg = WebGeneric(self.driver)

    def homescreen(self):
        self.wg.submit("xpath", "//a[text()='View Time-Track']")
        self.wg.submit("xpath", "//a[text()='Lock Time-Track']")