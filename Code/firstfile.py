# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:28:00 2023

@author: K NIKHIL KUMAR REDDY
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/K NIKHIL KUMAR REDDY/OneDrive/Desktop/mlproj/trained_model.sav', 'rb'))



def predict(input_data):
    kr=np.asarray(input_data)
    input_data_reshaped = kr.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    


    
    if (prediction == 0):
        return 'The Person does not have a Thyroid Disease'
    else:
        return 'The Person has Thyroid Disease'
    
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/house-plants-realistic_1284-66731.jpg?size=626&ext=jpg&ga=GA1.2.1826830348.1678777000&semt=ais");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


        
        
def main():
    add_bg_from_url() 
    title = "<h1><font color='red'><center><b>Thyroid Disease Prediction Web App</b></center></font></h1>"
    
    st.markdown(title, unsafe_allow_html=True)
    age = "<h4 ><font color='black'><b>Age</b></font></h3>"
    
    st.markdown(age, unsafe_allow_html=True)
    #a=st.text_input("")
    a = st.slider('', 0, 100,key="20")
    Gender = "<h4 ><font color='black'><b>Gender</b></font></h3>"
    st.markdown(Gender, unsafe_allow_html=True)
   
    b = st.radio('',
    ('male','female'))
    
    q1 = "<h4 ><font color='black'><b>On Thyroxine</b></font></h3>"
    st.markdown(q1, unsafe_allow_html=True)
    c = st.selectbox(
    '',
    ('','Yes', 'No'),key="1")
    
    q2 = "<h4 ><font color='black'><b>On AntiThroxine Medication</b></font></h3>"
    st.markdown(q2, unsafe_allow_html=True)
    d = st.selectbox(
    '',
    ('','Yes', 'No'),key="2")
    
    q3 = "<h4 ><font color='black'><b>Is Sick</b></font></h3>"
    st.markdown(q3, unsafe_allow_html=True)
    e = st.selectbox(
    '',
    ('','Yes', 'No'),key="3")
    
    q4 = "<h4 ><font color='black'><b>Is Pregnant</b></font></h3>"
    st.markdown(q4, unsafe_allow_html=True)
    f= st.selectbox(
    '',
    ('','Yes', 'No'),key="4")
    
    q5 = "<h4 ><font color='black'><b>Thyroid Surgery</b></font></h3>"
    st.markdown(q5, unsafe_allow_html=True)
    g = st.selectbox(
    '',
    ('','Yes', 'No'),key="5")
    
    
    q6 = "<h4 ><font color='black'><b>i131 Treatment</b></font></h3>"
    st.markdown(q6, unsafe_allow_html=True)
    h = st.selectbox(
    '',
    ('','Yes', 'No'),key="6")
    
    
    q7 = "<h4 ><font color='black'><b>query hypothyroid</b></font></h3>"
    st.markdown(q7, unsafe_allow_html=True)
    i = st.selectbox(
    '',
    ('','Yes', 'No'),key="7")
    
    
    
    q8 = "<h4 ><font color='black'><b>query hyperthyroid</b></font></h3>"
    st.markdown(q8, unsafe_allow_html=True)
    j = st.selectbox(
    '',
    ('','Yes', 'No'),key="8")
    
    
    q9 = "<h4 ><font color='black'><b>Lithium</b></font></h3>"
    st.markdown(q9, unsafe_allow_html=True)
    k = st.selectbox(
    '',
    ('','Yes', 'No'),key="9")
    
    q10 = "<h4 ><font color='black'><b>Goitre</b></font></h3>"
    st.markdown(q10, unsafe_allow_html=True)
    l = st.selectbox(
    '',
    ('','Yes', 'No'),key="10")
    
    
    q11 = "<h4 ><font color='black'><b>Tumor</b></font></h3>"
    st.markdown(q11, unsafe_allow_html=True)
    m = st.selectbox(
    '',
    ('','Yes', 'No'),key="11")
    
    q28 = "<h4 ><font color='black'><b>Hypopituitary</b></font></h3>"
    st.markdown(q28, unsafe_allow_html=True)
    z = st.selectbox(
    '',
    ('','Yes', 'No'),key="12")
    
    q12 = "<h4 ><font color='black'><b>Psych</b></font></h3>"
    st.markdown(q12, unsafe_allow_html=True)
    n = st.selectbox(
    '',
    ('','Yes', 'No'),key="13")
    
    
    q13 = "<h4 ><font color='black'><b>TSH Value</b></font></h3>"
    st.markdown(q13, unsafe_allow_html=True)
    
    o = st.slider('', 0.0, 40.0,key="14")
    
    q14 = "<h4 ><font color='black'><b>T3 Value</b></font></h3>"
    st.markdown(q14, unsafe_allow_html=True)
    
    p = st.slider('', 0.0, 10.0,key="15")
    
    q15 = "<h4 ><font color='black'><b>TT4 Vlaue</b></font></h3>"
    st.markdown(q15, unsafe_allow_html=True)
    
    q = st.slider('', 0, 300,key="16")
    
    q16 = "<h4 ><font color='black'><b>T4U Value</b></font></h3>"
    st.markdown(q16, unsafe_allow_html=True)
    
    r = st.slider('', 0.0, 10.0,key="17")
    
    q17 = "<h4 ><font color='black'><b>FTI Value</b></font></h3>"
    st.markdown(q17, unsafe_allow_html=True)
    
    s = st.slider('', 0, 300,key="18")
    
    q18 = "<h4 ><font color='black'><b>Referral</b></font></h3>"
    st.markdown(q18, unsafe_allow_html=True)
    t = st.selectbox(
    '',
    ('','other', 'SVI','SVHC','STMW','SVHD'),key="19")
    
    t1=0
    if t=="other":
        t1=0
    elif t=="SVI":
        t1=1
    elif t=="SVHC":
        t1=2
    elif t=="STMW":
        t1=3
    else:
        t1=4
    
    a1=a
    
    b1=0
    
    if b=="male":
        b1=1
    else:
        b1=0
     
    c1=0
    if c=="No":
        c1=0
    else:
        c1=1
        
    d1=0
    if d=="No":
        d1=0
    else:
        d1=1
        
    e1=0
    if e=="No":
        e1=0
    else:
        e1=1
        
    f1=0
    if f=="No":
        f1=0
    else:
        f1=1
        
    g1=0
    if g=="No":
        g1=0
    else:
        g1=1
        
    h1=0
    if h=="No":
        h1=0
    else:
        h1=1
    
    i1=0
    if i=="No":
        i1=0
    else:
        i1=1
    
    j1=0
    if j=="No":
        j1=0
    else:
        j1=1
    
    k1=0
    if k=="No":
        k1=0
    else:
        k1=1
    
    l1=0
    if l=="No":
        l1=0
    else:
        l1=1
    
    m1=0
    if m=="No":
        m1=0
    else:
        m1=1
    
    z1=0
    if z=="No":
        z1=0
    else:
        z1=1
    
    n1=0
    if n=="No":
        n1=0
    else:
        n1=1
        
    
    
    
    
    
    
    

    
    
    diagnosis = ''
    
    if st.button("Thyroid test result"):
        diagnosis= predict([a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1,z1,n1,o,p,q,r,s,t1])
     
    st.success(diagnosis)
       
if __name__ == '__main__':
    main()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    