import streamlit as st
from app.llm import get_chain

st.title("Simple HuggingFace Chatbot")

chain = get_chain()

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input:
        response = chain.invoke({"input": user_input})
        st.write("Bot:", response)
