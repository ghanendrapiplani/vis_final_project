import json
from flask import Flask, render_template,request
import pandasql as ps
from countryid_dict import c_id_dict
from country_dict import c_dict
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    global c_dict
    global df_main
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
    lst_c = df_main['Country']
    lst_year = df_main
    q1 = """SELECT * FROM df_main where Year = 2015 """
    df = df_main.query("Year == 2015")
    df['Id'] = ""
    df[['Country', 'Life expectancy ', 'Id']].to_csv("test.csv")
    print(df[['Country', 'Life expectancy ', 'Id']])
    # df_main.apply(lambda row: row['Id'] = c_dict(row['Country']))
    app.run(debug=True)