import streamlit as st
import pickle
st.title('Revenue Prediction')
deg=st.number_input('Input Temperature')
pickle.dump(model, open('model.pickle', "wb"))
model = pickle.load(open('model.pickle', "rb"))
if st.button('Predict'):
  st.write("Predicted Revenue")
  st.code(float(model.predict([[deg]])))
