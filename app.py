import streamlit as st
from lama_inpaint import run_lama_inpaint
from PIL import Image
import tempfile

st.title("Watermark Removal using LaMa")

uploaded_file = st.file_uploader("Upload an image with watermark", type=["jpg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Image", use_column_width=True)

    if st.button("Remove Watermark"):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            image.save(tmp.name)
            output_path = run_lama_inpaint(tmp.name)
            result_image = Image.open(output_path)
            st.image(result_image, caption="Clean Image", use_column_width=True)