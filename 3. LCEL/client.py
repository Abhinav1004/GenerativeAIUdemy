import requests
import json
import streamlit as st


def get_groq_response(input_text):
    json_body={
          "input": {
            "language": "French",
            "text":input_text
          },
          "config": {},
          "kwargs": {}
        }
    print(json_body)
    json_body = json.dumps(json_body, indent=2)
    response=requests.post("http://127.0.0.1:8000/chain/invoke",json_body)    

    print(response.json())


    return response.json()

## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to french")

if input_text:
    st.write(get_groq_response(input_text))