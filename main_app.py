import streamlit as st
from PIL import Image

st.title('まめのタイトル')
st.caption('まめのキャプションです')

# 画像
image = Image.open('./data/nyan.png')
st.image(image, width=300)