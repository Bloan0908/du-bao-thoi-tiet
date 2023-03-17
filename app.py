import streamlit as st
import pickle
st.title('Revenue Prediction')
a=st.number_input('Input Temperature')
pickle.dump(model, open(filename, "wb"))
model = pickle.load(open(filename, "rb"))
if st.button('Predict'):
  st.write('Revenue Prediction',model.predict(a))
