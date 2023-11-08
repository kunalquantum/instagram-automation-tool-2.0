
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
# Initialize Instaloader
bot = instaloader.Instaloader()

# Create a Streamlit app
st.title("Advanced Instagram Profile Viewer and Post Downloader")

# Function to get basic profile information
def get_basic_info(username):
    try:
        profile = instaloader.Profile.from_username(bot.context, username)
        st.header("Basic Profile Information")
        st.subheader("Username:")
        st.write(profile.username)
        st.subheader("User ID:")
        st.write(profile.userid)
        st.subheader("Number of Posts:")
        st.write(profile.mediacount)
        st.subheader("Followers Count:")
        st.write(profile.followers)
        st.subheader("Following Count:")
        st.write(profile.followees)
        st.subheader("Bio:")
        st.write(profile.biography)
        st.subheader("External URL:")
        st.write(profile.external_url)
        st.subheader("Profile Picture:")
        st.image(profile.profile_pic_url, caption="Profile Picture", use_column_width=True)
    except instaloader.ProfileNotExistsException:
        st.error("Profile not found. Please check the username.")
    except Exception as e:
        st.error(f"Error: {str(e)}")


# Function to download recent posts
def download_recent_posts(username, num_posts):
    try:
        profile = instaloader.Profile.from_username(bot.context, username)
        st.header(f"Download Recent Posts from {profile.username}")
        st.subheader("Profile Picture:")
        st.image(profile.profile_pic_url, caption="Profile Picture", use_column_width=True)
        st.subheader("Latest Posts:")
        posts = profile.get_posts()
        post_count = 0
        download_folder = f"downloaded_posts_{username}"
        os.makedirs(download_folder, exist_ok=True)
        for post in posts:
            if post_count < num_posts:
                st.image(post.url, caption=f"Post {post_count + 1}", use_column_width=True)
                filename = os.path.join(download_folder, f"{username}_post_{post_count + 1}.jpg")
                bot.download_post(post, target=filename)
                post_count += 1
            else:
                break
    except instaloader.ProfileNotExistsException:
        st.error("Profile not found. Please check the username.")
    except Exception as e:
        st.error(f"Error: {str(e)}")



def location(pl,br,mes,c):
    pt.hotkey('win')
    t.sleep(1)
    pt.typewrite('chrome')
    pt.hotkey('enter')
    t.sleep(1)
    pt.click(296, 52)
    t.sleep(1)
    pt.typewrite('https://www.instagram.com')
    pt.hotkey('enter')
    t.sleep(5)
    y=290
    pt.click(130,292)
    for i in range(c):
        t.sleep(2)
        pt.typewrite(f"{br} in {pl}")
        pt.hotkey("enter") 
        t.sleep(2)
        pt.click(245,y)
        t.sleep(3)
        pt.click(561,725)
        t.sleep(5)
        pt.click(764,161)
        t.sleep(2)
        pt.click(893,479)
        t.sleep(2)
        pt.click(840,162)
        #follow
        t.sleep(3)
        pt.click()
        #message
        t.sleep(3)
        pt.click(956,171)
        t.sleep(3)
        pt.click(623,722)
        t.sleep(3)
        pt.typewrite(mes)
        t.sleep(3)
        pt.click(1314,734)
        y=y+50
        pt.click(58,290)

    t.sleep(3455344)
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    t.sleep(1)
    browser.get('https://pallyy.com/tools/image-caption-generator')
     # open the webpage
    #browser.implicitly_wait()
    browser.maximize_window()
def tags(taggigg):
    pt.hotkey('win')
    t.sleep(2)
    pt.typewrite('chrome')
    pt.hotkey('enter')
    t.sleep(2)
    pt.click(296, 52)
    t.sleep(2)
    pt.typewrite('https://www.instagram.com')
    pt.hotkey('enter')
    t.sleep(5)
    hash=get_random_product_hashtag(taggigg)
    pt.click(106,271)#search icon
    t.sleep(1)
    pt.click(124,210)
    pt.typewrite(hash)
    t.sleep(4)
    pt.click()
    t.sleep(1)
    pt.click(189,269)
    pt.click()
    t.sleep(5)
    pt.click(474,438)#OPEN POST
    pt.click()
    t.sleep(5)
    pt.click(887,156)#FOLLOW PAGE
    t.sleep(2)
    pt.click(1019,164)
    t.sleep(3)
    pt.click(712,646)
    t.sleep(2)
    like=pt.locateCenterOnScreen('likes.png')
    pt.moveTo(like)
    pt.click()
    #pt.click(741,664)#OPENING THE LIKE LIST 
    t.sleep(2)
    



    #follows list 
    pt.click(809,327)
    t.sleep(2)
    pt.click(810,374)
    t.sleep(2)
    pt.click(810,417)
    t.sleep(2)
    pt.click(810,430)
    t.sleep(2)
    pt.click(824,557)
    t.sleep(2)
    pt.click(807,486)
    t.sleep(3)
    pt.click(818,616)
    t.sleep(1234)


