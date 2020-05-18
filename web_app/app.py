import json
from flask import Flask, render_template,request
from countryid_dict import c_id_dict
from country_dict import c_dict
import pandas as pd

app = Flask(__name__)

map_data = {
   "took": 492,
   "timed_out": "false",
   "_shards": {
      "total": 5,
      "successful": 3,
      "failed": 0
   },
   "hits": {
      "total": 30111166,
      "max_score": 0,
      "hits": []
   },
   "aggregations": {
      "world_map": {
         "doc_count_error_upper_bound": 0,
         "sum_other_doc_count": 0
      }
   }
}

@app.route("/")
def index():
    global c_dict
    global df_main
    df = df_main.query("Year == 2015")
    df_req = df[['Life expectancy ','iso3']]
    df_req.columns = ['doc_count', 'key']
    map_data['aggregations']['world_map']['buckets'] = df_req.to_dict('records')
    print(map_data)
    return render_template("index.html", data=map_data,
                           worldJSON=json.load(open("static/world.json")))
    # return render_template("index.html", data=,)


@app.route("/countryselected")
def countryselected():
    # global df_main
    arr = request.args.get('data')
    print(arr.split(','))
    return render_template("index.html", data="",  title=json.dumps({"title": "PCA for KMeans Clustered Data"}))


def prepare_for_client(df):
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return data


def fx(df_country_codes, country):
    val = ""
    try:
        val = df_country_codes.query("Combined_Key == '{}'".format(country))['iso3'][0]
    except Exception as e:
        print(e)
    return val


if __name__ == "__main__":
    df_main = pd.read_csv('Life_Expectancy_Data.csv', encoding='utf8')
    print(df_main)
    df_country_codes = pd.read_csv('country_lookup.csv')
    print(df_country_codes.head())
    df_main = df_main.merge(df_country_codes, on = 'Country', how='inner')
    # print(df_main.to_csv("test.csv"))
    app.run(debug=True)