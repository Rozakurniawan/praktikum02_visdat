import streamlit as st
import graphviz as graphviz

st.title("graphviz Chart")
st.write("Kelompok 13")
st.markdown("""
- ROZA KURNIAWAN NUR WAKID (0110222124)
- PRAMANA RAHMANSAH PUTRA (0110122051)
- IMAD HASAN AQIL (0110221166)
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algoritma"
        "ML Algoritma" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
    }
""")