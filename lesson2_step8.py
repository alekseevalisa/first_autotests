from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.get(link)

try:
    price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    book = driver.find_element_by_id('book')
    book.click()
    x_value = driver.find_element_by_id('input_value')
    x = x_value.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    answer = driver.find_element_by_id('answer')
    answer.send_keys(y)
    button = driver.find_element_by_id('solve')
    button.click()

finally:
    time.sleep(30)
    driver.quit()
