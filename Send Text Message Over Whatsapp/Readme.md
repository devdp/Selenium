# Send Text Message Over WhatsApp

#### import webdriver to specify which browser you want to automate i.e. Chrome or Mozilla
```python
from selenium import webdriver
```
#### import Keys for using keyboard functionalities like pressing ENTER, NAVIGATION KEYS etc.
```python
from selenium.webdriver.common.keys import Keys
```
#### import By for finding the element using:
- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector
```python
from selenium.webdriver.common.by import By
```
#### import time for making your script sleep for a some seconds so that you can scan the QR code
```python
import time
```
#### Maximise window automatically with the help of ChromeOptions when browser opens
```python
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
```
#### create instance of Chrome webdriver and open website
```python
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://web.whatsapp.com/")
```
#### make your script sleep for 10 sec so that you can scan QR code
```python
time.sleep(10)
```
#### locate search element of whatsapp using XPATH then enter name of person you want to send text then click on the first appeared result
```python
driver.find_element(By.XPATH,'//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys('Name of the person whom you want to send text')
driver.find_element(By.XPATH,'//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]').click()
```
#### Here I have used for loop just for sending text to same person for multiple times then find the textinput element using XPATH then input text and press Enter if you want send text in a single line else do not press Enter follow this -> press SHIFT + ENTER and then again input text, at last press ENTER
```python
for i in range(3):
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('*Hi This is Bramhesh*')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT,Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('*This is example text*')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.SHIFT,Keys.ENTER)
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys('Bye')
    driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
```
