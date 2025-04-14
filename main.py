from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Mega Agent is live and ready!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    print(f"🔓 Server listening on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)