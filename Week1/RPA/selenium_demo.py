from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com")

#driver.back()
#driver.forward()
#driver.refresh()
#driver.quit()


#finding elements
# element = driver.find_element(by.ID,"content")
element = driver.find_element(By.XPATH,"/html/body/div[2]")


#wait

wait =webdriver(driver,10)
element = wait.until(EC.presence_of_element_located((By.ID,"content")))


#intraction
element.click()