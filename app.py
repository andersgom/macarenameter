import streamlit as st #first thing we do is import the streamlit library which we need to create the app
import pandas as pd #import pandas if you are going to use excel or csv tables
from final_script import *
import streamlit.components.v1 as components

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

    test = ''
    if len(input_feature) > 50:
        test = frame_maker(input_feature)

        if test['Hit'].values == 1:
            st.write("Your song is a potential summer hit, amigo.")
        else:
            st.write("Good luck next time.")


        minipvar = input_feature[:25]+'embed/'+input_feature[25:]
        st.write(minipvar[:-20])
        miniplayer = f"""
        <iframe style="border-radius:12px" src="{minipvar[:-20]}?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
        """

        components.html(miniplayer, height=600)


    else:
        st.write("testtttttt")

#testlink = "https://open.spotify.com/track/7JIjUx3GsL0upxmNJacmtz?si=d4660d663dcf4150"

#tl2 = testlink[:-20]

#tl2[:25]+'embed/'+tl2[25:]

    #minipvar = 


#testlink = "https://open.spotify.com/embed/track/5ildQOEKmJuWGl2vRkFdYc"


#https://open.spotify.com/track/7JIjUx3GsL0upxmNJacmtz?si=d4660d663dcf4150

#https://open.spotify.com/embed/track/5ildQOEKmJuWGl2vRkFdYc
#https://open.spotify.com/embed/track/7MJQ9Nfxzh8LPZ9e9u68Fq
    #<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/7JIjUx3GsL0upxmNJacmtz?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>