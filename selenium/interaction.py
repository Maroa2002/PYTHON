from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/matiko847/Desktop/PYTHON/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(url)
number_of_articles = driver.find_element(by="css selector", value="#articlecount a")
# number_of_articles.click()

english_link = driver.find_element(by="link text", value="English")
# english_link.click()

search_bar = driver.find_element(by="id", value="searchInput")
search_bar.send_keys("django")
search_bar.send_keys(Keys.ENTER)