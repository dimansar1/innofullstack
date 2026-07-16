import requests
import streamlit as st

from api.client import get_error_message, get_tank, get_media_url

from patterns.header import header
from patterns.tank import render_favorite_button

header()

st.set_page_config(layout="wide")
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
left, right = st.columns(2, vertical_alignment='center')

photo_url = get_media_url(tank.get("photo_path"))

if not photo_url:
    left.info('Изображение не добавлено')
else:
    left.image(photo_url, width='stretch')

col_info, col_favourite = right.columns(2, vertical_alignment='center')
col_info.title(tank.get('title'))
col_info.write(f"Уровень: {tank.get('level')}")
col_info.write(f"Тип: {tank.get('category')}")
col_info.write(f"Нация: {tank.get('nation')}")
col_info.write(f"Здоровье: {tank.get('health')}")
col_info.write(f"Урон: {tank.get('damage')}")
col_info.write(f"Бронирование: {tank.get('armor')}")

with col_favourite:
    render_favorite_button(tank, key_prefix="details")

st.subheader('Историческая справка')
st.write(tank.get('history'))

st.subheader('Рекомендации')
st.write(tank.get('recommendation'))
