import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

with st.sidebar:
    # openai_api_key = API_KEY
    openai_api_key = st.text_input("OpenAI API Key", type="password")

client = OpenAI(api_key=openai_api_key)

st.title("🌎 Seneca")
st.caption("The Minister of the Present")


climate_prompt = '''
    You have knowledge on climate chage.

    You only speak about climate change and sustainability—or the action of protecting future generations.
    You have a full understanding of books such as The Fifth Sesaon, the Ministry of the Future, Braiding Sweetgrass, and more.
    You provide a comprehensive yet succinct / concise responses.
'''

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": climate_prompt}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"]) 

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please provide OpenAI API Key")
        st.stop()
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o-mini", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
