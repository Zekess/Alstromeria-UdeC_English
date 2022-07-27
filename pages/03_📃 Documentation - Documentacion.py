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
    st.header('Documentation')

    st.markdown("""The source code is aviable at the following GitHub repository:
    <a href="https://github.com/Zekess/Indices_de_asimetria">**Chromindex-UdeC Repository**</a>.\n""",
                unsafe_allow_html=True)
    st.markdown(""" Below there is a summary of the indices that **Chromindex-UdeC** includes. Note that in what
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
    st.markdown("""Where ___x<sub>l</sub>___ and ___x<sub>L</sub>___ are the mean length of the short arms and the
    mean length of the long arms, respectively.""", unsafe_allow_html=True)

    st.markdown("<h4>TF% (Huziwara, 1962)</h4>", unsafe_allow_html=True)
    st.markdown("The index __TF%__ is calculated in the following way:", unsafe_allow_html=True)
    st.latex(r'TF\% = \frac{\sum_{i=1}^n l_i}{\sum_{i=1}^n L_i+l_i}.')
    st.markdown("""Where ___L<sub>i</sub>___ and ___l<sub>i</sub>___ are the length of the longest arm and the length
    of the shortest arm of the _i_-th chromosome, respectively. That is, this index is calculated as the sum of the
    lengths of the short arms divided by the sum of the lengths of all the chromosomes. Note that Ask%+TF%=1 for any
    set of chromosomes.""", unsafe_allow_html=True)

# CONTENIDO EN ESPAÑOL
else:
    st.header('Documentación')

    st.markdown("""El código fuente está disponible en el siguiente repositorio de GitHub:
    <a href="https://github.com/Zekess/Indices_de_asimetria">**Chromindex-UdeC Repository**</a>.\n""",
                unsafe_allow_html=True)
    st.markdown(""" A continuación se detallan los índices que **Chromidex-UdeC** incluye. Notar que
    en lo que sigue, _n_ representa el número total de cromosomas. Además, la desviación estandar corresponde
    a la desviación estandar de la muestra de cromosomas (insesgada).""", unsafe_allow_html=True)

    # st.markdown("<h4>A<sub>1</sub> (Romero Zarco, 1986)</h4>", unsafe_allow_html=True)
    # st.markdown("El índice __A<sub>1</sub>__ es calculado de la siguiente forma:", unsafe_allow_html=True)
    # st.latex(r'A_1 = 1 - \frac{\sum_{i=1}^n\frac{b_i}{B_i}}{n_p}.')
    # st.markdown('Donde ___b_<sub>i</sub>__ y ___B_<sub>i</sub>__ corresponden, respectivamente, al largo promedio de los brazos\
    # cortos y al largo promedio de los brazos largos del _i_-ésimo par de cromosomas homólgos. Y ___n<sub>p</sub>___ es la \
    # cantidad de pares de cromosomas.', unsafe_allow_html=True)

    st.markdown("<h4>A<sub>2</sub> (Romero Zarco, 1986)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __A<sub>2</sub>__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'A_2 = \frac{s}{x}.')
    st.markdown("""Donde ___s___ y ___x___ son la desviación estandar y la meda de las longitudes de los
    cromosomas.""", unsafe_allow_html=True)

    st.markdown("<h4>Ask% (Arano y Saito, 1980)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __Ask%__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'Ask\% = \frac{\sum_{i=1}^n L_i}{\sum_{i=1}^n L_i+l_i}.')
    st.markdown("""Donde ___L<sub>i</sub>___ and ___l<sub>i</sub>___ son la longitud del brazo más largo y la longitud del
    brazo más corto del cromosoma _i_-ésimo, respectivamente. Es decir, este índice se calcula como la suma de las longitudes
    de los brazos largos dividido por la suma de las longitudes de todos los cromosomas.""", unsafe_allow_html=True)

    st.markdown("<h4>CV<sub>CI</sub> (Paszko, 2006)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __CV<sub>CI</sub>__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'CV_{CI} = \frac{s_{CI}}{x_{CI}}\times 100.')
    st.markdown("""Donde ___s<sub>CI</sub>___ y ___x<sub>CI</sub>___ son la desviación estándar y la media de
    los índices centroméricos, respectivamente.""", unsafe_allow_html=True)

    st.markdown("<h4>CV<sub>CL</sub>  (Peruzzi y Eroglu, 2013)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __CV<sub>CL</sub>__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'CV_{CL}= A_2 \times 100.')
    st.markdown("""Donde ___A<sub>2</sub>___ corresponde al índice propuesto por Romero Zarco, mostrado anteriormente.""",
                unsafe_allow_html=True)

    st.markdown("<h4>M<sub>CA</sub>  (Peruzzi y Eroglu, 2013)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __M<sub>CA</sub>__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'M_{CA} = \frac{\sum_{i=1}^n \frac{L_i-l_i}{L_i+l_i}}{n} \times 100.')
    st.markdown("""Donde ___L<sub>i</sub>___ y ___l<sub>i</sub>___ son la longitud del brazo más largo y la longitud del
    brazo más corto del cromosoma _i_-ésimo, respectivamente.""", unsafe_allow_html=True)

    st.markdown("<h4>Sy<sub>i</sub>  (Greihuber y Speta, 1976)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __Sy<sub>i</sub>__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'Sy_i = \frac{x_l}{x_L} \times 100.')
    st.markdown("""Donde ___x<sub>l</sub>___ y ___x<sub>L</sub>___ son la longitud media de los brazos cortos y la
    longitud media de los brazos largos, respectivamente.""", unsafe_allow_html=True)

    st.markdown("<h4>TF% (Huziwara, 1962)</h4>", unsafe_allow_html=True)
    st.markdown("El indice __TF%__ se calcula de la siguiente manera:", unsafe_allow_html=True)
    st.latex(r'TF\% = \frac{\sum_{i=1}^n l_i}{\sum_{i=1}^n L_i+l_i}.')
    st.markdown("""Donde ___L<sub>i</sub>___ y ___l<sub>i</sub>___ son la longitud del brazo más largo y la longitud
    del brazo más corto del cromosoma _i_-ésimo, respectivamente. Es decir, este índice se calcula como la suma de las
    longitudes de los brazos cortos dividido por la suma de las longitudes de todos los cromosomas. Notar que Ask%+TF%=1
    para cualquier conjunto de cromosomas.""", unsafe_allow_html=True)


write_espacios(2)

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

#Imagenes al final de la página
st.image('imagenes/banner.png')
