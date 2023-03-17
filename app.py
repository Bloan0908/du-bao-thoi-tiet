import streamlit as st
import pickle
st.title('Revenue Prediction')
deg=st.number_input('Input Temperature')
model = pickle.load(open('model.pickle', "rb"))
if st.button('Predict'):
  st.write("Revenue Prediction")
  st.code(float(model.predict([[deg]])))
