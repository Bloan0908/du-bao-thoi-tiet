import streamlit as st
import pickle
a=st.number_input('Input Temperature')
if st.button('Predict'):
  st.write('Revenue Prediction')
