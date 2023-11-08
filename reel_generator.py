import streamlit as st
import instaloader
import os
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
import streamlit as st
import pyautogui as pt
import time as t
def cap(want):
    pt.hotkey('win')
    t.sleep(1)
    pt.typewrite('chrome')
    pt.hotkey('enter')
    t.sleep(3)
    pt.click(296, 52)
    t.sleep(4)
    pt.typewrite('https://www.veed.io/tools/ai-video/text-to-video')
    pt.hotkey('enter')
    t.sleep(7)
    #t.sleep(312345)

    pt.click(395, 625)
    pt.typewrite(want)
    t.sleep(2)
    pt.click(1006, 624)#generate button
    #give some time for generating 
    t.sleep(40)
    for i in range (3):
        pt.hotkey("down")

    pt.click (510, 676)
    t.sleep(20)
    pt.click(1296, 140)
    t.sleep(5)
    pt.click(1107, 554)
    t.sleep(2)
    pt.click()
    t.sleep(35)
    for i in range(2):
        pt.click(1024, 449)
        t.sleep(2)
        #pt.click(1074, 439)
        t.sleep(8)
        pt.doubleClick(692, 538)
        t.sleep(3)


        t.sleep(4)
import streamlit as st
import time as t
# Define the function 'mode(use)'



# Streamlit app
st.title("Reel Generator")

# Slider for specifying the count
count = st.slider("Select the number of times to run the function:", 1, 10)

# Input for 'use' values
use_values = st.text_area("Enter topics of reel (one per line):")

# Split the entered 'use' values into a list
use_list = [use.strip() for use in use_values.split('\n') if use.strip()]

if st.button("Run Function"):
    if len(use_list) == 0:
        st.warning("Please enter 'use' values.")
    else:
        st.write(f"Running the function {count} times with 'use' values:")
        for _ in range(count):
            for i in use_list:
                cap(i)
                st.write("---")


