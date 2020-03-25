from flask import Flask, request, Response
from controllers import CSVController, GetDataController, FAQController
from config import config
from flask_cors import CORS
import requests, json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
csv_controller = CSVController.CSVController()
data = GetDataController.GetDataController()
faq_controller = FAQController.FAQController()


@app.route('/refreshData', methods=['GET'])
def get_info():
    try:
        URL = config.config()["URL"]
        r = requests.get(URL)
        data = csv_controller.main_method(r.text)
        return data
    except Exception as ex:
        print(ex)
        return {}

@app.route('/getData', methods=['GET'])
def get_data():
    try:
        return data.get_data()
    except Exception as ex:
        print(ex)
        return {}

@app.route('/getNews', methods=['GET'])
def get_news():
    try:
        URL = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?autoCorrect=false&pageNumber=1&pageSize=10&q=Coronavirus India&safeSearch=false"
        r = requests.get(url=URL, headers={
            "x-rapidapi-host":"contextualwebsearch-websearch-v1.p.rapidapi.com",
            "x-rapidapi-key":"62c1225008msh807b9d7226bb666p133e01jsn6e7ddaf124ce"
        })
        response = r.json()['value']

        for val in response:
            val['title'] = val['title'].replace('<b>','').replace('</b>','').replace('\n',' ')
        results = []
        for i in range(0, len(response), 2):
            temp_list = []
            response[i]["class"] ="card card-1"
            response[i+1]["class"] = "card card-2"
            temp_list.append(response[i])
            temp_list.append(response[i+1])
            results.append(temp_list)

        return Response(json.dumps(results),  mimetype='application/json')
    except Exception as ex:
        print(ex)
        return []


@app.route('/getFaq', methods=['GET'])
def get_faq():
    try:
        faq = faq_controller.get_faq()
        return Response(json.dumps(faq),  mimetype='application/json')
    except Exception as ex:
        print(ex)
        return []




if __name__ == '__main__':
    app.run(host="0.0.0.0")
