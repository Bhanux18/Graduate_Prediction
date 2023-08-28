import streamlit as st

#--------------------------------------------------------------------------------------

def nlines(n):
    for _ in range(n):
        st.write("\n")
#--------------------------------------------------------------------------------------


st.image("Grad.jpeg")

st.title("Graduate Admission Prediction")

st.write(":violet[____Quick view about parameters involved in prediction of admission:____]")

st.write(":tomato[__University Rating:__]")
st.write("A unique identifier assigned to each applicant in the dataset.")

st.write(":red[__GRE Score:__]")
st.write("The Graduate Record Examination (GRE) score, which is a standardized test commonly required for admission to graduate schools.")

st.write(":blue[__TOEFL Score:__]")
st.write("The Test of English as a Foreign Language (TOEFL) score, which measures an applicant's English language proficiency. This score is important for non-native English speakers applying to English-speaking universities.")

st.write(":green[__University Rating:__]")
st.write("The rating or ranking of the university where the applicant wishes to gain admission. It is usually based on factors like faculty reputation, research output, and academic facilities.")

st.write(":purple[__SOP (Statement of Purpose):__]")
st.write("This is a critical component of the application process, where applicants provide a written statement outlining their academic and career goals, research interests, and reasons for applying to the specific program.")

st.write(":orange[__LOR (Letter of Recommendation):__]")
st.write("Letters written by individuals who can attest to the applicant's academic abilities, character, and potential for success in the graduate program. Typically, universities require two to three letters of recommendation.")

st.write(":brown[__CGPA (Cumulative Grade Point Average):__]")
st.write("The overall GPA of the applicant throughout their undergraduate studies. This is a measure of their academic performance and success during their bachelor's degree.")

st.write(":purple[__Chance of Admit:__]")
st.write("The estimated probability or chance that the applicant will be admitted to the graduate program. It is calculated based on various factors, such as test scores, GPA, statement of purpose, letters of recommendation, and research experience.")



nlines(5)

st.caption("__Created By:__  _Bhanuprakash_")