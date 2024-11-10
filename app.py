import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('C:\\Users\\lugon_a5e16xi\\OneDrive\\Documents\\TripleTen\\GIT\\My_project\\vehicles_us.csv') # leer los datos

# Contenido de la aplicación 
st.header("Test Dispersión Del Odómetro VS Precio De Vehículos") # crea el encabezado
"""
hist_button = st.button("Construir histograma") # crea un botón para histograma

if hist_button: # al hacer clic en el botón
    '''
    Crea botón que al hacer clic en él, construya un histograma
    '''
    st.write("Creación de un histograma para el conjunto de datos de anuncios de ventas de coches") # crea mensaje 
    fig = px.histogram(car_data, x="odometer") # crea un histograma
    st.plotly_chart(fig, use_container_width=True) # muestra un gráfico Plotly interactivo

disp_button = st.button("Construir Gráfico De Dispersión") # crea un boton para gráfico de dispersión

if disp_button: # al hacer clic en el botón
    '''
    Crea botón que al hacer clic en él, construya un gráfico de dispersión
    '''
    st.write("Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches")
    fig2 = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
"""
build_hist = st.checkbox("Construir histograma") # crea una casilla de verificación

if build_hist: # al seleccionar 
    '''
    Crea checkbox que al seleccionar, construya un histograma
    '''
    st.write("Creación de un histograma para conjunto de datos de anuncios de venta de coches vs odometer") # crea mensaje
    fig = px.histogram(car_data, x="odometer") # crea histograma
    st.plotly_chart(fig, use_container_width=True) # muestra gráfico

build_disp = st.checkbox("Crea un gráfico de dispersión") # crea una casilla de verificación 

if build_disp:
    '''
    Crea checkbox que al seleccionar, contruya un gráfico de dispersión
    '''
    st.write("Creación de un gráfico de dispersión para conjunto de datos de anuncios de venta de coches vs odometer ")
    fig2 = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True) # muestra gráfico




