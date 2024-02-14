import streamlit as st


if 'display' not in st.session_state:
    st.session_state['display']: str = '0'
if 'operation' not in st.session_state:
    st.session_state['operation'] = None
if 'first_value' not in st.session_state:
    st.session_state['first_value'] = None
if 'operator' not in st.session_state:
    st.session_state['operator'] = '+'
if 'operand1' not in st.session_state:
    st.session_state['operand1'] = 0
if 'new_operand' not in st.session_state:
    st.session_state['new_operand'] = True


def format_number(num):
    """Function that cuts unnecessary zeros and commas"""
    if num % 1 == 0:
        return str(int(num))
    else:
        return str(num)


def calculate(operand1, operand2, operator):
    """Function that performs mathematical operations"""
    if operator == "+":
        return format_number(operand1 + operand2)

    elif operator == "-":
        return format_number(operand1 - operand2)

    elif operator == "*":
        return format_number(operand1 * operand2)

    elif operator == "/":
        if operand2 == 0:
            return "Error"
        else:
            return format_number(operand1 / operand2)


def reset():
    """Function that reset calculator state"""
    st.session_state['operator'] = "+"
    st.session_state['operand1'] = 0
    st.session_state['new_operand'] = True


def button_clicked(key):
    """Function that chose acton depend on button clicked"""
    if st.session_state['display'] == 'Error' or key == 'AC':
        st.session_state['display'] = "0"
        reset()
    elif key in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '00'):
        if st.session_state['display'] == '0' or st.session_state['new_operand'] is True:
            st.session_state['display'] = key
            st.session_state['new_operand'] = False
        else:
            st.session_state['display'] = st.session_state['display'] + key
    elif key in ('+', '-', '*', '/'):
        # if
        st.session_state['display'] = calculate(st.session_state['operand1'], float(st.session_state['display']), st.session_state['operator'])
        st.session_state['operator'] = key
        if st.session_state['display'] == 'Error':
            st.session_state['operand1'] = '0'
        else:
            st.session_state['operand1'] = float(st.session_state['display'])
        st.session_state['new_operand'] = True
    elif key in ('='):
        st.session_state['display'] = calculate(st.session_state['operand1'], float(st.session_state['display']),
                                                st.session_state['operator'])
        reset()
    elif key in ('%'):
        st.session_state['display'] = str(float(st.session_state['display']) / 100)
    elif key in ('+/-'):
        if float(st.session_state['display']) > 0:
            st.session_state['display'] = '-' + st.session_state['display']
        elif float(st.session_state['display']) < 0:
            st.session_state['display'] = st.session_state['display'][1:]
    elif key in ('.'):
        if '.' not in st.session_state['display']:
            st.session_state['display'] = st.session_state['display'] + '.'
    elif key in ('◀'):
        st.session_state['display'] = st.session_state['display'][:-1]
        if not st.session_state['display'] or st.session_state['display'] == '-':
            st.session_state['display'] = '0'


# page layout
st.set_page_config(page_title='Calculator')
st.title('Calculator')
st.write('This is the calculator app that hopefully do what every well behave calculator should do')

col0, col1, col2 = st.columns([3, 4, 3])
with col1:
    with st.container(border=True, height=60):
        st.write(st.session_state['display'])


with st.container():
    col0, col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1, 3])

    with col0:
        st.empty()

    with col1:
        st.button('AC', use_container_width=True, on_click=button_clicked, kwargs={'key': 'AC'})
        st.button('7', use_container_width=True, on_click=button_clicked, kwargs={'key': '7'})
        st.button('4', use_container_width=True, on_click=button_clicked, kwargs={'key': '4'})
        st.button('1', use_container_width=True, on_click=button_clicked, kwargs={'key': '1'})
        st.button('◀', use_container_width=True, on_click=button_clicked, kwargs={'key': '◀'})

    with col2:
        st.button('+/-', use_container_width=True, on_click=button_clicked, kwargs={'key': '+/-'})
        st.button('8', use_container_width=True, on_click=button_clicked, kwargs={'key': '8'})
        st.button('5', use_container_width=True, on_click=button_clicked, kwargs={'key': '5'})
        st.button('2', use_container_width=True, on_click=button_clicked, kwargs={'key': '2'})
        st.button('0', use_container_width=True, on_click=button_clicked, kwargs={'key': '0'})

    with col3:
        st.button('%', use_container_width=True, on_click=button_clicked, kwargs={'key': '%'})
        st.button('9', use_container_width=True, on_click=button_clicked, kwargs={'key': '9'})
        st.button('6', use_container_width=True, on_click=button_clicked, kwargs={'key': '6'})
        st.button('3', use_container_width=True, on_click=button_clicked, kwargs={'key': '3'})
        st.button('.', use_container_width=True, on_click=button_clicked, kwargs={'key': '.'})

    with col4:
        st.button('/', use_container_width=True, on_click=button_clicked, kwargs={'key': '/'})
        st.button('\*', use_container_width=True, on_click=button_clicked, kwargs={'key': '*'})
        st.button('\-', key='minus', use_container_width=True, on_click=button_clicked, kwargs={'key': '-'})
        st.button('\+', key='plus', use_container_width=True, on_click=button_clicked, kwargs={'key': '+'})
        st.button('=', use_container_width=True, on_click=button_clicked, kwargs={'key': '='})

    with col5:
        st.empty()

