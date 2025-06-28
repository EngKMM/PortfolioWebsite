import streamlit as st
import send_emails

st.header("Contact Me!")

with st.form(key="Email-form"):
    user_email = st.text_input("Your Email")
    user_message = st.text_area("Message")
    mail_message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_emails.send_email(mail_message)
        st.info("Your mail was sent successfully!")
