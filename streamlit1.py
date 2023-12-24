import random
import requests
import streamlit as st
from pathlib import Path
import json
from streamlit_lottie import st_lottie
import streamlit_extras
from PIL import Image


st.set_page_config(page_title="Brad Naylor - Portfolio", layout="wide")
DIR1 = Path(__file__).parent
CSS1 = DIR1 / "style" / "style.css"
ASST = DIR1 / "assets"
COOLNESS = ASST / "load.json"
COOLNESS1 = ASST / "hello.json"
wave = "<span class='wave'>👋</span>"

def load_coolness(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

with open(CSS1) as stylesheet:
    st.markdown(f"<style>{stylesheet.read()}</style>", unsafe_allow_html=True)

with st.container():
    st.title(f"Hello, I'm Brad Naylor ", anchor=False) 
    st.markdown(f"{wave}", unsafe_allow_html=True)
    st.header(f"I'm a Senior at UNCW - majoring in Information Technology with a concentration in Cybersecurity", anchor=False)
    st.write(
        "I'm passionate about Linux, Networking, Cybersecurity and Python Scripting. I'm interested in using scripts to automate tasks to be more efficient and effective in business settings."
    )
    content1 = """<form action="https://linkedin.com/in/brad-naylor"><button type="submit">Visit My LinkedIn</button></form>"""
    st.markdown(content1, unsafe_allow_html=True)
    st.write("---")
    

with st.container():
    st.header("My Projects", anchor=False)
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        lottie1 = load_coolness(COOLNESS)
        st_lottie(lottie1, key="load", height=160)
    with text_column:
        st.subheader("Python Netscanner", anchor=False)
        st.write(
            """
            Python IP Range + Mac Address Netscanning tool,
             complete with GUI and 4 different scanning methods including ARP, ICMP, TCP, and UDP. Built using Scapy library as well as 
            """
        )
        st.write("[View on Github](https://linkedin.com/in/brad-naylor)")
        

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        lottie1 = load_coolness(COOLNESS)
        st_lottie(lottie1, key="checkpls", height=160)
    with text_column:
        st.subheader("Home Networking Security Lab with Raspberry Pis", anchor=False)
        st.write("•	Integrated two Raspberry Pi Single Board Computers (SBCs): one as a Home Media Server using Jellyfin, providing seamless media streaming, and the other as a network-wide ad blocker with AdGuard, enhancing online privacy and security.")
        st.write("• Implemented a Honeypot utilizing HoneyPi using a third Raspberry Pi Single Board Computer, enhancing network security through proactive threat detection and analysis, aligning with industry best practices.")
        st.write("[View on Github](https://linkedin.com/in/brad-naylor)")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        lottie1 = load_coolness(COOLNESS)
        st_lottie(lottie1, key="hello", height=160)
    with text_column:
        st.subheader("Python/Streamlit Christmas Card", anchor=False)
        st.write(
            """
            Created a Digital Holiday Card to share with family and friends, using Python with the Streamlit library
            along with some html,css and json.
            """
        )
        st.write("[View on Github](https://linkedin.com/in/brad-naylor)")
        st.write("[View Webpage](https://christmas-card.streamlit.app)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!", anchor=False)
    st.text("")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="formsubmit.co//naylorbmn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        lottie2 = load_coolness(COOLNESS1)
        st_lottie(lottie2, key="bello", height=200)
    with right_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    
# hide link thingies
st.markdown("""
    <style>
    /* Hide the link button */
    
    
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    </style>
    """, unsafe_allow_html=True)
