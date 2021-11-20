import json
import pickle
import numpy as np

__model = None
__brand = None
__transmission_type = None
__fuel_type = None
__data_columns = None
__models = None


def get_estimated_price(brand, model, year, mileage, tax, mpg, engineSize, fuel_type, transmission_type):
    try:
        model_index = __data_columns.index(model.lower())
        brand_index = __data_columns.index(brand.lower())
        fuel_type_index = __data_columns.index(fuel_type.lower())
        transmission_type_index = __data_columns.index(transmission_type.lower())
    except:
        model_index = -1
        brand_index = -1
        fuel_type_index = -1
        transmission_type_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = year
    x[1] = mileage
    x[2] = tax
    x[3] = mpg
    x[4] = engineSize
    if brand_index >= 0:
        x[brand_index] = 1
    if model_index >= 0:
        x[model_index] = 1
    if fuel_type_index >= 0:
        x[fuel_type_index] = 1
    if transmission_type_index >= 0:
        x[transmission_type_index] = 1

    return np.round(float(__models.predict([x])), 2)


def get_brand_names():
    return __brand


def get_model_names():
    return __model


def get_fuel_type_names():
    return __fuel_type


def get_transmission_type_names():
    return __transmission_type


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __brand
    global __model
    global __fuel_type
    global __transmission_type
    global __models

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __brand = __data_columns[12:17]
        __model = __data_columns[17:]
        __fuel_type = __data_columns[5:9]
        __transmission_type = __data_columns[9:12]

    with open("./artifacts/car_prices_model.pickle", 'rb') as f:
        __models = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_brand_names())
    print(get_model_names())
    print(get_fuel_type_names())
    print(get_transmission_type_names())
    print(get_estimated_price("Toyota", "GT86", 2017, 36284,145, 36.2, 2.0, "Petrol", "Manual"))
