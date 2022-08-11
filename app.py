import streamlit as st #first thing we do is import the streamlit library which we need to create the app
import pandas as pd #import pandas if you are going to use excel or csv tables

#Firstly let us run our streamlit app so we see our changes happening live.

headers = st.container() #create a variable for your main header
model_training = st.container() 

with headers: #with is for us to get inside this section
    st.title('Macarenameter') #st.title allow us to create the main title 
    st.text("""Check if your song is a potential summer hit in Spain.""") #st.text allow us to write text

with model_training:
    st.header('')
    sel_col, disp_col = st.columns(2) #choose how many columns we want to work with
    #now we are creating a slider for user to choose what value he wants
    input_feature = sel_col.text_input('Write an opinion?',' ')

    st.write('You wrote: ', input_feature)

## ADD TWO FORMS