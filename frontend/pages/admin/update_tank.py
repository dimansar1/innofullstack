import requests
import streamlit as st

from patterns.header import header
from api.client import get_error_message, get_tank, update_tank, load_file

header()

st.set_page_config(layout="wide")
tank_id = st.session_state.get('selected_tank_id')
tank = get_tank(tank_id).json()
st.title('Изменение танка')

with st.form("create_tank_form"):
    title = st.text_input("Название танка", key="title", value=tank.get('title'))
    photo_path = st.file_uploader(
        "Фото танка", type=["jpg", "png", "webp"],
    )
    health = st.text_input("Здоровье танка", key="health", value=tank.get('health'))
    damage = st.text_input("Урон танка", key="damage", value=tank.get('damage'))
    armor = st.text_input("Бронирование танка", key="armor", value=tank.get('armor'))
    history = st.text_input("Историческая справка о танке", key="history", value=tank.get('history'))
    recommendation = st.text_input("Рекомендация по игре на танке", key="recommendation", value=tank.get('recommendation'))
    category = st.text_input("Тип танка", key="category", value=tank.get('category'))
    nation = st.text_input("Нация танка", key="nation", value=tank.get('nation'))
    level = st.text_input("Уровень танка", key="level", value=tank.get('level'))

    submitted = st.form_submit_button("Изменить танк")

if submitted:
    if not title.strip() or not category.strip() or not nation.strip() or not level.strip():
        st.error("Заполните обязательно поля: Название танка, Тип танка, Нация танка, Уровень танка.")
        st.stop()

    try:
        response = update_tank(
            tank_id = tank_id,
            title = title.strip(),
            health = health.strip(),
            damage = damage.strip(),
            armor = armor.strip(),
            history = history.strip(),
            recommendation = recommendation.strip(),
            category = category.strip(),
            nation = nation.strip(),
            level = level.strip(),
        )

        response1 = load_file(tank_id, photo_path)
    except requests.RequestException:
        st.error("Backend недоступен. Проверьте, запущен ли FastAPI.")
        st.stop()

    if response.status_code in (200, 201):
        st.success("Танк успешно добавлен")
        st.switch_page("pages/tanks.py")
    else:
        st.error(get_error_message(response))


