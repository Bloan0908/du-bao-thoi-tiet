import streamlit as st
import pickle
st.title('Revenue Prediction')
a=st.number_input('Input Temperature')
model = pickle.load(open(filename, "model.pickle"))
if st.button('Predict'):
  st.write('Revenue Prediction',model.predict(a))
