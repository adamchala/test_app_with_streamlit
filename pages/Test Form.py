import re
from datetime import date

import streamlit as st

st.set_page_config(page_title='Test Form')

if 'form_accepted' not in st.session_state:
    st.session_state['form_accepted']: bool = False
if 'first_name' not in st.session_state:
    st.session_state['first_name']: str = ''
if 'last_name' not in st.session_state:
    st.session_state['last_name']: str = ''
if 'email' not in st.session_state:
    st.session_state['email']: str = ''
if 'mobile' not in st.session_state:
    st.session_state['mobile']: str = ''
if 'gender' not in st.session_state:
    st.session_state['gender']: str = ''
if 'date_of_birth' not in st.session_state:
    st.session_state['date_of_birth']: str = ''


def check_form():
    if not st.session_state['form_accepted']:
        st.session_state['form_accepted'] = True
        if len(st.session_state['first_name']) > 0:
            pass
        else:
            st.session_state['form_accepted'] = False
            st.warning('First Name can not be empty!')

        if len(st.session_state['last_name']) > 0:
            pass
        else:
            st.session_state['form_accepted'] = False
            st.warning('Last Name can not be empty!')

        pattern = re.compile(r"^\S+@\S+$")
        if pattern.match(st.session_state['email']):
            pass
        else:
            st.session_state['form_accepted'] = False
            st.warning('Email is incorrect!')

        if st.session_state['mobile'].isdigit() and len(st.session_state['mobile']) == 9:
            pass
        else:
            st.session_state['form_accepted'] = False
            st.warning('Mobile is incorrect!')

        if st.session_state['gender']:
            pass
        else:
            st.session_state['form_accepted'] = False
            st.warning('Gender checkbox is not checked!')
    else:
        st.session_state['form_accepted'] = False


st.session_state.horizontal = True

st.title('Personal Form')


if not st.session_state['form_accepted']:
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state['first_name'] = st.text_input('First name', )
        with col2:
            st.session_state['last_name'] = st.text_input('Last name')

        st.session_state['email'] = st.text_input('Email')

        st.session_state['mobile'] = st.text_input('Mobile', max_chars=9)

        st.session_state['gender'] = st.radio('Gender:',
                                              options=['Male', 'Female', 'Other'],
                                              index=None,
                                              horizontal=True)

        st.session_state['date_of_birth'] = st.date_input('Date of Birth',
                                                          max_value=date.today(),
                                                          min_value=date.fromisocalendar(1940, 1, 1),
                                                          format='DD.MM.YYYY')

        st.button('Submit', on_click=check_form)

else:
    with st.container(border=True):
        st.write('First Name:')
        st.info(st.session_state['first_name'])
    with st.container(border=True):
        st.write('Last Name:')
        st.info(st.session_state['last_name'])
    with st.container(border=True):
        st.write('Email:')
        st.info(st.session_state['email'])
    with st.container(border=True):
        st.write('Mobile:')
        st.info(st.session_state['mobile'])
    with st.container(border=True):
        st.write('Gender:')
        st.info(st.session_state['gender'])
    with st.container(border=True):
        st.write('Date of Birth:')
        st.info(st.session_state['date_of_birth'])

    st.button('Reset', on_click=check_form)
