import json
from flask import Flask, render_template,request
import pycountry
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/countryselected")
def kmeans():
    # global df_main
    arr = request.args.get('data')
    print(arr.split(','))
    return render_template("index.html", data="asdf",  title=json.dumps({"title": "PCA for KMeans Clustered Data"}))


if __name__ == "__main__":
    df_main = pd.read_csv('life_expectancy_data.csv', encoding='utf8')
    print(df_main)
    print(list(pycountry.countries)[0])
    cols = ['Id']
    cols = ['Country']
    df_ = pd.DataFrame(columns=cols)
    rows_list = []
    for c in list(pycountry.countries):
        rows_list.append([c.alpha_2, c.name])
    df = pd.DataFrame(rows_list)
    print(df)
    df_m = pd.merge(df_main, df_, on='Country', how='inner')
    print(df_m.columns)
    app.run(debug=True)
