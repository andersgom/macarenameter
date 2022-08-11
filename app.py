import streamlit as st
import pandas as pd
from final_script import *
import streamlit.components.v1 as components


headers = st.container()
model_training = st.container() 

with headers:
    st.title('Macarenameter',)
    st.markdown("""#### Check if your song qualifies as a potential summer hit in Spain 🏖️""", unsafe_allow_html=False)
    st.markdown("""We analized the summer hits in Spain of the last 30 years, so you can know if your song would be a potential summer hit in the confort fo your home.
     Chek the full analysis in our [GitHub Repo](https://github.com/andersgom/project5-week6).""", unsafe_allow_html=False)

with model_training:
    sel_col, disp_col = st.columns(2)
    input_feature = sel_col.text_input('Insert your song url','')

    test = ''
    if len(input_feature) > 50:
        st.markdown("""### Single song results:""", unsafe_allow_html=False)
        test = frame_maker(input_feature)

        if test['Hit'].values == 1:
            st.write("Your song qualifies for a potential summer hit, amigo.")
        else:
            st.write("Good luck next time.")


        minipvar = input_feature[:25]+'embed/'+input_feature[25:]
        miniplayer = f"""
        <iframe style="border-radius:12px" src="{minipvar[:-20]}?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
        """

        components.html(miniplayer, height=400)


    else:
        st.write("")

    input_feature = sel_col.text_input('Insert your playlist url','')

    test = ''
    if len(input_feature) > 50:
        st.markdown("""### Playlist results:""", unsafe_allow_html=False)
        test = playlist_dataframe(input_feature)

        if len(test[test['Hit']==1][['artist_name', 'track_name', 'release_date']]) > 0:
            st.write("From your playlist, these tracks qualifiy as potential hits.")
            st.write(test[test['Hit']==1][['artist_name', 'track_name', 'release_date']])
        else:
            st.write("None of your tracks qualify.")
        


        minipvar = input_feature[:25]+'embed/'+input_feature[25:]
        miniplayer = f"""
        <iframe style="border-radius:12px" src="{minipvar[:-20]}?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
        """

        components.html(miniplayer, height=400)

    else:
        st.write(" ")