import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image




#find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage",page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local CSS
def local_css(file_name):
    with open(file_name) as  f:
        st.markdown(f"<style>{f.read()}</style",unsafe_allow_html=True)

local_css("style/style.css")

#-------------Load Assets----
lottie_coding =load_lottieurl("https://lottie.host/ec3d3f8c-daf9-46bc-8034-cef4dae0ed9f/IpreBWyG6g.json")
img_contact_form=Image.open('E:/Streamlitproject1/images/white-horse-runs.png')
img_lottie_animation = Image.open('E:/Streamlitproject1/images/car.png')


#----------header section------------
with st.container():
    st.subheader("Hi I am Guru :wave:")
    st.title("A  Data Analyst From India")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effetive  in business settings.")
    st.write("[Learn More >](https://pythonandvba.com)") 


# -----------What I do-------------
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do ")
        st.write("##")
        st.write (
            """
            Let see about the Python for the beginners:
            - Python is commonly used for developing websites and software, task automation, data analysis, and data visualization.
            - Since it's relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances
            -  Besides, Python requires relatively fewer numbers of lines of code to perform the same operations and tasks done in other programming languages with larger code blocks.
               """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#-------projects-----------
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        #insert image
        st.image(img_lottie_animation)

    with text_column:
        st.subheader("Integrate Lottie Animation Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animation make our web app more engaging and fun ,and Lottie Files are the easiest way to do .
            In this tutorial ,i'll show you excatly how to do it
            """
        )      
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=t9r4cHJF9ho)")
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How to Add A contact Form to your Streamlit app")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video,i'm going to show you to implement a contact form in your Streamlit  app using 
            """
        ) 
        st.markdown("[Watch Video...](https://youtube.be/FOULV9Xij_8)")  

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation : https:/formsubmit.co/ !!!Change email address!!!
    contact_form = """  
     <form action="https://formsubmit.co/karthikguruprasath2626@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false"> 
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
     """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()    

    


