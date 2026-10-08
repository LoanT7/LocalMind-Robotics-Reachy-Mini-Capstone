import requests
import time

url = "http://localhost:8080/v1/chat/completions"

messages = [
    {
        "role": "system",
        "content": "You are Reachy Mini, a friendly robot assistant. Keep responses short and natural."
    }
]

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    data = {
        "model": "local-model",
        "messages": messages,
        "max_tokens": 50,
        "temperature": 0.2
    }

    start = time.perf_counter()

    response = requests.post(url, json=data)
    result = response.json()

    elapsed = time.perf_counter() - start

    answer = result["choices"][0]["message"]["content"]

    print("\nReachy:", answer)
    print(f"Latency: {elapsed:.2f} seconds")

    messages.append({
        "role": "assistant",
        "content": answer
    })