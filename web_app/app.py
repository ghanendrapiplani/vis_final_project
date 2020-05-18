import json
from flask import Flask, render_template,request
from countryid_dict import c_id_dict
from country_dict import c_dict
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    global c_dict
    global df_main
    q1 = """SELECT * FROM df_main where Year = 2015 """
    df = df_main.query("Year == 2015")
    df['Id'] = ""
    df['Id'] = df.apply(lambda x: c_dict[x['Country']] if x['Country'] in c_dict.keys() else "", axis=1)
    print(df[['Country', 'Life expectancy ', 'Id']])
    df[['Country', 'Life expectancy ', 'Id']].to_csv("test.csv")
    return render_template("index.html")


@app.route("/countryselected")
def kmeans():
    # global df_main
    arr = request.args.get('data')
    print(arr.split(','))
    return render_template("index.html", data="asdf",  title=json.dumps({"title": "PCA for KMeans Clustered Data"}))


def fx(row):
    print("row")
    print(row)
    print(row['Country'])
    print(c_dict[row['Country']])
    row['Id'] = c_dict[row['Country']]


if __name__ == "__main__":
    df_main = pd.read_csv('Life_Expectancy_Data.csv', encoding='utf8')
    print("df mainn")
    print(df_main.head())
    print(c_id_dict)

    app.run(debug=True)