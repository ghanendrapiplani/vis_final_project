import json
from flask import Flask, render_template,request
from countryid_dict import c_id_dict
from country_dict import c_dict
import pandas as pd


app = Flask(__name__)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response


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
    # global df_main
    # df = df_main.query("Year == 2015")
    # df_req = df[['Life expectancy ','iso3']]
    # df_req.columns = ['doc_count', 'key']
    # map_data['aggregations']['world_map']['buckets'] = df_req.to_dict('records')
    # print(map_data)
    return render_template("index.html")


@app.route("/mapplot")
def mapplot():
    global df_main
    yr = request.args.get('q')
    print("YEAR")
    print(yr)
    df = df_main.query("Year == "+yr)
    df_req = df[['Life expectancy ', 'iso3']]
    df_req.columns = ['doc_count', 'key']
    map_data['aggregations']['world_map']['buckets'] = df_req.to_dict('records')
    df_req.to_csv("test"+yr+".csv")
    return render_template("map.html", data=map_data,
                           worldJSON=json.load(open("static/world.json")))


@app.route("/parallelplot")
def parallelplot():
    global df_main
    countries = request.args.get('q')
    yr = request.args.get('yr')
    print("countries={} year={}".format(countries, yr))
    return render_template("parallel.html", data=countries)


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
    df_country_codes = pd.read_csv('country_lookup.csv')
    df_main = df_main.merge(df_country_codes, on='Country', how='inner')
    print("res")
    # print(df_main.to_csv("test.csv"))
    app.run(debug=True)