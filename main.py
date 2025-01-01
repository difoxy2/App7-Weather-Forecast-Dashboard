import streamlit as st
import pandas as pd
import plotly.express as px
import backend

# Add title, text input, slider, selectbox, subheadder
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

if place:
# Fetch tempeture/sky data
    date_array,temp_array,sky_array=backend.get_data(days,place)


# Plot the graph
    if option=='Tempeture':
        plot=px.line(x=date_array,y=temp_array,labels={'x':'Date','y':'Tempeture (C)'})
        st.plotly_chart(plot)
    elif option=='Sky':
        image_path_dict = {
            'Clear': 'images/clear.png',
            'Clouds': 'images/cloud.png',
            'Rain': 'images/rain.png',
            'Snow': 'images/snow.png',

        }
        image_path_array = [image_path_dict[i] for i in sky_array]
        st.image(image_path_array,date_array,115)