import streamlit as st
import pandas as pd

def main():
    st.title("Hola, mundo")
    st.write("Esta es mi primera aplicación con Streamlit")

    try:
        df = pd.read_csv("Clientes_Empresa_Limpiados.csv")
        st.write("Base de datos de clientes:")
        st.dataframe(df)
    except FileNotFoundError:
        st.error("El archivo 'Clientes_Empresa_Limpiados.csv' no se encontró. Asegúrate de que está en la misma carpeta que este script.")
    except Exception as e:
        st.error(f"Se produjo un error al cargar el archivo: {e}")

if __name__ == "__main__":
    main()
