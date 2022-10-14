import streamlit as st
import plotly.express as px 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import sys
from Modules import etl


image = Image.open('Image/QR Code.png')

st.sidebar.subheader('🔹 Projeto realizado por Gabriel de Jesus')

st.sidebar.markdown(f'🇧🇷 O projeto tem como principal objetivo utilizar técnicas de NLP para realizar a extração das principais palavras utilizadas\
                    por cada partido político em seu plano de governo, disponibilizado para a eleição para a presidência do Brasil em 2023. \
                    Foram utilizadas como forma de visualização o gráfico de barras e a nuvem de palavras.\
                    Bibliotecas utilizadas: pdfplumber, nltk, wordcloud, plotly.\
                    \n\
                    \n🇺🇸 The main objective of the project is to use NLP techniques to extract the main words used \
                    by each political party in its government plan, made available for the election for the presidency of Brazil in 2023. \
                    The bar graph and the word cloud were used as a form of visualization.\
                    Libraries used: pdfplumber, nltk, wordcloud, plotly.')

st.sidebar.image(image,width=150)
st.sidebar.caption(f'🇧🇷 Para acessar outros projetos ou visualizar meu perfil do LinkedIN escaneie o QR Code \
             \n\
             \n🇺🇸 To access others projects or my LinkedIN profile scan the QR Code')

st.title('Análise de Planos de Governo ')
st.markdown('🇺🇸 - Government Plans Analysis')

suspense_bar = st.selectbox('Selecione um partido', ['DC','MDB', 'NOVO', 'PCB', 'PDT', 'PL','PROS','PSTU','PT','PTB','PUP','UNIÃO BR' ],key="1")

st.subheader('Palavras que mais aparecem nos Planos de Governo')
st.markdown('🇺🇸 - Most Frequent Words in Government Plans')

def create_barchart(suspense_bar):
     if suspense_bar == 'DC':
          topic_barchart = etl.plan_dc
     elif suspense_bar == 'MDB':
          topic_barchart = etl.plan_mdb
     elif suspense_bar == 'NOVO':
          topic_barchart = etl.plan_novo
     elif suspense_bar == 'PCB':
          topic_barchart = etl.plan_pcb       
     elif suspense_bar == 'PDT':
          topic_barchart = etl.plan_pdt     
     elif suspense_bar == 'PL':
          topic_barchart = etl.plan_pl  
     elif suspense_bar == 'PROS':
          topic_barchart = etl.plan_pros
     elif suspense_bar == 'PSTU':
          topic_barchart = etl.plan_pstu
     elif suspense_bar == 'PT':
          topic_barchart = etl.plan_pt   
     elif suspense_bar == 'PTB':
          topic_barchart = etl.plan_ptb   
     elif suspense_bar == 'PUP':
          topic_barchart = etl.plan_pup
     elif suspense_bar == 'UNIÃO BR':
          topic_barchart = etl.plan_uniaobr
     return topic_barchart

topic_barchart = create_barchart(suspense_bar)
st.plotly_chart(px.bar(topic_barchart, x='Word', y='Quantity'))

st.subheader('Nuvem de Palavras')
st.markdown('🇺🇸 - Word Cloud')

topic = st.selectbox('Selecione um partido', ['DC','MDB', 'NOVO', 'PCB', 'PDT', 'PL','PROS','PSTU','PT','PTB','PUP','UNIÃO BR' ],key="2")

def create_wordcloud(topic):
     if topic == 'Opções':
          return None
     elif topic == 'DC':
          topic = etl.all_words_dc
     elif topic == 'MDB':
          topic = etl.all_words_mdb
     elif topic == 'NOVO':
          topic = etl.all_words_novo
     elif topic == 'PCB':
          topic = etl.all_words_pcb
     elif topic == 'PDT':
          topic = etl.all_words_pdt
     elif topic == 'PL':
          topic = etl.all_words_pl
     elif topic == 'PROS':
          topic = etl.all_words_pros
     elif topic == 'PSTU':
          topic = etl.all_words_pstu
     elif topic == 'PT':
          topic = etl.all_words_pt
     elif topic == 'PTB':
          topic = etl.all_words_ptb
     elif topic == 'PUP':
          topic = etl.all_words_pup
     elif topic == 'UNIÃO BR':
          topic = etl.all_words_uniaobr
     else:
          None

     wordcloud = WordCloud(max_words = 30).generate(topic)
     return wordcloud

wordcloud = create_wordcloud(topic)
# Display the generated image:
fig, ax = plt.subplots(figsize = (12, 8), facecolor='k')
ax.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)

