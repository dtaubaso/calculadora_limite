import streamlit as st


st.set_page_config(
    layout="centered",
    initial_sidebar_state="collapsed",
    page_title="Calculadora de Topes",
    page_icon="🧮",
)

# Aplicar CSS personalizado
st.markdown("""
    <style>
            .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    .input-box {
        font-size: 18px; /* Tamaño de texto en los input */
        width: 200px; /* Tamaño del input box */
    }
    div[class*="stNumberInput"] label p {
  font-size: 20px;
  
}
    .stApp {
        max-width: 600px; /* Ancho máximo del contenedor */
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# Imagen y título
st.sidebar.empty()
st.title("Calculadora de Topes", )
st.image("https://i.imgur.com/yAVDAw1.png", use_column_width=True)
st.write("Esta app ayuda a calcular cuál es el tope que podés gastar para aprovechar una promoción con máximo de devolución.")

st.write("")

# Inputs con clases CSS personalizadas
porcentaje = st.number_input("Ingresá el porcentaje de descuento", 1, key="input1", format="%d", help="Valor en porcentaje", step=1)
limite = st.number_input("Ingresá el tope de devolución", 1, key="input2", format="%d", help="Límite en pesos", step=1)

# Cálculo y resultado
tope = (100 / porcentaje) * limite
st.subheader(f"Comprá por un máximo de ${tope:,.0f}")
st.write("")
#cafecito = '<a href="https://cafecito.app/daezta" rel="noopener" target="_blank"><p style="font-size: 12px;">Si te sirvió, invitame un café en cafecito.app</p></a>'
#st.markdown(cafecito, unsafe_allow_html=True)
st.markdown(body="[![Invitame un café en cafecito.app](https://cdn.cafecito.app/imgs/buttons/button_4.svg)](https://cafecito.app/daezta)")
st.write("")