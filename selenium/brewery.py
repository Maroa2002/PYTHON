from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "/home/matiko847/Desktop/PYTHON/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

first_name = driver.find_element(by="name", value="fName")
first_name.send_keys("george")
last_name = driver.find_element(by="name", value="lName")
last_name.send_keys("george")
email_address = driver.find_element(by="name", value="email")
email_address.send_keys("george@gmail.com")
sign_up = driver.find_element(by="css selector", value="form button")
sign_up.send_keys(Keys.ENTER)
