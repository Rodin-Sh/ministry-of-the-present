import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Climate Chatbot")
user_message = st.text_input("Message", "")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert in climate science. You also have knowledge of climate fiction novels, like Ministry of the Future of the Fifth Season."},
        {
            "role": "user",
            "content": f"{user_message}"
        }
    ]
)

if user_message:
    st.write(completion.choices[0].message.content)