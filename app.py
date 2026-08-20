import streamlit as st
import easyocr
import numpy as np
from PIL import Image

st.title("OCR Text Extractor")
st.write("Upload an image and extract the text from it using EasyOCR.")

@st.cache_resource
def load_reader():
    return easyocr.Reader(['en'])

reader = load_reader()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    if st.button("Extract Text"):
        image_array = np.array(image)

        result = reader.readtext(image_array)

        text = ""

        for item in result:
            text += item[1] + "\n"

        st.subheader("Extracted Text")
        st.text_area("OCR Result", text, height=200)