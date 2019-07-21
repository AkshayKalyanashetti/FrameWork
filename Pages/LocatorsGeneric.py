from selenium.common.exceptions import *
import xlrd
import moment
import allure
from selenium.webdriver.common.by import By
class LocatorGeneric:
    def __init__(self, driver):
        self.driver = driver
    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element(By.XPATH, locator_val)
            elif loc_type == "tagname":
                ele = self.driver.find_element_by_tag_name(locator_val)
            return ele
        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)
        except WebDriverException as e:
            print(e)
        except NoSuchWindowException as e:
            print(e)
        except UnexpectedTagNameException as e:
            print(e)
        except ElementClickInterceptedException as e:
            print(e)
        except SessionNotCreatedException as e:
            print(e)
        except StaleElementReferenceException as e:
            print(e)
        except Exception as e:
            print(e)

    def read_data(self, path, sheet_name, col_name):
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name(sheet_name)
        var = ws.cell_value(1,1)
        row_count = ws.nrows
        col_count = ws.ncols
        print(row_count)
        print(col_count)
        for i in range(row_count):
            for j in range(col_count):
                if ws.cell_value(i, j) == col_name:
                    val = ws.cell_value(i+1, j)

            break
        return  val



    def get_screenshot(self, log):
        cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        screenshot_name = log + "  " + cur_time
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
      #  self.driver.get_screenshot_as_file(
            #sos.getcwd().replace("\\", "/").replace("pages", "") + "/screenshots/" + screenshot_name + ".png")



