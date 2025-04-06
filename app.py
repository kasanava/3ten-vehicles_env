import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
car_data = pd.read_csv('notebooks/vehicles-us.csv')

#Boton de histograma
hist_button = st.checkbox('Construir histograma')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    hist_fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(hist_fig, use_container_width=True)

#Boton de diagrama de dispersión
disp_button = st.checkbox('Construir diagrama de dispersión')

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    disp_fig = px.scatter(car_data, x="odometer", y='price')
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(disp_fig, use_container_width=True)