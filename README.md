
print(" Simple AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye! ")
        break

    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How are you? ")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I'm a simple Python chatbot.")

    elif "python" in user:
        print("Bot: Python is a popular programming language.")

    elif "who created you" in user:
        print("Bot: I was created using Python!")

    elif "thank" in user:
        print("Bot: You're welcome! ")

    elif "help" in user:
        print("Bot: I can answer simple questions about myself and Python.")

    else:
        print("Bot: Sorry, I don't understand that yet.")

