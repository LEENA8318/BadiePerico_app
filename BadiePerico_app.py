# -- coding: utf-8 --
import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Gestión de Clientes")

# Descripción de la aplicación
st.write("Esta es mi primera aplicación con Streamlit con búsqueda avanzada")

# Intentar cargar el archivo CSV
try:
    # Cargar el archivo CSV
    df = pd.read_csv('Clientes_Empresa_Limpiados.csv')  # Ruta relativa al archivo CSV

    # Mostrar la tabla completa al inicio
    st.write("Base de datos completa:")
    st.dataframe(df)

    # Filtros de búsqueda
    st.subheader("Filtros de búsqueda")

    # Entrada de búsqueda por código
    codigo = st.text_input("Buscar por código")

    # Entrada de búsqueda por apellido
    apellido = st.text_input("Buscar por apellido")

    # Entrada de búsqueda por nombre
    nombre = st.text_input("Buscar por nombre")

    # Entrada de búsqueda por dirección
    direccion = st.text_input("Buscar por dirección")

    # Filtrar el dataframe según los criterios ingresados
    if codigo:
        df = df[df['Codigo'].astype(str).str.contains(codigo, case=False, na=False)]
    if apellido:
        df = df[df['Apellido'].str.contains(apellido, case=False, na=False)]
    if nombre:
        df = df[df['Nombre'].str.contains(nombre, case=False, na=False)]
    if direccion:
        df = df[df['Direccion'].str.contains(direccion, case=False, na=False)]

    # Mostrar los resultados filtrados
    st.write("Resultados de búsqueda:")
    st.dataframe(df)

except FileNotFoundError:
    st.error("El archivo 'Clientes_Empresa_Limpiados.csv' no se encontró. Asegúrate de que esté en la misma carpeta que este archivo.")
except Exception as e:
    st.error(f"Se produjo un error al cargar el archivo: {e}")
