from flask import Flask, request, jsonify
from api.routes import init_routes
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
init_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))