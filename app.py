from flask import Flask, flash, redirect, render_template, request, jsonify

import pickle
import numpy as np

model = pickle.load(open("/workspaces/79278298/project/weight.pk","rb"))

app = Flask(__name__)

SPECIES = ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt']

@app.route("/")
def index():
    #name = request.args.get("name")
    return render_template("layout.html")

@app.route('/calculate',methods=['POST','GET'])
def predict():

    feature_vales = []

    lenght = request.form.get("Length")
    feature_vales.append(lenght)
    Height = request.form.get("Height")
    feature_vales.append(Height)
    Width = request.form.get("Width")
    feature_vales.append(Width)
    specie = request.form.get("specie")
    feature_vales.append(specie)


    feature_vales = np.array(feature_vales)

    feature_vales = feature_vales.astype('int32')


    final_parameters=[np.array(feature_vales)]
    #return jsonify(request.form.get("Length"))
    print(feature_vales)
    print(final_parameters)

    weight_cal=model.predict(final_parameters)
    #final_parameters.dtype()

    print(weight_cal[0][0])

    output='{0:.{1}f}'.format(weight_cal[0][0], 3)


    return render_template('layout.html',pred='The predicted wieght is {} grams'.format(output))


if __name__ == '__main__':
    app.run(debug=True)

