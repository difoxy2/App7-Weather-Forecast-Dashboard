import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Weather Forecast for the Next Days')

place=st.text_input('Place')

days=st.slider('Forecast Days',1,5, help='Slide to see data for more dates')

option=st.selectbox('Select data to view',('Tempeture','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')


#plotdata = {
#        "date":['2025-1-2','2025-1-3','2025-1-4'],
#        "temp":['30','32','29'],
#    }
#plotdata['temp'] = [days*int(i) for i in plotdata['temp']]

#st.line_chart(pd.DataFrame(plotdata),x='date',y='temp')


dates=['2025-1-2','2025-1-3','2025-1-4']
temps=[30,32,29]
temps=[days*int(i) for i in temps]

plot=px.line(x=dates,y=temps,labels={'x':'Date','y':'Tempeture (C)'})
st.plotly_chart(plot)

