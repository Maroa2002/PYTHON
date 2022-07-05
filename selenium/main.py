from selenium import webdriver

chrome_driver_path = "/home/matiko847/Desktop/PYTHON/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
events_times = driver.find_elements(by="css selector", value=".event-widget .menu li time")
# for time in events_times:
#     # event_time = time.text
events_titles = driver.find_elements(by="css selector", value=".event-widget .menu li a")
# for title in events_titles:
#     # event_name = title.text
#     # print(event_name)
events = {}
for n in range(len(events_titles)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_titles[n].text,
    }

print(events)

driver.close()