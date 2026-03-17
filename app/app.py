from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "development")
    hostname = socket.gethostname()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h1>Project 4 - CI/CD with GitHub Actions< has been deployed/h1>
    <p><b>Version:</b> {version}</p>
    <p><b>Pod:</b> {hostname}</p>
    <p><b>Time:</b> {time}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
