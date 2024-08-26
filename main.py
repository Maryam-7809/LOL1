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

@app.route('/send-sticker', methods=['POST'])
def send_sticker():
    app_state = request.form.get('appState')
    inbox_target_id = request.form.get('inboxTargetID')
    message = request.form.get('message')
    timer = int(request.form.get('timer'))

    # Simulate timer delay
    time.sleep(timer)

    # Send message to Facebook inbox
    response = send_message(inbox_target_id, message)

    # Check for errors in the response
    if response.get('error'):
        return jsonify({'error': response['error']['message']}), 400
    
    return 'Sticker sent successfully'

def send_message(recipient_id, message):
    ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'  # Replace with your actual token
    GRAPH_API_URL = 'https://graph.facebook.com/v12.0/me/messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }
    payload = {
        'recipient': {'id': recipient_id},
        'message': {'text': message},
    }
    response = requests.post(GRAPH_API_URL, headers=headers, json=payload)
    
    # Print response for debugging
    print(response.json())
    
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
