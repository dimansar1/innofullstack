import streamlit as st

from patterns.header import header

header()

st.set_page_config(layout="wide")
st.title('Добро пожаловать в админку!')

st.subheader('Танки')
if st.button('Добавить танк'):
    st.switch_page('pages/admin/create_tank.py')

if st.button('Редактировать танк'):
    st.switch_page('pages/admin/edit_tanks.py')

st.subheader('Пользователи')
if st.button('Посмотреть всех пользователей'):
    st.switch_page('pages/admin/users.py')
