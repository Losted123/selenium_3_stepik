from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
# browser.switch_to.alert.accept()
# x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
# browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(int(x)))
# browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(int(x)))
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()