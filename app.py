
from chat import Chat 
import gradio as gr
import time
pairs = (
    (
        r"salom",
        (
            "Assalomu aleykum",
            "Salom salom",
        ),
    ),
    (
        r"ha",
        (
            "Ha yaxshi unda",
            "Tushunarli"
        )
    ),
    (
        r"M[ea]nga (.*) ker[eak]",
        (
            "%1? Nimaga kerak?",
            "Menimcha bu %1 unchalik zarurmas",
            "Aniq %1 kerakmi?"
        ),

    ),

    (
        r"(.*) isming (.*)",
        (
            "Salom, mening ismim Eliza!!!",
        )
    ),

    (
        r"[xayrbye]",
        (
            "Rahmat, salomat bo'ling",
            "Ko'rishguncha",
            "Xayr, xayr"
        ),
    ),
    (
        r"(.*)",
        (
            "Aniqroq yozingchi !",
            "Savolni sal o'zgartirib bering",
            "To'liqroq ayting",
            "Nimaga bu savolni so'rayapsiz",
            "O'ylab ko'rish kerak",
            "Qiziq"
        ),
    ),

    (
        r"(.*)\?",
        (
            "Nega bunaqa savol berdingiz?",
            "Siz bu savolning javobini bilasizmi?",
            "%1 savolingizdan tashqari boshqa savolingiz bormi?"
        )
    )
)

chat = Chat(pairs)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = chat.respond(message)
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch(share=True)