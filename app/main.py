from app.llm import get_chain

def start_chat():
    chain = get_chain()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            break

        response = chain.invoke({"input": user_input})
        print("Bot:", response)

