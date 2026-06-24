from datetime import datetime

print("=" * 50)
print("        WELCOME TO AI CHATBOT")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")
print("=" * 50)

name = ""

while True:
    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Ask chatbot name
    elif user in ["your name", "what is your name", "who are you"]:
        print("Bot: I am a Rule-Based AI Chatbot.")

    # Ask bot condition
    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    # User name
    elif user.startswith("my name is"):
        name = user.replace("my name is", "").strip().title()
        print(f"Bot: Nice to meet you, {name}!")

    elif user == "what is my name":
        if name:
            print(f"Bot: Your name is {name}.")
        else:
            print("Bot: I don't know your name yet. Tell me using 'My name is ...'")

    # Time
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {current_time}")

    # Date
    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    # Help
    elif user == "help":
        print("\nAvailable Commands:")
        print("1. hello / hi / hey")
        print("2. how are you")
        print("3. your name")
        print("4. my name is <your name>")
        print("5. what is my name")
        print("6. time")
        print("7. date")
        print("8. help")
        print("9. bye")

    # Thank you
    elif user in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")