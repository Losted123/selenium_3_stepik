from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

# x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(int(x)))
browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.XPATH, '//button[text() = "Submit"]').click()
