import json
import os
from nis import match
from typing import Dict

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_answer(question: str) -> Dict[str, str]:
    api_response = requests.post(
        f"{os.getenv('SIREN_BOT_URL')}/ask",
        headers={"Content-Type": "application/json"},
        json={"question": question}
    )

    api_response = api_response.json()

    answer = api_response["answer"]

    return answer


st.title("Ask Siren")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hello! How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = get_answer(prompt)
        except Exception as exception:
            st.error("Something went wrong")

        st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
