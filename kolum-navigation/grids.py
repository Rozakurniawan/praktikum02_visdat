import streamlit as st
from PIL import Image

st.title("Grids")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

img = Image.open("E:/supra.jpg")

# Defining no of Rows
for a in range(4):
    # Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)