from pickle import load
import streamlit as st
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
#--------------------------------------------------------------------------------------

def nlines(n):
    for _ in range(n):
        st.write("\n")
#--------------------------------------------------------------------------------------
# Loooking for file paths
abspath=os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(abspath, os.pardir)
dir = os.path.join(parent_dir, "resources")

scale_path=os.path.join(dir,"models","scaler.pkl")
logi_path=os.path.join(dir,"models","logistic.pkl")

#Title
st.title("Chance of :red[__Admit__] Prediction")
nlines(4)

# loading models
scale=load(open(scale_path,"rb"))
logi=load(open(logi_path,"rb"))

# user input :GREScore,TOEFLScore,UniversityRating,SOP,LOR,CGPA,Research
with st.form("user_input"):

    GRE=st.number_input("Enter GRE score :")
    TOEFL=st.number_input("Enter TOEFL score :")
    Rating=st.number_input("Enter University Rating score :")
    SOP=st.number_input("Enter SOP score :")
    LOR=st.number_input("Enter LOR score :")
    CGPA=st.number_input("Enter CGPA score :")
    #Research=st.radio("Enter [0=No  or 1=Yes] interested in research-oriented programs :",("No","Yes"))
    click=st.form_submit_button(label="Predict")

inputs=[[GRE,TOEFL,Rating,SOP,LOR,CGPA]]
input_scale=scale.transform(inputs)

pred=logi.predict(input_scale)

if click:
    if pred[0]==1:
        #st.subheader("Got Admission !🎉")
        st.balloons()
        st.success(" Got Admission !🎉",icon="✅")
        
    elif pred[0]==0:
        #st.subheader(" No Admission 😥!")
        st.success(" No Admission 😥!",icon="❌")



