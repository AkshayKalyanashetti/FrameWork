from Pages.Login import *
from Pages.Task import *
from Pages.Logout import *
from Pages.HomeScreen import *
import pytest
@pytest.mark.usefixtures('pre_and_post_action')
class Test_login:
    def test_actitime(self):
        driver= self.driver
        lp = LoginPage(driver)
        lp.acti_login()

    def test_hmscreen(self):
        driver = self.driver
        hm = HomeTime(driver)
        hm.homescreen()

    def test_task(self):
        driver = self.driver
        tk = TaskScreen(driver)
        tk.task()


    def test_logout(self):
        driver = self.driver
        lout = HomeScreen(driver)
        lout.logout()