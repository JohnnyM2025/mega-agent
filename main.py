from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Mega Agent is live and ready!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)