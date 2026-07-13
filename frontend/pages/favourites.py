import requests
import streamlit as st

from api.client import get_error_message, get_favourites, get_tank

from patterns.tank import render_tank_card
from patterns.header import header

from patterns.cookie import controller

header()

st.title("Избранное")

try:
    response = get_favourites()
except requests.RequestException:
    st.error("Не удалось выполнить запрос к backend.")
    st.stop()

if not response.ok:
    st.error(get_error_message(response))
    st.stop()

favourites = response.json()

if not favourites:
    st.info("В избранном пока ничего нет.")
    st.stop()

for favourite in favourites:
    tank_id = favourite.get('tank_id')
    tank = get_tank(tank_id).json()
    render_tank_card(tank)