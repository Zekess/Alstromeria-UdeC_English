import streamlit as st
from utilidades import *

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
    st.header('How to use')

    st.subheader('Step 1:')
    """
    MicroMeasure is a scientific image analysis program, whose application is intended for cytological, cytogenetic and
    cytotaxonomic studies. This program receives images in a specific format and, through internal calculations, returns
    an excel with important information on the karyotype under study.
    """

    st.image("imagenes/paso1.png", caption="Example of Excel obtained from MicroMeasure.")

    st.subheader('Step 2:')
    """
    Go to the 🥀 __Index Calculation - Calculos de Indices__ menu and click on the button to upload files. Choose the excel file obtained with
    MicroMeasure.
    """

    st.image("imagenes/paso2_eng.png", caption="Corresponding menu and button to upload excel file.")

    st.subheader('Step 3:')
    """
    Once the excel file has been uploaded to the web application, a menu will appear to select the indices to be
    calculated (See __📃 Documentation - Documentacion__ to revise how the indices are calculated). Select the indices you need and click
    on the button _Calculate Indices_. If everything was done correctly, a table will be displayed that, for each excel
    file uploaded (indicated by its name), will show the value of the selected indices to the right. In addition, there
    is the option to download the displayed table in excel format by clicking on the button 📥 _Download as Excel_.
    The file will be downloaded with the name Indices_dd-mm-yyyy_hhmmss.xlsx, where dd-mm-yyyy and hhmmss correspond,
    respectively, to the exact date and time at the time of calculating the indices.
    """

    st.image("imagenes/paso3_eng.png",
             caption="Final result: Table with the indices selected for each uploaded file, and download button.")

    st.subheader('In case of errors')

    st.markdown("""In case of having errors when using the app, it is recommended to refresh the page. If the problem persists, write\
    an email to the author (alvaroo.g98@gmail.com) or create an *Issue* on the \
    <a href="https://github.com/Zekess/Indices_de_asimetria">**GitHub**</a>  page (See __📃 Documentation - Documentacion__), \
    detailing the problem and attaching images if necessary.""", unsafe_allow_html=True)

    st.subheader('Test file')
    """
    You can test Chromidex-UdeC with the following test excel file. It was obtained with MicroMeasure.
    """

    st.download_button(
        label='📥 Download test Excel file',
        data=open('elementos_web/excel_ejemplo1.xlsx', 'rb'),
        file_name="A. hookeri subsp. hookeri.xlsx",
        mime="application/vnd.ms-excel"
    )

# CONTENIDO EN ESPAÑOL
else:
    st.header('Instrucciones de Uso')

    st.subheader('Paso 1:')
    """
    MicroMeasure es un programa científico de análisis de imágenes, cuya aplicación está destinada a estudios citológicos, citogenéticos y
    estudios citotaxonómicos. Este programa recibe imágenes en un formato específico y, a través de cálculos internos, devuelve
    un excel con información importante sobre el cariotipo en estudio.
    """

    st.image("imagenes/paso1.png", caption="Ejemplo de Excel obtenido con MicroMeasure.")

    st.subheader('Paso 2:')
    """
    Vaya al menú __🥀 Index Calculation - Calculos de Indices__ y haga clic en el botón para cargar archivos. Elija el archivo Excel obtenido con
    MicroMeasure.
    """

    st.image("imagenes/paso2_esp.png", caption="Menú correspondiente y botón para cargar archivo excel..")

    st.subheader('Paso 3:')
    """
    Una vez subido el archivo excel a la aplicación web, aparecerá un menú para seleccionar los índices a
    calcular (Ver __📃 Documentation - Documentacion__ para revisar cómo se calculan los índices). Seleccione los índices que necesita y haga clic en
    en el botón _Calcular Indices_. Si todo se hizo correctamente, se mostrará una tabla que, por cada excel
    cargado (indicado por su nombre), mostrará el valor de los índices seleccionados hacia la derecha. Además, está
    la opción de descargar la tabla mostrada en formato excel haciendo clic en el botón 📥 _Descargar como Excel_.
    El archivo será descargado con el nombre Indices_dd-mm-yyyy_hhmmss.xlsx, donde dd-mm-yyyy y hhmmss corresponden,
    respectivamente, a la fecha y hora exacta al momento en que se calcularon los indices.
    """

    st.image("imagenes/paso3_esp.png",
             caption="Resultado final: Tabla con los índices seleccionados por cada archivo subido, además del botón de descarga.")

    st.subheader('En caso de errores')

    st.markdown("""En caso de tener errores al usar la aplicación, se recomienda recargar la página. \
    Si el problema persiste, puede escribir un correo al autor (alvaroo.g98@gmail.com) o crear un *Issue* \
    en la página de <a href="https://github.com/Zekess/Indices_de_asimetria">**GitHub**</a> (Ver __📃 Documentation - Documentacion__),\
    detallando el problema y adjuntando imágenes de ser necesario.""", unsafe_allow_html=True)

    st.subheader('Archivo de prueba')
    """
    Puede probar Chromindex-Udec con el siguiente archivo excel de prueba. Fue obtenido con MicroMeasure-
    """

    st.download_button(
        label='📥 Descargar archvo Excel de prueba',
        data=open('elementos_web/excel_ejemplo1.xlsx', 'rb'),
        file_name="A. hookeri subsp. hookeri.xlsx",
        mime="application/vnd.ms-excel"
    )


#Imagenes al final de la página
write_espacios(3)
st.image('imagenes/banner.png')
