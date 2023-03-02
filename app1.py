

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pickle
import pandas as pd

pickle_in=open(r'Classifier.pkl','rb')
Classifier=pickle.load(pickle_in)



def welcome():
    return "Welcome All"



def churn_predict(voicemessages,intlmins,intlcalls,intlcharge,daymins,daycalls,daycharge,evemins,evecalls,evecharge,nightmins,nightcalls,nightcharge,customercalls,voiceplanyes,intlplanyes):
    prediction=Classifier.predict([[voicemessages,intlmins,intlcalls,intlcharge,daymins,daycalls,daycharge,evemins,evecalls,evecharge,nightmins,nightcalls,nightcharge,customercalls,voiceplanyes,intlplanyes]])
    print(prediction)
    return prediction

    
  
def main():
    st.title("Customer churn prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Churn prediction app </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    voicemessages = st.text_input("Voicemessages","Type Here")
    intlmins = st.text_input("intlmins","Type Here")
    intlcalls = st.text_input("intlcalls","Type Here")
    intlcharge = st.text_input("intlcharge","Type Here")
    daymins = st.text_input("daymins","Type Here")
    daycalls = st.text_input("daycalls","Type Here")
    daycharge = st.text_input("daycharge","Type Here")
    evemins = st.text_input("evemins","Type Here")
    evecalls = st.text_input("evecalls","Type Here")
    evecharge = st.text_input("evecharge","Type Here")
    nightmins = st.text_input("nightmins","Type Here")
    nightcalls = st.text_input("nightcalls","Type Here")
    nightcharge = st.text_input("nightcharge","Type Here")
    customercalls = st.text_input("customercalls","Type Here")
    voiceplanyes = st.text_input("voiceplanyes","Type Here")
    intlplanyes = st.text_input("intlplanyes","Type Here")
   
    result=""
    if st.button("Predict"):
        result=churn_predict(voicemessages,intlmins,intlcalls,intlcharge,daymins,daycalls,daycharge,evemins,evecalls,evecharge,nightmins,nightcalls,nightcharge,customercalls,voiceplanyes,intlplanyes)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()








