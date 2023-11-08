import streamlit as st
import pyautogui as pt
import time as t
# Define the main page layout
def main_page():
    # Add a header with the title
    st.title("My instagram Handler ")

    # Sidebar for navigation
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Go to", ["Login", "Default Page","Notification","Message Individually","Searching And Following","Liking the Posts","Broadcast message"])

    if page == "Login":
        login_page()
    elif page == "Message Individually":
        message()
    elif page == "Broadcast message":
        message1()
    elif page == "Searching And Following":
        search()
    elif page == "Notification":
        notification()
    elif page == "Liking the Posts":
        post_liking()
    elif page == "Scheduled post":
        post_liking()
    else:
        default_page()

# Login page layout
def login_page():
    st.markdown("## Login Page")

    # Input fields for username and password
    username1 = st.text_input("Username")
    password = st.text_input("Password", type="password")
    username=username1.lower()
   
    # Login button
    login_button = st.button("Login")

    if login_button:
        login1(username,password)
        
    
# Default page layout
def default_page():
    pt.hotkey('win')
    t.sleep(1)
    pt.typewrite('chrome')
    
    pt.hotkey('enter')
    t.sleep(1)
    pt.typewrite('https://www.instagram.com/')
    pt.hotkey('enter')
    t.sleep(23)
    

def login1(username,password):
    pt.hotkey('win')
    t.sleep(2)
    pt.typewrite('firefox')
    pt.hotkey('enter')
    t.sleep(2)
    pt.typewrite('https://www.instagram.com/')
    pt.hotkey('enter')
    t.sleep(3)
    pt.click(782, 283)
    
    t.sleep(1)
    pt.click()
    t.sleep(2)
    pt.typewrite(username)
    t.sleep(2)
    pt.click(791, 333)
    t.sleep(2)
    pt.click()
    t.sleep(2)
    pt.typewrite(password)
    pt.sleep(2)
    pt.click
    t.sleep(4)  
    pt.click(891, 378)
    t.sleep(798, 434)
    pt.click(798, 434)
    t.sleep(2)
    pt.click
def notification():
    
    pt.hotkey('win')
    t.sleep(1)
    pt.typewrite('chrome')
    pt.hotkey('enter')
    t.sleep(1)
    pt.typewrite('https://www.instagram.com/notifications/')
    pt.hotkey('enter')
    t.sleep(3)

def message():
     # Create a list to store user names and messages
    user_data = []

    # Streamlit UI
    st.title("Message Sender App")

    num_users = st.slider("Number of Users", min_value=1, max_value=10, value=1)
    num_messages = st.slider("Number of Messages per User", min_value=1, max_value=10, value=1)

    for _ in range(num_users):
        user_name = st.text_input("Enter User Name",key=f"user{_}")
        user_messages = []
        for _ in range(num_messages):
            user_message = st.text_area(f"Enter Message for {user_name}")
            user_messages.append(user_message)
        
        user_data.append((user_name, user_messages))

    if st.button("Send All Messages"):
        pt.hotkey('win')
        t.sleep(3)
        pt.typewrite('chrome')
        pt.hotkey('enter')
        t.sleep(2)
        t.sleep(2)
        for user_name, user_messages in user_data:
            if user_name:
                for user_message in user_messages:
                    if user_message:
                        pt.click(296, 52)
                        t.sleep(4)
                        pt.typewrite('https://www.instagram.com/direct/inbox/')
                        pt.hotkey('enter')
                        t.sleep(5)
                        pt.doubleClick(916, 529)
                        pt.hotkey('enter')
                        t.sleep(2)
                        t.sleep(2)
                        pt.typewrite(user_name)
                        t.sleep(2)
                        pt.click(485, 340)
                        t.sleep(2)
                        pt.hotkey('enter')
                        t.sleep(2)
                        pt.click(678, 612)
                        t.sleep(5)
                        pt.hotkey('enter')
                        t.sleep(2)
                        pt.typewrite(user_message)
                        pt.hotkey('enter')
        st.success("All messages sent!")

    # Display user data
    st.header("User Data")
    st.table(user_data)

import time as t
import pyautogui as pt
import streamlit as st

def message1():
    # Create a list to store user names
    user_names = []

    # Streamlit UI
    st.title("Message Sender App")

    num_users = st.slider("Number of Users", min_value=1, max_value=10, value=1)

    for i in range(num_users):
        user_name = st.text_input("Enter User Name", key=f"user_{i}")
        if user_name:
            user_names.append(user_name)

    common_message = st.text_area("Enter the Common Message to Send")

    if st.button("Send Common Message"):
        pt.hotkey('win')
        t.sleep(3)
        pt.typewrite('chrome')
        pt.hotkey('enter')
        t.sleep(2)
        t.sleep(2)
        for user_name in user_names:
            if user_name:
                pt.click(296, 52)
                t.sleep(4)
                pt.typewrite('https://www.instagram.com/direct/inbox/')
                pt.hotkey('enter')
                t.sleep(5)
                pt.doubleClick(916, 529)
                pt.hotkey('enter')
                t.sleep(2)
                t.sleep(2)
                pt.typewrite(user_name)
                t.sleep(2)
                pt.click(485, 340)
                t.sleep(2)
                pt.hotkey('enter')
                t.sleep(2)
                pt.click(678, 612)
                t.sleep(5)
                pt.hotkey('enter')
                t.sleep(2)
                pt.typewrite(common_message)
                pt.hotkey('enter')
        st.success("Common message sent to all users!")

    # Display user names
    st.header("User Names")
    st.table(user_names)


    
