from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.shwapno.com/")

#select city
city = Select(driver.find_element_by_id("state"))
city.select_by_value("BD8")

#select location/area
area = Select(driver.find_element_by_id("city"))
area.select_by_visible_text("Mirpur 2")

#click on submit button
driver.find_element_by_id("btnFindStore").click()


#Registration
driver.find_element_by_xpath("/html/body/form/div[4]/center/div/div/center/div/div[1]/div/div[1]/div[2]/div/div/a[2]").click()
registration = driver.find_element_by_xpath("//*[@id='txtCRMMobileNO']").send_keys("01521330532")
driver.find_element_by_id("btnValidateMob").click()


driver.find_element_by_xpath("//*[@id='txtOTP']").send_keys("8457")
driver.find_element_by_xpath("//*[@id='btnValidateOTP']").click()

driver.find_element_by_name("txtFirstName").send_keys("John")
driver.find_element_by_name("txtLastName").send_keys("son")
driver.find_element_by_name("txtEmailID").send_keys("John@gmail.com")
driver.find_element_by_id("txtPassword").send_keys("12345")
driver.find_element_by_id("txtConfirmPassword").send_keys("12345")
driver.find_element_by_id("btnRegistration").click()


#Login/validate registration is successful or not

driver.find_element_by_xpath("/html/body/form/div[4]/center/div/div/center/div/div[1]/div/div[1]/div[2]/div/div/a[1]").click()
driver.find_element_by_xpath("//*[@id='tab1']")

driver.find_element_by_xpath("//*[@id='txtCRMMobileNOLogin']").send_keys("01521330532")
driver.find_element_by_id("btnValidateMob").click()
driver.find_element_by_id("txtOTP").send_keys("1686")
driver.find_element_by_id("btnValidateOTP").click()



