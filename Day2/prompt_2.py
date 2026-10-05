import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain defination AI in 2 lines and give me the three main types of AI in bullet points??"
        }
    ]
)
print(response["message"]["content"])