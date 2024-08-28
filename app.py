import streamlit as st
from textblob import TextBlob
from googletrans import Translator

st.title('Análisis de Sentimiento')
#image = Image.open('emoticones.jpg')
#st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
