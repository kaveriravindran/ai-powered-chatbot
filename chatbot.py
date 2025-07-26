import random

def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hey there! How can I help you today?"
    elif "who are you" in user_input:
        return "I'm Kavs, your friendly AI chatbot built by Kaveri 💖"
    elif "how are you" in user_input:
        return "I'm all code, but feeling great today! 😊"
    elif "bye" in user_input:
        return "Goodbye! Come back soon 💫"
    elif "love" in user_input:
        return "Aww that's sweet! 💕"
    elif "joke" in user_input:
        return random.choice([
            "Why don’t scientists trust atoms? Because they make up everything!",
            "What did the fish say when it hit the wall? Dam.",
            "Why was the math book sad? It had too many problems."
        ])
    else:
        return random.choice([
            "That's interesting. Tell me more!",
            "Can you elaborate on that?",
            "Hmm, let's think about that together.",
            "I'm listening... 😊"
        ])
