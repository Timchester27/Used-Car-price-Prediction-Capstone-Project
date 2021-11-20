from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/get_brand_names')
def get_brand_names():
    response = jsonify({
        "brand" : util.get_brand_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


@app.route('/get_model_names')
def get_model_names():
    response = jsonify({
        "model" : util.get_model_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


@app.route('/get_fuel_type_names')
def get_fuel_type_names():
    response = jsonify({
        "fuel_type" : util.get_fuel_type_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


@app.route('/get_transmission_type_names')
def get_transmission_type_names():
    response = jsonify({
        "transmission_type" : util.get_transmission_type_names()
    })
    response.headers.add("Access-Control-Allow-Origin", '*')

    return response


@app.route('/predict_car_price', methods=['POST'])
def predict_car_price():
    mpg = float(request.form['mpg'])
    engineSize = float(request.form['engineSize'])
    brand = request.form['brand']
    model = request.form['model']
    fuel_type = request.form['fuel_type']
    transmission_type = request.form['transmission_type']
    year = int(request.form['year'])
    mileage = int(request.form['mileage'])
    tax = int(request.form['tax'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(brand, model, year, mileage, tax, mpg, engineSize, fuel_type, transmission_type)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Flask Server")
    util.load_saved_artifacts()
    app.run()