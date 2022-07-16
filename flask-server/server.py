from searchnews import search, getData
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

@app.route("/searchitem")
def searchitem():
    docIdList = search('trump')
    return jsonify(docIdList)

@app.route("/data")
def data():
    dataList = getData()
    return jsonify(dataList)

if __name__ == "__main__":
    app.run(debug=True) 