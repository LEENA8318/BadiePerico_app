# -- coding: utf-8 --
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Hola, mundo")

# Descripción o contenido de la aplicación
st.write("Esta es mi primera aplicación con Streamlit")

# Intentar cargar el archivo CSV
try:
    # Cargar el archivo CSV
    df = pd.read_csv('Clientes_Empresa_Limpiados.csv')  # Ruta relativa al archivo CSV

    # Mostrar la tabla en la aplicación
    st.write("Base de datos de clientes:")
    st.dataframe(df)  # Mostrar los datos en una tabla interactiva
except FileNotFoundError:
    st.error("El archivo 'Clientes_Empresa_Limpiados.csv' no se encontró. Asegúrate de que esté en el mismo directorio que este archivo.") 
except Exception as e:
    st.error(f"Se produjo un error al cargar el archivo: {e}")
