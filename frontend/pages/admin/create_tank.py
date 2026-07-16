import requests
import streamlit as st

from patterns.header import header
from api.client import get_error_message, get_tank, create_tank, load_file

header()

st.set_page_config(layout="wide")
st.title('Добавление танка')

with st.form("create_tank_form"):
    title = st.text_input("Название танка", key="title")
    photo_path = st.file_uploader(
        "Фото танка", type=["jpg", "png", "webp"]
    )
    health = st.text_input("Здоровье танка", key="health", value='-')
    damage = st.text_input("Урон танка", key="damage", value='-')
    armor = st.text_input("Бронирование танка", key="armor", value='-')
    history = st.text_input("Историческая справка о танке", key="history", value='Историческая справка о данном танке отсутствует')
    recommendation = st.text_input("Рекомендация по игре на танке", key="recommendation", value='Рекомендации по игре на данном танке отсутстуют')
    category = st.text_input("Тип танка", key="category")
    nation = st.text_input("Нация танка", key="nation")
    level = st.text_input("Уровень танка", key="level")

    submitted = st.form_submit_button("Добавить танк")

if submitted:
    if not title.strip() or not category.strip() or not nation.strip() or not level.strip():
        st.error("Заполните обязательно поля: Название танка, Тип танка, Нация танка, Уровень танка.")
        st.stop()

    try:
        response = create_tank(
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

        tank_id = response.json().get('id')
        response1 = load_file(tank_id, photo_path)
    except requests.RequestException:
        st.error("Backend недоступен. Проверьте, запущен ли FastAPI.")
        st.stop()

    if response.status_code in (200, 201):
        st.success("Танк успешно добавлен")
        st.switch_page("pages/tanks.py")
    else:
        st.error(get_error_message(response))


