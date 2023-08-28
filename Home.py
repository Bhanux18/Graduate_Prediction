import streamlit as st

from matplotlib import image
import pandas as pd
import plotly.express as px
import os



st.title("First Data App !!")

st.subheader("It's my :blue[portfolio!] web app ")

btn1 = st.button("Profile !")


if btn1 == True:
    
    st.subheader("Hello Amigos !!")
    st.write("My name is :blue[__name__],Data Science intern at Innomatics Research Labs.")
    st.write("\n")
    st.write("My very aim is to work .")
    st.write("\n")
    st.write("\n")
    st.write("\n")

   
    st.write("Feel free to connect with me on below links")
 
    st.markdown("[Linkedin](https://www.linkedin.com/in/bhanux18/)")
    st.markdown("[Github](https://github.com/Bhanux18)")
    st.markdown("[mail-to](mailto:coursestuff25@gmail.com)")
    









    st.balloons()