# used libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# set and run driver
driver = webdriver.Edge()

# creating try:except:finally method to open a website
try:
    driver.get('https://itcareerhub.de') # set the url
    # searching and selecting a moment with paying methods
    element = driver.find_element(By.LINK_TEXT, 'Zahlungsarten')
    element.click() # clicking on pay methods
    # creating waiting time
    time.sleep(3)
    # saving screenshot
    driver.save_screenshot('./screen_of_pay_methods.jpg')
    time.sleep(5)
    # ending of a script
    print(f'Entered website:\n"{driver.title}"\n\nScreenshot saved as "screen_of_pay_methods.jpg" in the same folder as the script.')
# creating exception if any trouble exists
except Exception as error:
    print(f'ERROR | {error}')
# finally closing browser edge
finally:
    driver.quit()
