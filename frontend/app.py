import streamlit as st

navbar = st.navigation(
    {
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
        ]
    }
)

navbar.run()