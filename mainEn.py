import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from clases import IndicesDesdeExcel
from io import BytesIO


def xlsdownload(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='openpyxl')
    df.to_excel(writer, index=False)
    writer.save()
    return output.getvalue()


def del_sesion_state(st_key):
    if st_key in st.session_state:
        del st.session_state[st_key]


def add_sesion_state(st_key, value):
    if st_key not in st.session_state:
        st.session_state[st_key] = value


st.set_page_config(layout="wide")

paginas_navegacion = ['Home', 'How to use', 'Index Calculation', 'Documentation', 'About Alstroemeria-UdeC']

col1, _, col2 = st.columns([1, 3, 2])
col1.image('imagenes/logoAPP.bmp')
col2.image('imagenes/udec.gif', use_column_width='always')

with st.sidebar:
    st.image('imagenes/marca_udec2.png')
    st.session_state['idioma'] = st.selectbox('Language', ['English', 'Spanish'])
    st.text('')
    st.text('')
    pag_navegacion_actual = st.radio('Navigate', paginas_navegacion)

if pag_navegacion_actual == paginas_navegacion[0]:
    st.header('Alstroemeria-UdeC')

    """
    **Alstroemeria-UdeC**, a simple way to calculate karyotype asymmetry indices from Excel tables generated with the 
    Micromeasure software (Reeves, 2001).

    Álvaro Guzmán Chacón¹, Carlos Baeza Perry² & Pedro Pinacho Davidson³.

     ¹Facultad de Ciencias Físicas y Matemáticas, Departamento de Ingeniería Civil Matemática,
      Universidad de Concepción, Concepción, Chile.

     ²Facultad de Ciencias Naturales y Oceanográficas, Departamento de Botánica, 
     Universidad de Concepción, Concepción, Chile.

     ³Facultad de Ingeniería, Departamento de Ingeniería Informática y Ciencias de la 
     Computación, Universidad de Concepción, Concepción, Chile.
    """

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

