import streamlit as stl
from sklearn.externals import joblib 
import pandas as pd
import webbrowser


model=joblib.load('XGBoostClassifier.pickle.dat') 
stl.title(' PHISHING WEBSITE DETECTION ')

stl.write("Paste URL that is needed to be tested")
sentence = st.text_input('Input your sentence here:')
if sentence:
    stl.write(model.predict([['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth',
       'Redirection', 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record',
       'Web_Traffic', 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over',
       'Right_Click', 'Web_Forwards', 'Label']])

stl.write("Prediction")

stl.write("    ")

