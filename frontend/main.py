# main.py
# Responsável pelos setups e pela inicialização do Streamlit

import streamlit as st
from src.views.chat_view import render_chat_view

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Rocket Chat",
    page_icon="🚀",
    layout="centered"
)

# Inicialização do histórico de mensagens no estado da sessão
if "messages" not in st.session_state:
    st.session_state.messages = []

# Renderiza a view principal do chat
render_chat_view()