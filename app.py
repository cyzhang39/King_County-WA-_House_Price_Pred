from flask import Flask, request, jsonify, render_template
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/zipcode', methods=['GET'])
def zipcode():
    response = jsonify({
        'zipcode': utils.get_zip()
    })
    return response

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    zipcode = request.form['zipcode']
    bed = int(request.form['bedrooms'])
    bath = int(request.form['bathrooms'])
    sqft = float(request.form['sqft_living'])
    floors = int(request.form['floors'])
    above = int(request.form['sqft_above'])
    base = int(request.form['sqft_basement'])
    built = int(request.form['yr_built'])
    reno = int(request.form['yr_renovated'])

    response = jsonify({
        'price': utils.price_prediction(zipcode, bed, bath, sqft, floors, above, base, built, reno)
    })

    return response


if __name__ == "__main__":
    utils.load_file()
    app.run()