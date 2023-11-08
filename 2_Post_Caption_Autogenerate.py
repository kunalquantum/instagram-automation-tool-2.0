import streamlit as st
import pyautogui
import time
from PIL import Image

# Logo
#logo = Image.open("logo.png")


# Function to open Google Chrome
def open_chrome():
  pyautogui.hotkey('win', 'r')
  pyautogui.typewrite('chrome')
  pyautogui.press('enter')
  time.sleep(5)

# Function for the automation steps
def automation_steps(post):
    # Open Google Chrome (You may need to adjust the coordinates)
  pyautogui.hotkey('win', 'r') # Open the Run dialog
  pyautogui.typewrite('chrome')
  pyautogui.press('enter')

  # Wait for Chrome to open
  time.sleep(5)

  # Search for Google
  pyautogui.typewrite('https://designer.microsoft.com/')
  pyautogui.press('enter')

  # Wait for Google to load (you may need to adjust the delay)
  time.sleep(12)
  #placehoder
  pyautogui.click(424, 379)
  time.sleep(4)
   
  pyautogui.typewrite(f"create a beautiful and lively post for instagram on (image) {post}")
  time.sleep(4)
  #generate button
  
  pyautogui.click(587, 472)
  time.sleep(30)
  #modified prompt
  pyautogui.click(329, 476)
  time.sleep(12)
  #generate
  pyautogui.click(592, 469)
  time.sleep(15)
  #selecting the post 
  pyautogui.click(821, 366)
  time.sleep(7)
  st.write("3")
  #download 
  pyautogui.click(1130, 710)
  time.sleep(7)
  st.write("3")
  #download 
  pyautogui.click(1139, 430)
  st.write("3")


  pass

def main():
  st.markdown("---")
  st.title("Generate Awesome posts and Captions")
  st.markdown("---")
  

  # Sidebar
  with st.sidebar:
    st.markdown("**Instructions:**")
    st.markdown("1. Enter the post you want to generate.")
    st.markdown("2. Click the 'Start Automation' button.")
  st.markdown("---")
  # Post input
  post = st.text_input("Enter your Post to Generate:")
  st.markdown("---")
 # Button to start the automation
  
  if st.button("Post an AI generated Post and Caption "):

   
      combine(post)
   
import pyperclip
import streamlit as st
import pyautogui as pt
import time as t
import streamlit as st
import io
import time
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def cap():
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    t.sleep(1)
    browser.get('https://pallyy.com/tools/image-caption-generator')
     # open the webpage
    #browser.implicitly_wait()
    browser.maximize_window()
    
    t.sleep(2)
    input=browser.find_element(By.XPATH,'//div[@class="upload-input"]')
    input.click()
    t.sleep(2)
    #choosig the downloads
    pt.click(64, 176)
    t.sleep(2)
    pt.click(236, 172)
    st.write("1")
    t.sleep(4)
    pt.click(508, 423)
    for i in range(10):
        pt.hotkey("down")
    t.sleep(7)
    generate=browser.find_element(By.XPATH,'//button[@class="button generate-button"]')
    generate.click()
    t.sleep(6)
    for i in range(10):
        pt.hotkey("down")
    t.sleep(2)
    copy=browser.find_element(By.XPATH,'//button[@class="button tweet__button-copy"]')
    t.sleep(1)
    copy.click()
    st.title("your Captions are ready ")

    # Check if there is text in the clipboard
    # Check if there is text in the clipboard
    if pyperclip.paste():
        clipboard_text = pyperclip.paste()
        st.write("Text from clipboard:")
        
        # Use an expandable container to display text
        with st.expander("Clipboard Text"):
            st.text(clipboard_text)
        
        # Add a button to copy text to clipboard
        if st.button("Copy to Clipboard"):
            pyperclip.copy(clipboard_text)
            st.success("Text copied to clipboard!")
    else:
        st.write("Clipboard is empty.")
    browser.close()
    

    

def combine(post):
    automation_steps(post)
    t.sleep(2)
    cap()
    t.sleep(2)
    create()


def create():
    pt.hotkey('win')
    t.sleep(1)
    pt.typewrite('chrome')
    pt.hotkey('enter')
    t.sleep(1)
    pt.click(296, 52)
    t.sleep(4)
    pt.typewrite('https://www.instagram.com')
    pt.hotkey('enter')
    t.sleep(2)
    t.sleep(3)
    pt.click(92, 575)
    t.sleep(2)
    pt.click(675,528)
    t.sleep(2)
    pt.click(61, 221)
    t.sleep(1)
    pt.click(232, 171)
    t.sleep(2)
    pt.click(501, 424)
    t.sleep(1)
    pt.click(870, 213)
    t.sleep(1)
    pt.click(870, 212)
    t.sleep(1)
    pt.click(1040, 214)
    t.sleep(1)
    pt.click(1041, 203)
    t.sleep(1)
    pt.click(818,320)
    t.sleep(2)
    pt.hotkey('ctrl','v')
    t.sleep(2)
    pt.click(1032,215)
    t.sleep(2112)

    

if __name__ == "__main__":
  main()



