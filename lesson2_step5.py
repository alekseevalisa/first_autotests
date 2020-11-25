import time
import os
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Elena')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Pavlova')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('pavlovae@tt.tt')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    doc = browser.find_element_by_id('file')
    doc.send_keys(file_path)

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    
    