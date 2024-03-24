# Instagram Post Automation
# Version 1.1
'''
This is simple instagram post upload automation,
it is limited to only single image file posting.

Chrome Driver Version - 122
Browser used : Brave Browser
'''
# Modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from pyautogui import typewrite

# Vars
DRIVER = ".\Driver\chromedriver.exe"
BRAVE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

LINK = "https://www.instagram.com"

IMAGE_PATH = ".\image.jpg" #UPDATE ME
DESCRIPTION = """This is a post""" #UPDATE ME 
USERNAME = "" #UPDATE ME
PASSWORD = "" #UPDATE ME

#Chrome Options
Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_argument("--incognito")
Chrome_Options.binary_location = BRAVE

#Initialisation
service = Service(executable_path=DRIVER)
Browser = webdriver.Chrome(service=service, options=Chrome_Options)

# Automation Process
Browser.get(LINK)
WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))

Username_Input_Element = Browser.find_element(By.NAME, "username")
Username_Input_Element.send_keys(USERNAME)

Password_Input_Element = Browser.find_element(By.NAME, "password")
Password_Input_Element.send_keys(PASSWORD + Keys.ENTER)
WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]""")))

Create_Button = Browser.find_element(By.XPATH, """/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]""")
Create_Button.click()

WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button""")))
Upload_Button = Browser.find_element(By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button""")
Upload_Button.click()

sleep(2.5)
typewrite(IMAGE_PATH)
typewrite(['enter'])
sleep(2)

Next_Button_1 = Browser.find_element(By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]""")
Next_Button_1.click()

WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]""")))
Next_Button_2 = Browser.find_element(By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]""")
Next_Button_2.click()

WebDriverWait(Browser, 10).until(EC.presence_of_element_located((By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]""")))
Description_Box = Browser.find_element(By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]""")
Description_Box.send_keys(DESCRIPTION)
sleep(1)

Share_Button = Browser.find_element(By.XPATH, """/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]""")
Share_Button.click()

#Quit
sleep(15)
Browser.quit()
