import streamlit as st
st.title('APPLICATION OF RRB')
st.text_input('NAME OF APPLICANT')
st.text_input('FATHER NAME')
st.text_input('MOTHER NAME')
st.date_input('DATE OF BIRTH')
st.write('GENDER')
selected_option = st.selectbox('Select one option:',
    ['MALE', 'FEMALE', 'OTHER'], key='optioin')
st.text_input('ENTER 10TH ROLL NO.')
s=st.number_input('ENTER PERCENTAGE')
if s>=80:
    st.write('You appear this exam')
else:
    st.write('You not appear this exam')
st.text_input('ADDRESS')
st.write('CATEGORY')
selected_options = st.selectbox("Select one options:",
    ['GENREAL', 'OBC', 'SC'], key='option')
st.button('SUBMIT')
st.balloons()