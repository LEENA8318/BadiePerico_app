# -- coding: utf-8 --
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Hola, mundo")

# Descripción o contenido de la aplicación
st.write("Esta es mi primera aplicación con Streamlit")

# Intentar cargar el archivo CSV
try:
    # Leer el archivo CSV
    df = pd.read_csvdf = pd.read_csv(r'C:\Users\HOLA\Desktop\mi_primera_app\Clientes_Empresa_Limpiados.csv')

    # Mostrar la tabla en la aplicación
    st.write("Base de datos de clientes:")
    st.dataframe(df)
except FileNotFoundError:
    st.error("El archivo 'Clientes_Empresa_Limpiados.csv' no se encontró. Asegúrate de que esté en la misma carpeta que este archivo.")
except Exception as e:
    st.error(f"Se produjo un error al cargar el archivo: {e}")



