import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a therapist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Therapist", description= "Welcome to your digital therapist- a safe, confidential space to share your thoughts and feelings. Ask me for advice on anything!")

demo.launch(share=True)