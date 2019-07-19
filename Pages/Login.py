#from data.testdata import *
from Pages.WebGeneric import WebGeneric
class LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="username";
        self.pwd_name="pwd";
        self.login_btn_xpath="//*[text()='Login ']"
        self.wg=WebGeneric(self.driver)

    def acti_login(self):
        self.wg.enter("id",self.un_id, 'admin')
        #self.driver.find_element_by_name("pwd").send_keys("manager")

        self.wg.enter("name",self.pwd_name, 'manager')
        self.wg.submit("xpath",self.login_btn_xpath)