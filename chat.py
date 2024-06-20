import requests

url = "https://chat-gpt26.p.rapidapi.com/"

def get_response():
    user_input = input("You: ")
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "b2772b16a6msh0606a2b82ac6130p11b00bjsn59031be9005a",
        "X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Bot:", response.json()["choices"][0]["message"]["content"])

while True:
    get_response()