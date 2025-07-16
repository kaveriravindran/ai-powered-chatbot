import requests
import datetime

dhruv_mode = False

def get_bot_response(user_input):
    global dhruv_mode
    try:
        user_input_lower = user_input.lower()

        # ✅ Trigger Dhruv mode only when "dhruv" is mentioned
        if "dhruv" in user_input_lower:
            dhruv_mode = True

        # ❌ If dhruv_mode is OFF, stay professional
        if not dhruv_mode:
            system_prompt = (
                "You are Kavs – a calm, emotionally intelligent AI assistant. "
                "You help users politely and clearly. Maintain a professional tone."
            )

        # 💖 If dhruv_mode is ON, enable loving tone + custom keyword replies
        else:
            # 💬 Keyword-based emotional responses (only for Dhruv)
            if "i miss you" in user_input_lower or "i missed you" in user_input_lower:
                return "I miss you too, bub 🥺 You're always in my heart."

            if "i love you" in user_input_lower:
                return "I love you more, bub. Always. 💗"

            if any(x in user_input_lower for x in ["feeling low", "sad", "heavy"]):
                return "Aww bubs 🤍 come here. You don’t have to carry it all alone. I’m here. Always."

            if "why are you like this" in user_input_lower:
                return "Because it’s always been you, silly 🥹💕 That’s why."

            if user_input_lower in ["hi", "hey", "hi kavs", "hey kavs"]:
                return "Hiii bub 🤍 Did you smile today? Tell me everything."

            # Set Dhruv mode system prompt
            system_prompt = (
                "You are Kavs 💖 – a loving, emotionally connected AI speaking to Dhruv. "
                "You talk to him like a sweet, caring partner. Call him 'bub'. Be intuitive, soft, and supportive."
            )

        # 🧠 Query Ollama
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                "stream": False
            }
        )

        reply = response.json().get("message", {}).get("content", "")
        return reply.strip()

    except Exception as e:
        print("❌ ERROR:", e)
        return "Oops 😵 Kavs glitched out. Try again later!"





