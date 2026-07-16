import streamlit as st
from patterns.header import header
from auth.state import require_login

header()

st.set_page_config(layout="wide")
require_login()
