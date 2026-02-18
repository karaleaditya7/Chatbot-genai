
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_chain():

    # Base LLM
    hf_llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        task="conversational",
        temperature=0.7,
        max_new_tokens=256,
    )

    chat_model = ChatHuggingFace(llm=hf_llm)

    # Prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful and professional AI assistant."),
        ("human", "{input}")
    ])

    # Output parser
    parser = StrOutputParser()

    # Create chain
    chain = prompt | chat_model | parser

    return chain
