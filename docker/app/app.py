from flask import Flask, jsonify
import os

from config import config

app = Flask(__name__)

# Load configuration
app.config.from_object(config)


@app.route("/")
def home():
    return jsonify(
        {"message": "Web App Deployed Successfully!", "debug": app.config["DEBUG"]}
    )


if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
