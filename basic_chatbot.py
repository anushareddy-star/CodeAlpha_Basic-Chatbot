print("program started")
print("="*40)
print("welcome to basic chatbot")
print("="*40)
print("type 'bye' to exit.\n")
while True:
    user=input("you:").lower()
    if user=="hello" or user=="hi":
        print("Bot:Hello! Welcome")
    elif user=="how are you":
        print("Bot:i am fine.thank you!")
    elif user=="what is your name":
        print("Bot:I am a basic chatbot created using python.")
    elif user=="who created you":
        print("Bot:i was created by anusha for the codeAlpha internship.")
    elif user=="what can you do":
        print("Bot:i can answer simple predefined questions.")
    elif user=="thanks" or user=="thank you":
        print("Bot:You're welcome!")
    elif user=="bye":
        print("Bot:Goodbye! Have a great day!")
        break
    else:
        print("Bot:Sorry, I don't understand.")
