import os
import tempfile

import streamlit as st
from py_mistral_helper.MistralHelper import MistralHelper

st.set_page_config(page_title="OCR Verse", layout="centered")

st.title("📄 OCR Verse")

# Model selection
target_model = st.selectbox("Select OCR model", ["Mistral"], index=0)

# User input selection
option = st.radio("Choose input type", ["Document URL", "PDF", "Image URL", "Image"], horizontal=True)

# Input fields
document_url = None
document = None
image_url = None
image = None
extracted_text = ""

if option == "Document URL":
    document_url = st.text_input("Enter document url")
elif option == "PDF":
    document = st.file_uploader("Upload a pdf", type=["pdf"])
elif option == "Image URL":
    image_url = st.text_input("Enter image url")
elif option == "Image":
    image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if st.button("Extract text"):
    if option == "Document URL" and document_url:
        mistral_helper = MistralHelper(api_key=st.secrets["MISTRAL_API_KEY"])
        extracted_text = ""
        _extracted_text = mistral_helper.extract_text_using_pdf_document_url(document_url)
        for text in _extracted_text.pages:
            extracted_text = extracted_text + "\n" + text.markdown
        st.expander("Extracted Text", expanded=True).markdown(extracted_text)
    elif document:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(document.read())
            temp_file_path = temp_file.name

        mistral_helper = MistralHelper(api_key=st.secrets["MISTRAL_API_KEY"])
        _extracted_text = mistral_helper.extract_text_using_pdf(temp_file_path)
        for text in _extracted_text.pages:
            extracted_text = extracted_text + "\n" + text.markdown
        st.expander("Extracted Text", expanded=True).markdown(extracted_text)

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
    elif image_url:
        mistral_helper = MistralHelper(api_key=st.secrets["MISTRAL_API_KEY"])
        _extracted_text = mistral_helper.extract_text_using_image_url(image_url)
        for text in _extracted_text.pages:
            extracted_text = extracted_text + "\n" + text.markdown
        st.expander("Extracted Text", expanded=True).markdown(extracted_text)
    elif image:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{image.type.split('/')[-1]}") as temp_file:
            temp_file.write(image.read())
            temp_file_path = temp_file.name

        mistral_helper = MistralHelper(api_key=st.secrets["MISTRAL_API_KEY"])
        _extracted_text = mistral_helper.extract_text_using_image_path(temp_file_path)
        for text in _extracted_text.pages:
            extracted_text = extracted_text + "\n" + text.markdown
        st.expander("Extracted Text", expanded=True).markdown(extracted_text)
    else:
        st.error("Please provide a valid input.")
        st.stop()
