import requests
import streamlit as st
from json import dumps

from api.client import get_error_message, get_tank

from patterns.header import header
from patterns.tank import render_favorite_button

header()

tank_id = st.session_state.get("selected_tank_id")

if tank_id is None:
    st.info("Сначала выберите запись в списке.")
    st.page_link("pages/tanks.py", label="Перейти в список")
    st.stop()

try:
    response = get_tank(tank_id)
except requests.RequestException:
    st.error("Не удалось выполнить запрос к backend.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

tank = response.json()

st.header(tank['title'])
render_favorite_button(tank, key_prefix="details")
