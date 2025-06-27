import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=500)
with col2:
    st.title("Kareem Mohamed")
    content = """Hi! My name is Kareem and I'm an undergrad A.I Engineering student at GU.
    I'm fairly new to the vast world of tech and I'm an obsessive learner looking to grow my practical
    knowledge every single day by getting things done with my very own hands , whether by structured coursework or independent research
    I always figure out a way to learn the structure of different technologies and how they work under the hood. Driven by passion (some might say even delusion)
    I always try learning in depth about every new technology that I can get my hands on, and through pure dedication and persistence, I somehow always manage to do just that.
    """
    st.info(content)

st.text("Below you can find some of the projects I've been working on. Enjoy! Also don't hesitate to contact me if you like what you see.")
