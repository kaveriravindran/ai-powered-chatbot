import gradio as gr
from chatbot import get_bot_response

def chat_with_kavs(message):
    return get_bot_response(message)

iface = gr.Interface(
    fn=chat_with_kavs,
    inputs="text",
    outputs="text",
    title="Chat with Kavs 💖",
    description="A simple AI chatbot built by Kaveri"
)

if __name__ == "__main__":
    iface.launch()



