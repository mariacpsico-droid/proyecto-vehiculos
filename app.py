import pandas as pd
import plotly.express as px
import streamlit as st

vehicles = pd.read_csv('vehicles_us.csv')

st.header('Analisis de Datos de Vehiculos')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(vehicles, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)