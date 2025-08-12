from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"Received login - Username: {username}, Password: {password}")
    return f"Hello, {username}! Your login was received."

if __name__ == '__main__':
    app.run(debug=True)
