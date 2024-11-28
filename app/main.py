from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Función para obtener los datos del clima
def get_weather_data(city: str):
    API_KEY = '8766f9421597fca5b850bc1c1bd3e14b'
    idioma = 'es'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang={idioma}&appid={API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


@app.route("/cv")
def cv():
    return render_template("cv.html")





# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            data = get_weather_data(city)
            if data and data.get("cod") == 200:
                return render_template("mayra.html", data=data)
            else:
                return render_template("mayra.html", error="Ciudad no encontrada.")
    return render_template("mayra.html")

if __name__ == "__main__":
    app.run(debug=True)
