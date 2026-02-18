from app.llm import get_llm
from langchain_core.messages import HumanMessage

def start_chat():
    llm = get_llm()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            break

        response = llm.invoke([HumanMessage(content=user_input)])
        print("Bot:", response.content)
