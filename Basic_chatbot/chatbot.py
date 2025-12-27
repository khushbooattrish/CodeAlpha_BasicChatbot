# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    """
    This function returns a response based on user input
    """
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! 😊"
    elif user_input == "how are you":
        return "I'm fine, thanks! How can I help you?"
    elif user_input == "bye":
        return "Goodbye! Have a nice day 👋"
    else:
        return "Sorry, I don't understand that."

# Main program
print("🤖 Chatbot is running!")
print("Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Bot:", response)

    if user_message.lower() == "bye":
        break

print("\n✅ Chatbot stopped.")

