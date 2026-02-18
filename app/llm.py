import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

def get_llm():
    # Step 1: Base endpoint (LLM layer)
    hf_llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        task="conversational",
        temperature=0.7,
        max_new_tokens=500,
    )

    # Step 2: Wrap in Chat model
    chat_model = ChatHuggingFace(llm=hf_llm)

    return chat_model
