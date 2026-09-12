from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Hello from your Jenkins CI/CD Flask App1!"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    # Important for Docker: listen on all interfaces
    app.run(host="0.0.0.0", port=5000, debug=False)
