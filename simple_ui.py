import streamlit as st
from app.llm import get_llm
from langchain_core.messages import HumanMessage

st.title("Simple HuggingFace Chatbot")


llm = get_llm()

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input:
        response = llm.invoke([HumanMessage(content=user_input)])
        st.write("Bot:", response.content)



