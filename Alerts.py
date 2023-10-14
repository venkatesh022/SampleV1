import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
time.sleep(3)
alert_window = driver.switch_to.alert

print(alert_window.text)

alert_window.send_keys("Hi There!")
alert_window.accept()  # closes alert window by using ok button
# alert_window.dismiss()  # closes alert window by using cancel button

#########################

# Authentication alert / popup
# https://the-internet.herokuapp.com/basic_auth


# username:admin
# password:admin

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
driver.quit()


#############################################################

# Diable notification popups

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=ops)
driver.maximize_window()
driver.get("https://whatmylocation.com/")

time.sleep(3)





