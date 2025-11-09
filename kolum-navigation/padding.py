import streamlit as st
from PIL import Image

st.title("Padding")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

img = Image.open("E:/supra.jpg")

# Defining Padding with columns
col1, padding, col2 = st.columns((10,2,10))

with col1:
    col1.image(img)

with col2:
    col2.image(img)