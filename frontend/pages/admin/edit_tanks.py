import requests
import streamlit as st

from patterns.header import header
from patterns.tank import render_tank_card_for_edit

from api.client import get_error_message, get_tanks

header()

st.set_page_config(layout="wide")
st.title('Выберите танк для редактирования или удаления танка')

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
        render_tank_card_for_edit(tank)
