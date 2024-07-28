from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# articles_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
# articles_count.click()

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("Aditya")
lname.send_keys("Ghumatkar")
email.send_keys("ag.gh@mail.com")

button = driver.find_element(By.CSS_SELECTOR, value=".btn")
button.click()



