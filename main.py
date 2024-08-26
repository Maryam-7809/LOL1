def send_facebook_message(access_token, recipient_id, message):
    GRAPH_API_URL = 'https://graph.facebook.com/v12.0/me/messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}',
    }
    payload = {
        'recipient': {'id': recipient_id},
        'message': {'text': message},
    }
    response = requests.post(GRAPH_API_URL, headers=headers, json=payload)
    print(response.json())  # Print the response to debug
    return response.json()
