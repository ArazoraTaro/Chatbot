import requests
user = input("Enter your username: ")
while True:
    parameter = input (user+": ")
    r = requests.get('https://some-random-api.ml/chatbot?message='+parameter)
    response_json  = r.json()
    bot_reply = response_json['response']
    print('Chatbot:',bot_reply)