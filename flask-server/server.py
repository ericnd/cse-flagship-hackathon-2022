from searchnews import search, getData
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)

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