import smtplib, ssl
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "karimgohary.gohary@gmail.com"
    password = os.getenv("PORTFOLIO_EMAIL_PASSWORD") or st.secrets.get("PORTFOLIO_EMAIL_PASSWORD")

    receiver = "karimgohary.gohary@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)