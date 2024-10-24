import streamlit as st


st.set_page_config(
    layout="centered",
    initial_sidebar_state="collapsed",
    page_title="Calculadora de Topes",
    page_icon="🧮",
)
st.sidebar.empty()
st.image("https://i.imgur.com/yAVDAw1.png", use_column_width=True)
st.title("Calculadora de Topes 🧮")
st.write("")

porcentaje = st.number_input("Ingresá el porcentaje de descuento", 1)
limite = st.number_input("Ingresá el tope", 1)
tope = 100/porcentaje*limite
st.subheader(f"Comprá por un máximo de ${tope:,.0f}")