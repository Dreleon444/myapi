from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def get_ip():
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Use free IP geolocation API
    geo_url = f"http://ip-api.com/json/{user_ip}"
    try:
        response = requests.get(geo_url)
        data = response.json()
        city = data.get("city", "Unknown City")
        country = data.get("country", "Unknown Country")
    except:
        city, country = "Unknown", "Unknown"

    # Modern, stylish HTML response
    return f"""
    <html>
        <head>
            <style>
                body {{
                    background-color: #121212;
                    color: #ff69b4;
                    font-family: 'Segoe UI', sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }}
                .box {{
                    background-color: #1e1e1e;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
                    display: inline-block;
                }}
                h1 {{
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="box">
                <h1>yooo what tha bizzness izzz buster boy!</h1>
                <p>Your IP Address: <strong>{user_ip}</strong></p>
                <p>Location: <strong>{city}, {country}</strong></p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)
