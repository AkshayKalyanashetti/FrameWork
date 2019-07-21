from Data.data import *
from Pages.WebGeneric import WebGeneric
from Pages.LocatorsGeneric import *
class LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="username"
        self.pwd_name="pwd"
        self.login_btn_xpath="//*[text()='Login ']"
        self.wg=WebGeneric(self.driver)

    def acti_login(self):
        #self.driver.find_element_by_id('username').send_keys('admin')
       # self.wg.enter("id",self.un_id, USERNAME)
        un = self.wg.read_data("E:/data.xlsx","Sheet1", "username")
        self.wg.enter("id", self.un_id, un)
        #self.driver.find_element_by_name("pwd").send_keys("manager")
        pwd = self.wg.read_data("E:/data.xlsx", "Sheet1", "pass")
        self.wg.enter("name",self.pwd_name, pwd)
        self.wg.submit("xpath",self.login_btn_xpath)


