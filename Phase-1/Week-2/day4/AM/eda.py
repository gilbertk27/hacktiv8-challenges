import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def app():
    # title
    st.title('Fifa 2022 Player Rating Prediction')

    # subheader
    st.subheader('EDA utk analisa dataset Fifa 2022')

    # add image
    image = Image.open('bola.jpg')
    st.image(image, caption = 'Fifa 2022')

    # add desc
    st.write('Page ini dibuat oleh Xyncz')
    st.write('# Halo')
    st.write('## Halo')
    st.write('### Halo')

    st.write('**Halo**')
    st.write('*Halo*')

    # Markdown
    st.markdown('----')

    # Masukkan pandas dataframe

    # show dataframe
    df = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/master/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(df)

    # membuat barplot
    st.write('#### Plot AttackingWorkRate')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='AttackingWorkRate', data=df)
    st.pyplot(fig)

    # membuat hist
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df['Overall'], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat hist berdasarkan input
    st.write('#### Histogram based on input user')

    # option 2 (radiobutton) selectbox -> radio
    option = st.selectbox('Pilih Column:', ('Age', 'Weight', 
                                            'Height', 'ShootinTotal'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[option], bins=30, kde=True)
    st.pyplot(fig)

    # Membuat plotly plot
    st.write('#### Plotly Plot - ValueEUR vs Overall')
    fig  = px.scatter(df, x = 'ValueEUR', y = 'Overall', hover_data = ['Name', 'Age'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    app()