def search():
     # Create a list to store user names and messages
    user_data = []

    # Streamlit UI
    st.title("Search and follow  App")

    num_users = st.slider("Number of Users to be followed", min_value=1, max_value=10, value=1)
   
    for _ in range(num_users):
        user_name = st.text_input("Enter User Name",key=f"user{_}")
        
        user_data.append((user_name))

    if st.button("Find and Follow"):
        pt.hotkey('win')
        t.sleep(1)
        pt.typewrite('chrome')
        pt.hotkey('enter')
        t.sleep(1)
      
        for user_name in user_data:
            if user_name:
                    pt.click(296, 52)
                    t.sleep(4)
                    pt.typewrite(f'https://www.instagram.com/{user_name}')
                    pt.hotkey('enter')
                    t.sleep(7)
                    pt.click(795, 161)
                    t.sleep(3)
    st.header("User Data")
    st.table(user_data)                  
                    
def post_liking():
     # Create a list to store user names and messages
    user_data = []

    # Streamlit UI
    st.title("Like the post App")

    num_users = st.slider("Number of users for liking the post", min_value=1, max_value=10, value=1)
    c=st.slider("Number of posts to like ",min_value=1,max_value=10,value=2)
    for _ in range(num_users):
        user_name = st.text_input("Enter User user_Name",key=f"user{_}")
        
        user_data.append((user_name))

    if st.button("Start liking the Post "):

        pt.hotkey('win')
        t.sleep(1)
        pt.typewrite('chrome')
        pt.hotkey('enter')
        t.sleep(1)
      
        for user_name in user_data:
            if user_name:
                    pt.click(296, 52)
                    t.sleep(4)
                    pt.typewrite(f'https://www.instagram.com/')
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
                    t.sleep(2)
                    pt.click()
                    t.sleep(2)
                    i=0
                    
                    for i in range(c):
                        #like
                        pt.click(767, 666)
                        t.sleep(1)
                        pt.click(923, 243)
                        t.sleep(2)
                        pt.click(706, 611)
                        t.sleep(2)
                        
                        pt.click(923, 243)
                        t.sleep(2)
                        t.sleep(1)
                        pt.click(631, 616)
                        t.sleep(1)
                        pt.click(923, 243)
                        t.sleep(2)
                        pt.click(635, 616)
                        pt.sleep(1)
                        pt.click(923, 243)
                        t.sleep(2)
                        pt.click(637, 614)
                        like=pt.locateCenterOnScreen("like.png")
                        pt.moveTo(like)
                        t.sleep(3)
                        pt.click()

                        t.sleep(3)
                        #next
                        #pt.click(1334, 433)
                        pt.hotkey('right')
                        c+=1
                    pt.click(1341, 132)

                    
    st.header("User Data")
    st.table(user_data)                  

def create():
    import streamlit as st
    import pyautogui as pt
    import time as t
    import schedule
    from datetime import datetime

    # Streamlit UI
    st.title("Post sharing")

    co = st.slider("Number of posts to share", min_value=1, max_value=10, value=2)
    scheduled_time = st.time_input("Select the time to schedule the task")

    def share_posts():
        for i in range(co):
            pt.hotkey('win')
            t.sleep(1)
            pt.typewrite('chrome')
            pt.hotkey('enter')
            t.sleep(1)
            t.sleep(4)
            pt.typewrite('https://www.instagram.com')
            pt.hotkey('enter')
            t.sleep(2)
            t.sleep(3)
            pt.click(662, 523)
            t.sleep(1)
            pt.click(219, 256)
            t.sleep(1)
            pt.click(512, 501)
            t.sleep(2)
            pt.click(868, 214)
            t.sleep(1)
            pt.click(1039, 216)
            t.sleep(1)
            pt.click(889, 355)
            t.sleep(1)
            pt.typewrite("caption")
            t.sleep(25)

        # Create a button to manually trigger post sharing
        if st.button("Start liking the Post"):
            share_posts()

        # Schedule the task based on the user's selected date and time
        scheduled_datetime = datetime.combine(datetime.today(), scheduled_time)
        st.info(f"The task is scheduled to run at {scheduled_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

        def schedule_task():
            schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(share_posts)

        # Streamlit will continuously run the app, and the scheduled task will be executed as configured.
        while True:
            schedule.run_pending()
            t.sleep(1)


                       
    






    
# Main app
if __name__ == "__main__":
    main_page()
