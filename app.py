
from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load("california.joblib")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            features = [
                float(request.form["MedInc"]),
                float(request.form["HouseAge"]),
                float(request.form["AveRooms"]),
                float(request.form["AveBedrms"]),
                float(request.form["Population"]),
                float(request.form["AveOccup"]),
                float(request.form["Latitude"]),
                float(request.form["Longitude"])
            ]

            prediction = model.predict([features])[0]

        except ValueError:
            error = "Please enter valid numbers in all fields."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>California House Price Prediction</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #dbeafe, #e0e7ff);
                min-height: 100vh;
                padding: 35px 15px;
            }}

            .container {{
                max-width: 750px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 18px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            }}

            h1 {{
                text-align: center;
                color: #1d4ed8;
                margin-bottom: 10px;
            }}

            .subtitle {{
                text-align: center;
                color: #64748b;
                margin-bottom: 30px;
            }}

            .form-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
            }}

            label {{
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
                color: #334155;
            }}

            input {{
                width: 100%;
                padding: 12px;
                border: 1px solid #cbd5e1;
                border-radius: 8px;
                font-size: 15px;
            }}

            input:focus {{
                outline: 2px solid #93c5fd;
                border-color: #2563eb;
            }}

            button {{
                width: 100%;
                margin-top: 25px;
                padding: 14px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 9px;
                font-size: 17px;
                font-weight: bold;
                cursor: pointer;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            .result {{
                margin-top: 25px;
                padding: 18px;
                background: #dcfce7;
                color: #166534;
                border-radius: 10px;
                text-align: center;
                font-size: 20px;
                font-weight: bold;
            }}

            .error {{
                margin-top: 20px;
                color: #b91c1c;
                text-align: center;
            }}

            .footer {{
                text-align: center;
                color: #64748b;
                margin-top: 25px;
                font-size: 13px;
            }}

            @media (max-width: 550px) {{
                .form-grid {{
                    grid-template-columns: 1fr;
                }}

                .container {{
                    padding: 20px;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🏡 California House Price</h1>

            <p class="subtitle">
                Enter property details to estimate its value
            </p>

            <form method="POST">
                <div class="form-grid">

                    <div>
                        <label>Median Income (MedInc)</label>
                        <input type="number" step="any"
                               name="MedInc" required>
                    </div>

                    <div>
                        <label>House Age (HouseAge)</label>
                        <input type="number" step="any"
                               name="HouseAge" required>
                    </div>

                    <div>
                        <label>Average Rooms (AveRooms)</label>
                        <input type="number" step="any"
                               name="AveRooms" required>
                    </div>

                    <div>
                        <label>Average Bedrooms (AveBedrms)</label>
                        <input type="number" step="any"
                               name="AveBedrms" required>
                    </div>

                    <div>
                        <label>Population</label>
                        <input type="number" step="any"
                               name="Population" required>
                    </div>

                    <div>
                        <label>Average Occupancy (AveOccup)</label>
                        <input type="number" step="any"
                               name="AveOccup" required>
                    </div>

                    <div>
                        <label>Latitude</label>
                        <input type="number" step="any"
                               name="Latitude" required>
                    </div>

                    <div>
                        <label>Longitude</label>
                        <input type="number" step="any"
                               name="Longitude" required>
                    </div>

                </div>

                <button type="submit">
                    🔍 Predict House Price
                </button>
            </form>

            {f'<div class="result">Estimated Price: ${prediction * 100000:,.2f}</div>' if prediction is not None else ''}
            {f'<div class="error">{error}</div>' if error else ''}

            <div class="footer">
                California Housing ML Project | Built with Flask
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
