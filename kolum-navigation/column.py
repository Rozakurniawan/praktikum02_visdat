import streamlit as st

st.title("Columns")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama.")
col1.image("E:\supra.jpg")
col2.write("Ini adalah kolom kedua.")
col2.image("E:\m4.jpg")
