from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_id('num1')
    x = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    y = int(num2.text)
    z = str(x + y)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(z)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
