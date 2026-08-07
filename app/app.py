from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Fixed: Safe environment variable lookup
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "development_fallback")
    return "Hello, Azure DevOps World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
