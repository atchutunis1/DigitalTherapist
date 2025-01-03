import openai

openai.api_key = "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"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")