from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    tok=WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_id("solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(10)
    browser.quit()
test rep
