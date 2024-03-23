import streamlit as st
import requests

headers = {"Authorization": "Bearer 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"}
API_URL_SEMANTICS = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

def generate_semantics(data):
    response = requests.post(API_URL_SEMANTICS, headers=headers, data=data)
    return response.json()

API_URL_CAPTION = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

def generate_captions(payload):
	response = requests.post(API_URL_CAPTION, headers=headers, json=payload)
	return response.json()

st.set_page_config(page_title="Image Caption Generator",layout="wide")

st.title("Image Caption Generator")

file=st.file_uploader("Put your file",label_visibility="hidden")

if file is not None:
    col1,col2,col3=st.columns(3)
    with col1:
        st.image(file)
    with col2:
        st.subheader("Semantics")
        text=list(generate_semantics(file)[0]['generated_text'])
        text[0]=text[0].upper()
        text="".join(text)
        st.write(text)
    with col3:
        st.subheader("Caption")
        question=f"Generate a instagram post title with this photo semantics '{text}' dont forgot to use hash tags"
        caption=generate_captions({
             "inputs":question
        })
        st.write(caption[0]['generated_text'][len(question)+1:])