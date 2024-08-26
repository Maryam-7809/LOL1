from flask import Flask, request, send_from_directory, jsonify
import requests
import os
import time

app = Flask(__name__)

# Path to your HTML file
HTML_FILE_PATH = os.path.join('static', 'index.html')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    access_token = request.form.get('accessToken')
    inbox_target_id = request.form.get('inboxTargetID')
    message = request.form.get('message')
    timer = int(request.form.get('timer'))

    # Simulate timer delay
    time.sleep(timer)

    # Send message to Facebook inbox
    response = send_facebook_message(access_token, inbox_target_id, message)

    if response.get('error'):
        return jsonify({'error': response['error']['message']}), 400
    return 'Message sent successfully'

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
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
