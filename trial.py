#python -m streamlit run trial.py 
import streamlit as st
import os
from openai import OpenAI
import base64 

client = OpenAI(api_key=st.secrets["api_key"])

st.title("Math Reader 📷")

with st.form(key="sample_form"):
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button(label="Read")

if submit_button:
    if uploaded_file is not None:
        image_raw=uploaded_file.getvalue()
        #st.write(len(image_raw)) TEST
        image_base64=base64.b64encode(image_raw).decode("utf-8")
        #st.write(image_base64[:10]) 
        final_format="data:image/png;base64,"+image_base64
        #st.write(final_format[:30])
 
        response=client.responses.create(
            model="gpt-5.4",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": "Read the handwritten math in this image. Return only the equation in infix notation. Do not explain. Do not solve."},
                        {"type": "input_image", "image_url": final_format},
                    ]
                }
            ]
        )
        st.write("Answer:")
        st.code(response.output_text)
else: 
    pass


