import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key='email form'):
    user_email = st.text_input('Your email address', key='email')
    user_message = st.text_area('Your message')
    button = st.form_submit_button()
    message = f"""
    Subject: New email from {user_email} \n\n
    From: {user_email}
    {user_message}
    """

    if button:
        send_email(message)
        st.info("Your email was sent successfully")
