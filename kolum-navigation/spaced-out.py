import streamlit as st
from PIL import Image

st.title("Spaced-Out Columns")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

img = Image.open("E:\supra.jpg") 
# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1)) 
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)