import json
import pickle
import numpy as np

__model = None
__cols = None
__zip = None


def get_zip():
    return __zip

def load_file():
    global __zip
    global __cols
    global __model
    with open("./model/cols.json", "r") as f:
        __cols = json.load(f)['data_columns']
        __zip = __cols[8:]
    with open("./model/kc_housing_predict", 'rb') as f:
        __model = pickle.load(f)

def price_prediction(zip, bed, bath, sqft, floors, sqft_above, sqft_basement, yr_built, yr_reno):
    try:
        i = __cols.index(zip)
    except:
        i = -1

    a = np.zeros(len(__cols))
    a[0] = bed
    a[1] = bath
    a[2] = sqft
    a[3] = floors
    a[4] = sqft_above
    a[5] = sqft_basement
    a[6] = yr_built
    a[7] = yr_reno
    if i >= 0:
        a[i] = 1
    result = __model.predict([a])[0]
    if result > 300000:
        result = result - 100000
    return round(result, 2)



if __name__ == "__main__":
    load_file()
    print(price_prediction('98001', 3, 4, 2714, 2, 2714, 0, 2005, 2005))
    print(price_prediction('98199', 5, 8, 3520, 2, 3520, 0, 2001, 2001))
    print(price_prediction('98034', 3, 3, 1260, 1, 1260, 0, 1872, 1972))