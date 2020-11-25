import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    x_value = browser.find_element_by_id('input_value')
    x = x_value.text

    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    checkbox_robot = browser.find_element_by_id('robotCheckbox')
    checkbox_robot.click()
    rb_robot = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb_robot)
    rb_robot.click()
    button = browser.find_element_by_tag_name('button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()




   