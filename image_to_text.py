import streamlit as st
import google.generativeai as genai
from PIL import Image
# import matplotlib.pyplot as plt

model = genai.GenerativeModel("gemini-1.5-pro")

api_key='AIzaSyDYiuoZ93AI0DZJVflT3j7v2tMLHdyCBO0'
genai.configure(api_key=api_key)




st.title("my App")
st.text("sreamlit app")
st.write("hello ")
# st.text_input("name"," ")
st.button("click")

st.header("image analytics")
upload_file=st.file_uploader('upload as image',type=["png","jpg",'jpeg'])
if upload_file is not None:
    st.image(Image.open(upload_file))

promt=st.text_input('Enter text')
if  st.button("Get Response"):
    img=Image.open(upload_file)
    model=genai.GenerativeModel("gemini-1.5-pro")
    respone = model.generate_content([promt, img])
    st.markdown(respone.parts)