import json
import pickle
import numpy as np
from pathlib import Path

__model = None
__cols = None
__zip = None

_BASE = Path(__file__).resolve().parent
_MODEL_DIR = _BASE / "model"
_COLS_PATH = _MODEL_DIR / "cols.json"
_MODEL_PATH = _MODEL_DIR / "kc_housing_predict"

def _ensure_loaded():
    global __zip, __cols, __model
    if __cols is not None and __model is not None:
        return
    with _COLS_PATH.open("r") as f:
        __cols = json.load(f)["data_columns"]
        __zip = __cols[8:]
    with _MODEL_PATH.open("rb") as f:
        __model = pickle.load(f)

def get_zip():
    _ensure_loaded()
    return __zip

def price_prediction(zip_code, bed, bath, sqft, floors, sqft_above, sqft_basement, yr_built, yr_reno):
    _ensure_loaded()

    try:
        i = __cols.index(str(zip_code))
    except ValueError:
        i = -1

    a = np.zeros(len(__cols), dtype=float)
    a[0] = bed
    a[1] = bath
    a[2] = sqft
    a[3] = floors
    a[4] = sqft_above
    a[5] = sqft_basement
    a[6] = yr_built
    a[7] = yr_reno
    if i >= 0:
        a[i] = 1.0

    result = float(__model.predict([a])[0])
    if result > 300000:
        result -= 100000
    return round(result, 2)

if __name__ == "__main__":
    print(price_prediction('98001', 3, 4, 2714, 2, 2714, 0, 2005, 2005))
    print(price_prediction('98199', 5, 8, 3520, 2, 3520, 0, 2001, 2001))
    print(price_prediction('98034', 3, 3, 1260, 1, 1260, 0, 1872, 1972))
