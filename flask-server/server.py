from searchnews import search, getData
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def index():
  return ""

@app.route("/searchitem", methods=['GET'])
def searchitem():
    searching = request.args.get('searching')
    docIdList = search(str(searching))
    return jsonify(docIdList)

@app.route("/data")
def data():
    dataList = getData()
    return jsonify(dataList)

if __name__ == "__main__":
    app.run(debug=True) 