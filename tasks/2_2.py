from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# a = browser.find_element(By.CSS_SELECTOR, "#num1").text
# b = browser.find_element(By.CSS_SELECTOR, "#num2").text
# print(a)
# print(b)
# ans = int(a) + int(b)

# browser.find_element(By.CSS_SELECTOR, "select.custom-select").click()
# browser.find_element(By.CSS_SELECTOR, 'option[value="'+str(ans)+'"]').click()

# browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()



# x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
# ans = browser.find_element(By.CSS_SELECTOR, "#answer")
# browser.execute_script("return arguments[0].scrollIntoView(true);", ans)
# ans.send_keys(calc(int(x)))
# check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
# browser.execute_script("return arguments[0].scrollIntoView(true);", check)
# check.click()
# rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
# browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
# rule.click()
# submit = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
# submit.click()




current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
browser.find_element(By.CSS_SELECTOR, 'input#file').send_keys(file_path)
elements = browser.find_elements(By.CSS_SELECTOR, '.form-group input')
for elem in elements:
    elem.send_keys("test")

browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
