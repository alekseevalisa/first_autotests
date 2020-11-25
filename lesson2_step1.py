import math
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    x_value = browser.find_element_by_id('answer')
    x_value.send_keys(y)

    select_checkbox = browser.find_element_by_id('robotCheckbox')
    select_checkbox.click()

    select_radio = browser.find_element_by_id('robotsRule')
    select_radio.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()