from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application" : "Co-de-ploy",
        "message" : "Devops pipeline is alive",
        "version" : os.getenv("APP_VERSION","development")  
    }

@app.route("/health")
def health():
    return {
        "status" : "healthy"
    }

@app.route("/version")
def version():
    return {
        "version" : os.getenv("APP_VERSION","development")  
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)