import pyjokes
from datetime import datetime

print("\n______Simple CLI Chatbot______")
print("\nSay hello to your chatbot")
print("\nType 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if "bye" in user_input:
        print("Bot: Goodbye! Have a nice day ")
        break

    # Greeting
    elif "hi" in user_input or "hello" in user_input:
        print("Bot: Hello! How can I help you today? ")

    # Ask name
    elif "your name" in user_input:
        print("Bot: I am a simple rule-based Python chatbot.")

    # Ask about Python
    elif "python" in user_input:
        print("Bot: Python is an easy and powerful programming language.")

    # Ask time
    elif "time" in user_input:
        now = datetime.now()
        print("Bot: Current time is", now.strftime("%H:%M:%S"))

    # Ask day
    elif "day" in user_input:
        today = datetime.now()
        print("Bot: Today is", today.strftime("%A"))

    # Ask for joke
    elif "joke" in user_input:
        joke = pyjokes.get_joke()
        print("Bot:", joke)

    # Default response
    else:
        print("Bot: Sorry, I didn't understand that. Please try again.")