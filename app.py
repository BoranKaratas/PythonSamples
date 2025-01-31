import os
from app import create_app

app = create_app()

@app.route("/", methods=['POST'])
def home():
    return "Merhaba. Server ayakta!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)