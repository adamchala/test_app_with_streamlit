import streamlit as st

st.set_page_config(page_title='Test App')
st.title('Test App')
st.write('This is the app for my test automation showcase')

buttons = st.page_link('pages/Calculator.py', label='Calculator')
text_inputs = st.page_link('pages/Test Form.py', label='Test Form')
