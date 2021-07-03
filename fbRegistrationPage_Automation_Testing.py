from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/r.php")

driver.find_element_by_name("firstname").send_keys("abc")
driver.find_element_by_name("lastname").send_keys("hasan")
driver.find_element_by_name("reg_email__").send_keys("abc@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("abc@gmail.com")
driver.find_element_by_name("reg_passwd__").send_keys("1234")

# select the day dropdown menu by using Select class
ele = driver.find_element_by_id("day")
day = Select(ele)
#select by value
day.select_by_value("23") #should select 23

month = Select(driver.find_element_by_id("month"))
#select by visible text
month.select_by_visible_text("Sep")

year = Select(driver.find_element_by_id("year"))
#select by visible text
year.select_by_visible_text("1997")

#driver.find_element_by_css_selector("input[type='radio'][name='sex'][value='2']").click()
driver.find_element_by_css_selector("input[name='sex'][value='2']").click()

# click on Sign up button
driver.find_element_by_name("websubmit").click()


