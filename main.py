from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.baidu.com")
print(driver.title)

search = driver.find_element_by_name("wd")
search.send_keys("test")
search.send_keys(Keys.RETURN) #mean hit enter

#make sure the searching page is correctly loaded.
try:
    content_right = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "content_right"))
    )
    print(content_right.text)
except:
    print("Wait Driver Failed")
    driver.quit()

driver.quit()
