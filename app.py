import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from textblob import Word

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
        
if trans_text:

    opcion_elegida = st.selectbox(
        "Que quieres procesar en tu texto would you like to be contacted?",
        ("Oraciones en el párrafo", "Sinónimo", "Definición"),
    )
    
    # Ejecutar código según la opción seleccionada
    if opcion_elegida == "Oraciones en el párrafo":
        st.write("Has elegido la Opción 1. Aquí va el código específico para esta opción:")
        # Código para la Opción 1
        st.write("print('Hola desde la Opción 1')")
        print("Tenemos", len(trans_text.sentences), "oraciones.\n")
        for sentence in trans_text.sentences:
            st.write(sentence)
            st.write("-" * 75)
    
    elif opcion_elegida == "Sinónimo":
        st.write("Has elegido la Opción 2. Aquí va el código específico para esta opción:")
        # Código para la Opción 2
        st.write("Hola desde la Opción 2")
    else:
        st.write("Has elegido la Opción 3. Aquí va el código específico para esta opción:")
        # Código para la Opción 3
        st.write("Hola desde la Opción")

