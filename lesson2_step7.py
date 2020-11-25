from selenium import webdriver
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    button = driver.find_element_by_tag_name('button')
    button.click()

    current_window = driver.window_handles[0]
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x_value = driver.find_element_by_id('input_value')
    x = x_value.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    answer = driver.find_element_by_id('answer')
    answer.send_keys(y)
    button = driver.find_element_by_tag_name('button')
    button.click()

finally:
    time.sleep(10)
    driver.quit()

