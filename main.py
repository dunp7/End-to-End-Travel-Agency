import streamlit as st
from PIL import Image

# Configure page
st.set_page_config(page_title="Mindtrip", layout="wide")

# Sidebar navigation
st.sidebar.markdown("<h1 style='font-size:35px; font-weight:bold;'>Mindtrip</h1>", unsafe_allow_html=True)

# Radio button để chọn các tùy chọn
option = st.sidebar.radio("Select Option:", ["Chats", "Explore"])

if option == "Chats":
    # Header section
    st.markdown("# Where to today?")
    st.markdown("> Hey there, where would you like to go? I’m here to assist you in planning your experience. Ask me anything travel related.")

    # Main content sections
    st.markdown("---")

    # Explore Section
    st.subheader("For you in 🌍 Hang Bai")
else:

    pass
