from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads")
print(driver.title)
driver.quit()