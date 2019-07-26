from selenium import webdriver
driver = webdriver.Chrome('E:\sample\Drivers\chromedriver.exe')
driver.get('https://www.google.com/intl/en-GB/gmail/about/#')
var = driver.current_window_handle
print(var)
driver.find_element_by_partial_link_text('Sign in').click()
mul_var = driver.window_handles
for id in mul_var:
    if (var != id):
        driver.switch_to.window(id)
        import time
        time.sleep(3)
        driver.find_element_by_id('identifierId').send_keys('akshaykalyanashetti@gmail.com')

