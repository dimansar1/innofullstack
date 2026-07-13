import requests 
import streamlit as st

from auth.state import is_authenticated
from api.client import get_error_message, get_favourite_by_tank_id, add_favourite, remove_favourite

def render_tank_card(tank: dict) -> None:
    tank_id = tank["id"]

    with st.container(border=True):
        if tank.get("photo_path") != '-':
            st.image(tank["photo_path"], use_container_width=True)
        else:
            st.info("Изображение не добавлено")

        st.subheader(tank["title"])

        if st.button("Подробнее", key=f"card_details_{tank_id}"):
            st.session_state["selected_tank_id"] = tank_id
            st.switch_page("pages/tank.py")


def render_favorite_button(tank: dict, key_prefix: str) -> None:
    if not is_authenticated():
        st.caption("Войдите, чтобы добавить запись в избранное.")
        return

    tank_id = tank["id"]
    is_favorite = get_favourite_by_tank_id(tank_id)
    button_text = "Убрать из избранного" if is_favorite.status_code == 200 else "В избранное"

    if st.button(button_text, key=f"{key_prefix}_favorite_{tank_id}"):
        try:
            if is_favorite:
                response = remove_favourite(tank_id)
            else:
                response = add_favourite(tank_id)
        except requests.RequestException:
            st.error("Не удалось выполнить запрос к backend.")
            return

        if response.ok:
            st.rerun()
        else:
            st.error(get_error_message(response))
