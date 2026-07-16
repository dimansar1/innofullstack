import streamlit as st
from auth.state import is_admin

pages = {
        "Авторизация": [
            st.Page("pages/registration.py", title="Регистрация"),
            st.Page("pages/login.py", title="Логин"),
            st.Page("pages/noregistration.py", title="Незарегистрировано"),
        ],
        "Основные страницы": [
            st.Page("pages/tanks.py", title="Список танков"),
            st.Page("pages/tank.py", title="Информация о танке"),
            st.Page("pages/favourites.py", title="Избранное"),
            st.Page("pages/profile.py", title="Профиль"),
        ],
    }

if is_admin():
    pages["Админка"] = [
            st.Page("pages/admin/admin.py", title="Админка"),
            st.Page("pages/admin/create_tank.py", title="Добавить танк"),
            st.Page("pages/admin/edit_tanks.py", title="Редактировать танк"),
            st.Page("pages/admin/update_tank.py", title="Редактирование танка"),
            st.Page("pages/admin/users.py", title="Все пользователи"),
        ]
    
navbar = st.navigation(pages, position='top')

navbar.run()