import streamlit as st
import pickle
st.title('Revenue Prediction')
a=st.number_input('Input Temperature')
if st.button('Predict'):
  st.write('Revenue Prediction')
