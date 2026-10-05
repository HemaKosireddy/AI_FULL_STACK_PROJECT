import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content": "You are teaching a 5 year old child, give me answer in 2-3 lines only."
        },
        {
            "role": "user",
            "content": "Explain ML??"
        }
    ]
)
print(response["message"]["content"])