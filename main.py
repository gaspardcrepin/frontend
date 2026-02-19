import httpx
import streamlit as st

from rest.service import Chat, client

st.set_page_config(page_title="JuniaGPT", page_icon="")

st.title("JuniaGPT")

temperature_mapping = {"Accurate": 0, "Balanced": 0.7, "Creative": 1}
# Let the user chose the temperature category he wants
temperature_choice = st.sidebar.radio(
    label="Model Behavior",
    options=temperature_mapping.keys(),
    index=1,
)
# get the float value associated
temperature = temperature_mapping.get(temperature_choice)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?", key="user_prompt"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = Chat(
            model="llama3.2",
            temperature=temperature,
            messages=st.session_state.messages,
        )
        response = client.post(chat=chat)
        if response.status_code == httpx.codes.OK:
            message = response.json()["answer"]
            st.markdown(message)
            st.session_state.messages.append(
                {"role": "assistant", "content": message},
            )
        else:
            st.write("It seems that something broke down 😅")
            st.write(response.status_code)
