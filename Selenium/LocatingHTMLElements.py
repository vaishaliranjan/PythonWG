from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://tech-with-tim-merch-shop.creator-spring.com/search")
search= driver.find_element(by= By.CLASS_NAME,value="search-box")

search.send_keys("Test")
search.send_keys(Keys.RETURN)
# print(driver.page_source)
# time.sleep(5)
# driver.quit()

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"search-results"))
    )
    print(element)
except:
    driver.quit()
