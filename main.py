import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)
with col2:
    st.title("Kareem Mohamed")
    content = """Hi! My name is Kareem and I'm an undergrad A.I Engineering student at GU.
    I'm fairly new to the vast world of tech and I'm an obsessive learner looking to grow my practical
    knowledge every single day by getting things done with my very own hands.
    """
    st.info(content)
