import pytest
from Pages.window_handle import WindowHandlingPage
@pytest.mark.usefixtures('pre_and_post_action')
class Test_login1:
    def test_window(self):
        driver = self.driver
        wp = WindowHandlingPage(driver)
        wp.window_handle()
