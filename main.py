import streamlit as st

st.title('Weather Forecast for the Next Days')

place=st.text_input('Place')

days=st.slider('Forecast Days',1,5, help='Slide to see data for more dates')

option=st.selectbox('Select data to view',('Tempeture','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')