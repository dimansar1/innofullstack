import requests
import streamlit as st

from api.client import get_error_message, get_tanks

from patterns.tank import render_tank_card
from patterns.header import header

header()

st.set_page_config(layout="wide")
st.title("Список танков")

try:
    response = get_tanks()
except requests.RequestException:
    st.error("Backend недоступен. Проверьте запуск FastAPI.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

tanks = response.json()

if not tanks:
    st.info("В каталоге пока нет записей.")
    st.stop()

columns = st.columns(4)

for index, tank in enumerate(tanks):
    with columns[index % 4]:
        render_tank_card(tank)