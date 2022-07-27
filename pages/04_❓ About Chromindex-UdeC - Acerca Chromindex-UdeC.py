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
    st.header('About Chromindex-UdeC')

    st.markdown(
        """
        Cytotaxonomy is a branch of cytogenetics, dedicated to the comparative study of karyological traits for
        systematic and evolutionary purposes (Siljak-Yakovlev & Peruzzi 2012). It has been very important in recent
        years because its contribution to the knowledge of the evolution and phylogeny of vascular plants has allowed a
        clearer and more precise understanding of the mechanisms involved in plant diversification.

        Currently, the use of karyotype asymmetry indices, both intra- and interchromosomal, is widely used in plant
        systematics (Paszko 2006; Peruzzi & Eroglu 2013). One of the daily difficulties is the tabular use of the
        generated data. Normally, these data are very numerous and complex to use, which can generate unintentional
        errors that can generate noise in the interpretation of the results. For this reason, the contribution of the
        Chromindex-UdeC program can help to remedy this situation.

        **Chromindex-UdeC** was born from the motivation to create a tool to facilitate the calculation of karyotype
        asymmetry indices, with the idea of speeding up research and avoiding the complex calculations behind these
        indices. Chromindex-UdeC was conceived in the context of the internship of the Data Science Unit of the
        University of Concepción. This internship was a cooperation between the collaborators presented on the home
        page.

        To develop the **Chromindex-UdeC** program, the first step was to create a **Python** script (Rossum & Drake
        2009) capable of reading Excel tables and retrieving values of the different indexes. However, a user-friendly
        interface was also needed so that any researcher could use this tool, without the need to understand
        programming. For this purpose, the **Streamlit** library (https://streamlit.io/) was used. This library allows
        the creation of a web application from Python code without major difficulties. Once the code was obtained, it
        was uploaded to **GitHub** (https://github.com/) to use a server for mounting the application on the web.
        """,
        unsafe_allow_html=True
    )

# CONTENIDO EN ESPAÑOL
else:
    st.header('Acerca Chromindex-UdeC')

    st.markdown(
        """
        La citotaxonomía es una rama de la citogenética, dedicada al estudio comparativo de los rasgos cariológicos de
        **propósitos sistemáticos y evolutivos**!! (Siljak-Yakovlev & Peruzzi 2012). Ha sido muy importante en los últimos
        años porque su contribución al conocimiento de la evolución y filogenia de las plantas vasculares ha permitido
        una comprensión más clara y precisa de los mecanismos implicados en la diversificación de las plantas.

        Actualmente, el uso de índices de asimetría del cariotipo, tanto intra- como intercromosómicos, es ampliamente utilizado en
        **plantas sistemática**!! (Paszko 2006; Peruzzi & Eroglu 2013). Una de las dificultades cotidianas es el uso tabular de los
        datos generados. Normalmente, estos datos son muy numerosos y complejos de utilizar, lo que puede generar
        errores que pueden generar ruido en la interpretación de los resultados. Por ello, la contribución del
        programa Chromindex-UdeC puede ayudar a solucionar esta situación.

        **Chromindex-UdeC** nació de la motivación de crear una herramienta que facilitara el cálculo de los índices de
        asimetría del cariotipo, con la idea de agilizar la investigación y evitar los cálculos complejos que hay detrás de estos
        índices. Chromindex-UdeC fue concebido en el contexto de las prácticas de la Unidad de Data Science de la
        Universidad de Concepción. Esta práctica fue una cooperación entre los colaboradores presentados en la página
        de inicio.

        Para desarrollar el programa **Chromindex-UdeC**, el primer paso fue crear un script en **Python** (Rossum & Drake
        2009) capaz de leer tablas de Excel y obtener los valores de los diferentes índices. Sin embargo, también se
        necesitaba una interfaz fácil de usar para que cualquier investigador pudiera utilizar esta herramienta, sin necesidad de entender
        programación. Para ello se utilizó la librería **Streamlit** (https://streamlit.io/). Esta biblioteca permite
        la creación de una aplicación web a partir de código Python sin mayores dificultades. Una vez desarrollado el código, se
        se subió a **GitHub** (https://github.com/) para usar un servidor y montar en él la aplicación en la web.
        """,
        unsafe_allow_html=True
    )


write_espacios(2)

st.caption("<h10>Van Rossum, G. & Drake, F.L., 2009. Python 3 Reference Manual, Scotts Valley, CA: \
           CreateSpace.</h10>", unsafe_allow_html=True)

#Imagenes al final de la página
st.image('imagenes/banner.png')
