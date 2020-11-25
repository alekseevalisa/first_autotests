import math
import time
from selenium import webdriver

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_id('treasure')
    x = picture.get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    select_checkbox = browser.find_element_by_id('robotCheckbox')
    select_checkbox.click()

    select_radio = browser.find_element_by_id('robotsRule')
    select_radio.click()

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()