def cap(pl,br,mes,c):
    service = Service(executable_path='C:\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(service=service, options=options)
    t.sleep(1)
    browser.get('https://www.instagram.com/')
     # open the webpage
    #browser.implicitly_wait()
    browser.maximize_window()
    t.sleep(2)
    pt.click(775,325)
    pt.typewrite("disha0000000")
    t.sleep(0.5)
    pt.click(844,369)
    t.sleep(0.5)
    pt.typewrite("kunal12345")
    t.sleep(8)
    
    pt.click(860,376)
    pt.sleep(8)
    pt.click(875,417)
    pt.click()
    pt.sleep(10)
    
    y=296
    for i in range(c):
        t.sleep(1)
        
        #replace with the y and make it inrease by 10
            #browser.close()
        
        #pt.click(662,537)
        t.sleep(4)
        pt.click(784,456)
        t.sleep(4)
        pt.click(662,537)
        t.sleep(2)
        pt.click(311,175)
        t.sleep(2)
        pt.doubleClick(662,537)
        t.sleep(9)
        pt.click(37,302)#search icon
        t.sleep(2)
        pt.typewrite(f'{br} in #{pl}')
        t.sleep(4)
        pt.click(190,y)

        t.sleep(3)
        pt.click(856,170)#follow
        t.sleep(2)
        #pt.click(662,543)
        t.sleep(2)
        pt.click(981,175)#message
        t.sleep(3)
        pt.click(662,543)
        t.sleep(3)
        pt.click(311,172)
        t.sleep(1)
        pt.typewrite(mes)
        t.sleep(2)
        pt.click(1297,733)#send
        t.sleep(2)
        y=y+80
        i=i+1


    t.sleep(3445)

def comments():
    for i in range(18):
        pt.hotkey("down")
        


import random

# Dictionary of popular product hashtags
product_hashtags = {
    "shoes": [
        "#ShoeGame",
        "#KicksOfTheDay",
        "#SneakerHead",
        "#FashionFootwear",
        "#ShoeLove",
        "#SoleCollector",
    ],
    "books": [
        "#BookLovers",
        "#ReadingList",
        "#MustRead",
        "#Bookworm",
        "#BookNerd",
        "#Literature",
    ],
    "pen": [
        "#PenAddict",
        "#WritingTools",
        "#FountainPen",
        "#Penmanship",
        "#InkPen",
    ],
    "ring": [
        "#RingSelfie",
        "#EngagementRing",
        "#JewelryAddict",
        "#RingGoals",
        "#DiamondRing",
    ],
    "coffee shop": [
        "#CoffeeShopVibes",
        "#CaffeineFix",
        "#CoffeeLover",
        "#CoffeeTime",
        "#CoffeeAddict",
    ],
    "laptop": [
        "#TechGear",
        "#LaptopLife",
        "#PortableOffice",
        "#GamingLaptop",
        "#ProductivityTools",
    ],
    "handbag": [
        "#FashionAccessory",
        "#BagLover",
        "#DesignerHandbag",
        "#LuxuryBags",
        "#HandbagCollection",
    ],
    "camera": [
        "#PhotographyGear",
        "#CameraLife",
        "#CaptureMoments",
        "#DSLRPhotography",
        "#Shutterbug",
    ],
    "bicycle": [
        "#CyclingLife",
        "#BikeRides",
        "#BicycleAdventures",
        "#MountainBiking",
        "#BikeLife",
    ],
    "guitar": [
        "#GuitaristLife",
        "#MusicianLife",
        "#AcousticGuitar",
        "#ElectricGuitar",
        "#JamSession",
    ],
    "phone": [
        "#MobileTech",
        "#SmartphoneLife",
        "#PhonePhotography",
        "#iPhoneAndroid",
        "#CellphoneLove",
    ],
    "cosmetics": [
        "#MakeupAddict",
        "#BeautyProducts",
        "#CosmeticHaul",
        "#SkincareRoutine",
        "#GlamLook",
    ],
    "watch": [
        "#WristWatch",
        "#WatchCollector",
        "#LuxuryTimepieces",
        "#WatchFam",
        "#TimepieceLove",
    ],
    "chocolate": [
        "#ChocolateLover",
        "#SweetTreats",
        "#DeliciousDesserts",
        "#ChocolateHeaven",
        "#CocoaIndulgence",
    ],
    "travel": [
        "#Wanderlust",
        "#TravelAdventure",
        "#ExploreTheWorld",
        "#VacationGoals",
        "#AdventureAwaits",
    ],
    "gaming": [
        "#GamerLife",
        "#GamingCommunity",
        "#VideoGameAddict",
        "#GamingSetup",
        "#GameOn",
    ],
    "flowers": [
        "#FloralBeauty",
        "#FlowerMagic",
        "#BlossomLove",
        "#GardenBlooms",
        "#FloralArrangement",
    ],
    "pets": [
        "#PetLovers",
        "#FurryFriends",
        "#AdoptDontShop",
        "#PetCuddles",
        "#DoggoLove",
    ],
    "fitness": [
        "#FitLife",
        "#WorkoutMotivation",
        "#HealthyLiving",
        "#GymRat",
        "#ActiveLifestyle",
    ],
    "art": [
        "#ArtisticExpression",
        "#ArtGallery",
        "#CreativeMinds",
        "#ArtisticJourney",
        "#VisualArt",
    ],
    # Add more products and their associated hashtags as needed
}

def get_random_product_hashtag(product):
    """
    Get a random hashtag associated with a product.

    Args:
        product (str): The name of the product.

    Returns:
        str: A random hashtag associated with the product.
    """
    product = product.lower()
    if product in product_hashtags:
        hashtags = product_hashtags[product]
        return random.choice(hashtags)
    else:
        return "No hashtags found for this product."

def post_liking():
   

    if st.button("Start Scrapping "):
        pt.hotkey('win')
        t.sleep(1)
        pt.typewrite('chrome')
        pt.hotkey('enter')
        t.sleep(1)
      
        for user_name in user_data:
            if user_name:
                    pt.click(296, 52)
                    t.sleep(4)
                    pt.typewrite(f'https://www.instagram.com')
                    t.sleep(2)
                    pt.hotkey("enter")
                    t.sleep(6)
                    pt.click(129, 295)#search icon
                    t.sleep(2)
                    pt.typewrite(user_name)
                    pt.hotkey('enter')
                    t.sleep(2)
                    pt.click(167, 276)
                    t.sleep(3)
                    pt.click (585, 358)
                    for i in range(12):
                        pt.hotkey('down')
                    t.sleep(5)
                    
                    t.sleep(2)
                    i=0
                    for i in range(c):
                        #like
                        pt.click(767, 666)
                        t.sleep(5)
                        pt.click(826, 612)
                        loc=pt.locateCenterOnScreen('close.png')
                        pt.moveTo(loc)
                        pt.click()

                        t.sleep(12)
                        pt.click(657, 348)
                        t.sleep(2)
                        pt.click(675, 457)
                        



# Streamlit user interface
st.sidebar.header("Select an action")
action = st.sidebar.radio("Choose an action:", ("Get Basic Info",  "Download Recent Posts","Trending Hastags Reach","scrapping tool"))

if action == "Get Basic Info":
    st.header("Get Basic Info")
    username = st.text_input("Enter the Instagram username:")
    if st.button("Get Info"):
        get_basic_info(username)
elif action == "Location Based Reach":
    st.header("Location Based Reach")
    pl=st.text_input("enter the location For analysis")
    br=st.text_input("enter your product name ")
    mes=st.text_area("enter the Proper message about your product")
    c=st.slider("Enter the number of people to follow ",1,10,1)
    if st.button("start"):
        #location(pl,br,mes,c)
        cap(pl,br,mes,c)

elif action == "scrapping tool":
        # Create a list to store user names and messages
    user_data = []

    # Streamlit UI
    st.title("scrap the comments of the post ")

    num_users = st.slider("Number of users for scrapping the comment", min_value=1, max_value=10, value=1)
    c=st.slider("Number of posts from which to scrap commnets",min_value=1,max_value=10,value=2)
    for _ in range(num_users):
        user_name = st.text_input("Enter User user_Name",key=f"user{_}")
        
        user_data.append((user_name))
    post_liking()
elif action == "Download Recent Posts":
    st.header("Download Recent Posts")
    username = st.text_input("Enter the Instagram username:")
    num_posts = st.number_input("Number of Recent Posts to Download", min_value=1, value=5)
    if st.button("Download"):
        download_recent_posts(username, num_posts)
elif action == "Trending Hastags Reach":
    st.header("Reach to the Potential Customers using Hashtags")
    tagging = st.text_input("Enter the product Name for tagging")
    if st.button("Initiate Reach"):
        tags(tagging)
