import streamlit as st

st.set_page_config(
    page_title="JuniaGPT",
    page_icon=""
)

st.title("JuniaGPT")

if "messages" not in st.session_state: 
    st.session_state.messages = [] 

for message in st.session_state.messages: 
    with st.chat_message(message["role"]): 
        st.markdown(message["content"]) 

if prompt := st.chat_input("What is your question?", key="user_prompt"): 
    with st.chat_message("user"): 
        st.markdown(prompt) 

    with st.chat_message("assistant"): 
        st.markdown(prompt) 

    with st.chat_message("assistant"): 
        response = prompt 
        st.markdown(response) 

        st.session_state.messages.append( 
            {"role": "assistant", "content": response}, 
        ) 