elif pag_navegacion_actual == paginas_navegacion[1]:
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
    Go to the _Index Calculation_ menu and click on the button to upload files. Choose the excel file obtained with 
    MicroMeasure.
    """

    st.image("imagenes/paso2.png", caption="Corresponding menu and button to upload excel file.")

    st.subheader('Step 3:')
    """
    Once the excel file has been uploaded to the web application, a menu will appear to select the indices to be 
    calculated (See *Documentation* to REVIEW!! how the indices are calculated). Select the indices you need and click 
    on the button _Calculate Indices_. If everything was done correctly, a table will be displayed that, for each excel 
    file uploaded (indicated by its name), will show the value of the selected indices to the right. In addition, there 
    is the option to download the displayed table in excel format by clicking on the button _📥 Download as Excel_. 
    The file will be downloaded with the name Indices_dd-mm-yyyy_hhmmss.xlsx, where dd-mm-yyyy and hhmmss correspond, 
    respectively, to the exact date and time at the time of calculating the indices.
    """

    st.image("imagenes/paso3.png",
             caption="Final result: Table with the indices selected for each uploaded file, and download button.")

    st.subheader('In case of errors')

    """
    In case of having errors when using the app, it is recommended to refresh the page. If the problem persists, write 
    an email to the author (alvaroo_98@hotmail.cl) or create an *Issue* on the GitHub page, detailing the problem and 
    attaching images if necessary.
    """

    st.subheader('Test file')
    """
    You can test the web application with the following test excel file. It was obtained with MicroMeasure.
    """

    st.download_button(
        label='📥 Download test Excel file',
        data=open('elementos_web/excel_ejemplo1.xlsx', 'rb'),
        file_name="A. hookeri subsp. hookeri.xlsx",
        mime="application/vnd.ms-excel"
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

elif pag_navegacion_actual == paginas_navegacion[2]:
    st.header('Alstroemeria-UdeC')

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
            df = pd.DataFrame(columns=['File name'] + indices_seleccionados)
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
                label='_📥 Download as Excel_',
                data=st.session_state['df_resultado'],
                file_name=excel_nombre,
                mime="application/vnd.ms-excel",
                on_click=del_sesion_state('df_resultado')
            )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

elif pag_navegacion_actual == paginas_navegacion[3]:
    st.header('Documentation')

    st.markdown("""The source code is aviable ON!! the following GitHub repository:
    <a href="https://github.com/Zekess/Indices_de_asimetria">**Alstromeria-UdeC Repository**</a>.\n""",
                unsafe_allow_html=True)
    st.markdown(""" Below there is a summary of the indices that **Alstromeria-UdeC** includes. Note that in what 
    follows, _n_ represents the total number of chromosomes. Also the standard deviation corresponds to the sample 
    standard deviation (unbiased).""", unsafe_allow_html=True)

    # st.markdown("<h4>A<sub>1</sub> (Romero Zarco, 1986)</h4>", unsafe_allow_html=True)
    # st.markdown("El índice __A<sub>1</sub>__ es calculado de la siguiente forma:", unsafe_allow_html=True)
    # st.latex(r'A_1 = 1 - \frac{\sum_{i=1}^n\frac{b_i}{B_i}}{n_p}.')
    # st.markdown('Donde ___b_<sub>i</sub>__ y ___B_<sub>i</sub>__ corresponden, respectivamente, al largo promedio de los brazos\
    # cortos y al largo promedio de los brazos largos del _i_-ésimo par de cromosomas homólgos. Y ___n<sub>p</sub>___ es la \
    # cantidad de pares de cromosomas.', unsafe_allow_html=True)

    st.markdown("<h4>A<sub>2</sub> (Romero Zarco, 1986)</h4>", unsafe_allow_html=True)
    st.markdown("The index __A<sub>2</sub>__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'A_2 = \frac{s}{x}.')
    st.markdown("""Where ___s___ and ___x___ are the standard deviation and the mean of the length of 
    chromosomes.""", unsafe_allow_html=True)

    st.markdown("<h4>Ask% (Arano y Saito, 1980)</h4>", unsafe_allow_html=True)
    st.markdown("The index __Ask%__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'Ask\% = \frac{\sum_{i=1}^n L_i}{\sum_{i=1}^n L_i+l_i}.')
    st.markdown("""Where ___L<sub>i</sub>___ and ___l<sub>i</sub>___ are the length of the longest arm and the length of
     the shortest arm of the _i_-th chromosome, respectively. That is, this index is calculated as the sum of the lengths 
     of the long arms divided by the sum of the lengths of all the chromosomes.""", unsafe_allow_html=True)

    st.markdown("<h4>CV<sub>CI</sub> (Paszko, 2006)</h4>", unsafe_allow_html=True)
    st.markdown("The index __CV<sub>CI</sub>__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'CV_{CI} = \frac{s_{CI}}{x_{CI}}\times 100.')
    st.markdown("""Where ___s<sub>CI</sub>___ and ___x<sub>CI</sub>___ are the standard deviation and the mean of the 
    centromeric indices, respectively.""", unsafe_allow_html=True)

    st.markdown("<h4>CV<sub>CL</sub>  (Peruzzi y Eroglu, 2013)</h4>", unsafe_allow_html=True)
    st.markdown("The index __CV<sub>CL</sub>__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'CV_{CL}= A_2 \times 100.')
    st.markdown("""Where ___A<sub>2</sub>___ corresponds to the index proposed by Romero Zarco, previously shown.""",
                unsafe_allow_html=True)

    st.markdown("<h4>M<sub>CA</sub>  (Peruzzi y Eroglu, 2013)</h4>", unsafe_allow_html=True)
    st.markdown("The index __M<sub>CA</sub>__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'M_{CA} = \frac{\sum_{i=1}^n \frac{L_i-l_i}{L_i+l_i}}{n} \times 100.')
    st.markdown("""Where ___L<sub>i</sub>___ and ___l<sub>i</sub>___ are the length of the longest arm and the length of 
    the shortest arm of the _i_-th chromosome, respectively.""", unsafe_allow_html=True)

    st.markdown("<h4>Sy<sub>i</sub>  (Greihuber y Speta, 1976)</h4>", unsafe_allow_html=True)
    st.markdown("The index __Sy<sub>i</sub>__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'Sy_i = \frac{x_l}{x_L} \times 100.')
    st.markdown("""Where ___x<sub>l</sub>___ and ___x<sub>L</sub>___ are the mean lengths of the short arms and the 
    mean lengths of the long arms, respectively.""", unsafe_allow_html=True)

    st.markdown("<h4>TF% (Huziwara, 1962)</h4>", unsafe_allow_html=True)
    st.markdown("The index __TF%__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'TF\% = \frac{\sum_{i=1}^n l_i}{\sum_{i=1}^n L_i+l_i}.')
    st.markdown("""Where ___L<sub>i</sub>___ and ___l<sub>i</sub>___ are the length of the longest arm and the length 
    of the shortest arm of the _i_-th chromosome, respectively. That is, this index is calculated as the sum of the 
    lengths of the short arms divided by the sum of the lengths of all the chromosomes. Note that Ask%+TF%=1 for any 
    set of chromosomes.""", unsafe_allow_html=True)

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.caption("<h10>Greilhuber, J., Speta. F. 1976. C-banded karyotypes in the Scilla hohenackeri group, S. persica, \
    and Puschkinia (Liliaceae). Plant Systematics and Evolution 126: 149-188.</h10>", unsafe_allow_html=True)
    st.caption("<h10>Huziwara, Y. 1962. Karyotype analysis in some genera of Compositae. VIII. Further studies on \
    the chromosomes of Aster. American Journal of Botany 49:116-119.</h10>", unsafe_allow_html=True)
    st.caption("<h10>Paszko, B. 2006. A critical review and a new proposal of karyotype asymmetry indices. \
    Plant Systematics and Evolution 258: 39-48.</h10>", unsafe_allow_html=True)
    st.caption("<h10>Peruzzi, L., Eroglu. H. 2013. Karyotype asymmetry: ¿again, how to measure and what \
    to measure?  Comparative Cytogenetics 7: 1-9.</h10>", unsafe_allow_html=True)
    st.caption("<h10>Romero Zarco, C. 1986. A new method for estimating Karyotype asymmetry. \
    Taxon 36: 526-530.</h10>", unsafe_allow_html=True)

elif pag_navegacion_actual == paginas_navegacion[4]:
    st.header('About Alstroemeria-UdeC')

    st.markdown(
        """
        **Alstroemeria-UdeC** was born from the motivation to create a tool to facilitate the calculation of karyotype 
        asymmetry indices, with the idea of speeding up the research and avoid going through the complex calculation 
        behind these indices. Alstroemeria-UdeC was conceived in the context of the internship of the Data Science Unit 
        of the University of Concepción. This internship was a cooperation between the collaborators presented on the 
        _Home_ page.
        
        To develop the **Alstroemeria-UdeC** program, the first step was to create a **Python** script (Rossum & Drake 
        2009) capable of solving the problem (reading Excel tables and returning the value of the different indexes). 
        However, a user-friendly interface was also needed so that any researcher could use this tool, without the need 
        to understand programming. For this purpose, the **Streamlit** library (https://streamlit.io/) was used. This 
        library allows the creation of a web application from Python code without major difficulties. Once the code was 
        obtained, it was uploaded to **GitHub** (https://github.com/)  to use a server to mount the application on the 
        web.
        """,
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.caption("<h10>Van Rossum, G. & Drake, F.L., 2009. Python 3 Reference Manual, Scotts Valley, CA: \
               CreateSpace.</h10>", unsafe_allow_html=True)

st.image('imagenes/banner.png')
