import streamlit as st

st.set_page_config(
    page_title="Hello World",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Esse é um teste")

arquivo = st.file_uploader("Upload de arquivo", type="pdf")

if arquivo:
    st.success("Arquivo enviado com sucesso")


