import time

from Pages.WebGeneric import WebGeneric
class WindowHandlingPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.login_xpath="/html/body/div[1]/div[1]/div[5]/ul/li[2]/a"
        self.email_tx_id="identifierId"
        # self.dest_xpath="//*[@id='droppable']"
        self.wg=WebGeneric(self.driver)

    def window_handle(self):
        cur_win_id = self.driver.current_window_handle
        time.sleep(15)
        #self.locator("xpath",self.login_xpath)
        self.wg.submit("xpath", self.login_xpath)
        mul_win_id = self.driver.window_handles
        print(mul_win_id)
        for id in mul_win_id:
            if (cur_win_id != id):
                self.driver.switch_to.window(id)
                time.sleep(3)
                self.wg.enter("id", self.email_tx_id, "Test")





