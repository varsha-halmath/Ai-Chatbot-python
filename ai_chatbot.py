import datetime

print("🤖 VarshaBot: Hello! Type 'bye' to exit")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("VarshaBot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("VarshaBot: My name is VarshaBot 😊")

    elif "how are you" in user_input:
        print("VarshaBot: I am doing great! What about you?")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("VarshaBot: Current time is", current_time)

    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("VarshaBot: Today's date is", current_date)

    elif "help" in user_input:
        print("VarshaBot: I can tell time, date and chat with you.")

    elif user_input == "bye":
        print("VarshaBot: Goodbye Varsha 🌸 Have a nice day!")
        break

    else:
        print("VarshaBot: Sorry, I don't understand that.")
