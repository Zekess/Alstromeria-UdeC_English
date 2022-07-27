import streamlit as st
from utilidades import *
from IndexCalc import *

#Configuracion de la página (como se ve la pestaña del navegador, layout de la pagina, etc)
st.set_page_config(
page_title="Chromidex-UdeC",
page_icon="imagenes/logoAPP.jpeg",
layout="wide"
)

#Elementos de ls sidebar (ícono uded)
leng = lenguaje_selectbox()
write_espacios_sbar(30)
st.sidebar.image("imagenes/marca_udec2.png")


#AQUI COMIENZA EL CONTENIDO DE LA PAGINA (CUERPO)

#Imagenes al inicio
col1, _, col2 = st.columns([1, 3, 2])
col1.image('imagenes/logoAPP.jpeg')
col2.image('imagenes/udec.gif', use_column_width='always')


# CONTENIDO EN INGLES
if leng == lenguajes[0]:
    st.header('Chromindex-UdeC')

    ## Uploades de los excels:
    lista_excels = st.file_uploader('Upload files', type=['xls', 'xlsx'], accept_multiple_files=True,
                                    on_change=add_sesion_state('uploader_key', 1))

    indices_nombres = [u'A\u2082', 'Ask%', 'CVCI', 'CVCL', 'MCA', 'Syi', 'TF%']

    if ('uploader_key' in st.session_state) & (len(lista_excels) > 0):
        container_multiselect = st.container()
        check_all = st.checkbox('Select all')
        if check_all:
            indices_seleccionados = container_multiselect.multiselect('Multiselect', indices_nombres, indices_nombres)
        else:
            indices_seleccionados = container_multiselect.multiselect('Multiselect', indices_nombres)
        if st.button('Calculate Indices'):
            df = pd.DataFrame(columns=['File'] + indices_seleccionados)
            for uploader in lista_excels:
                indices_clase = IndicesDesdeExcel(uploader)
                indices_dicc = indices_clase.calcular_indices(indices_seleccionados)
                excel_nombre = uploader.name.split('.xls')[0]
                df.loc[len(df) + 1] = [excel_nombre] + list(indices_dicc.values())
            df
            add_sesion_state('df_resultado', xlsdownload(df))
        if 'df_resultado' in st.session_state:
            fecha_hoy = datetime.now().strftime(r"%d-%m-%Y_%Hh%Mm%Ss")
            excel_nombre = f'Indices_{fecha_hoy}.xlsx'
            st.download_button(
                label='📥 Download as Excel',
                data=st.session_state['df_resultado'],
                file_name=excel_nombre,
                mime="application/vnd.ms-excel",
                on_click=del_sesion_state('df_resultado')
            )

# CONTENIDO EN ESPAÑOL
else:
    st.header('Chromindex-UdeC')

    ## Uploades de los excels:
    lista_excels = st.file_uploader('Cargar archivos', type=['xls', 'xlsx'], accept_multiple_files=True,
                                    on_change=add_sesion_state('uploader_key', 1))

    indices_nombres = [u'A\u2082', 'Ask%', 'CVCI', 'CVCL', 'MCA', 'Syi', 'TF%']

    if ('uploader_key' in st.session_state) & (len(lista_excels) > 0):
        container_multiselect = st.container()
        check_all = st.checkbox('Seleccionar todos')
        if check_all:
            indices_seleccionados = container_multiselect.multiselect('Multiselect', indices_nombres, indices_nombres)
        else:
            indices_seleccionados = container_multiselect.multiselect('Multiselect', indices_nombres)
        if st.button('Calcular Indices'):
            df = pd.DataFrame(columns=['Archivo'] + indices_seleccionados)
            for uploader in lista_excels:
                indices_clase = IndicesDesdeExcel(uploader)
                indices_dicc = indices_clase.calcular_indices(indices_seleccionados)
                excel_nombre = uploader.name.split('.xls')[0]
                df.loc[len(df) + 1] = [excel_nombre] + list(indices_dicc.values())
            df
            add_sesion_state('df_resultado', xlsdownload(df))
        if 'df_resultado' in st.session_state:
            fecha_hoy = datetime.now().strftime(r"%d-%m-%Y_%Hh%Mm%Ss")
            excel_nombre = f'Indices_{fecha_hoy}.xlsx'
            st.download_button(
                label='📥 Descargar como Excel',
                data=st.session_state['df_resultado'],
                file_name=excel_nombre,
                mime="application/vnd.ms-excel",
                on_click=del_sesion_state('df_resultado')
            )

#Imagenes al final de la página
write_espacios(21)
st.image('imagenes/banner.png')
