import ollama

response = ollama.chat(
    model="llama3.1",
    messages=[
        {
            "role": "user",
            "content": "Make some excuses as to why you can't go to class today",
        },
    ],
)
print(response["message"]["content"])
