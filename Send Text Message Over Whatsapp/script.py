from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://web.whatsapp.com/")
time.sleep(10)

driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys('Name of the person whom you want to send text')
driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]').click()

for i in range(3):
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('*Hi This is Bramhesh*')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT,Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('*This is example text*')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT,Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('Bye')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
