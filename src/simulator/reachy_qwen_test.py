import requests
import time
import pyttsx3

from reachy_mini import ReachyMini


url = "http://localhost:8080/v1/chat/completions"

messages = [
    {
        "role": "system",
        "content": (
            "You are Reachy Mini, a friendly robot assistant. "
            "Keep your responses short, natural, and conversational."
        )
    }
]


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


with ReachyMini() as mini:

    print("Connected to Reachy Mini simulation!")
    print("Qwen conversation is ready.")
    print("Type 'exit' or 'quit' to stop.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Conversation ended.")
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        data = {
            "model": "local-model",
            "messages": messages,
            "max_tokens": 40,
            "temperature": 0.2
        }

        start_time = time.perf_counter()

        response = requests.post(
            url,
            json=data,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        elapsed = time.perf_counter() - start_time

        answer = result["choices"][0]["message"]["content"]

        print("\nReachy:", answer)
        print(f"LLM latency: {elapsed:.2f} seconds")

        # Move antennas
        mini.goto_target(
            antennas=[0.4, -0.4],
            duration=0.4
        )

        # Speak response
        speak(answer)

        # Return antennas to normal
        mini.goto_target(
            antennas=[0, 0],
            duration=0.4
        )

        messages.append({
            "role": "assistant",
            "content": answer
        })