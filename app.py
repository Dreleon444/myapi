from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def get_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    geo_url = f"http://ip-api.com/json/{user_ip}"
    try:
        response = requests.get(geo_url, timeout=5)
        data = response.json()
        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
    except Exception as e:
        print("Geolocation error:", e)
        city, country = "Unknown", "Unknown"

    return f"""
    <html>
    <head>
        <title>Digital Mirage</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background: #0f0f0f;
                color: #ff4da6;
                font-family: 'Courier New', monospace;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                flex-direction: column;
                text-align: center;
                background: linear-gradient(135deg, #0f0f0f 60%, #1a1a1a);
            }}

            h1 {{
                font-size: 3em;
                margin-bottom: 0.5em;
                text-shadow: 0 0 10px #ff4da6, 0 0 20px #ff4da6;
            }}

            p {{
                font-size: 1.2em;
                color: #ddd;
                margin: 0.5em 0;
            }}

            .neon-frame {{
                border: 2px solid #ff4da6;
                padding: 2em;
                border-radius: 12px;
                box-shadow: 0 0 15px #ff4da6, inset 0 0 10px #ff4da6;
                background-color: rgba(255, 255, 255, 0.02);
                backdrop-filter: blur(5px);
            }}

            .footer {{
                position: absolute;
                bottom: 15px;
                font-size: 0.8em;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="neon-frame">
            <h1>Ayo still good onnat $75❓</h1>
            <p><strong>IP Address:</strong> {user_ip}</p>
            <p><strong>Location:</strong> {city}, {country}</p>
        </div>
        <div class="footer">↯ Powered by Flask + ip-api.com | Styled in neon dreams</div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)
