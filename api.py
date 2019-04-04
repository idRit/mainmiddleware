from databaseconnector.databaseModel import dbModel
from flask import Flask, url_for, request, json, Response, jsonify
from flask_cors import CORS, cross_origin

interactor = dbModel()
interactor.connected()

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def index():
    details_array = interactor.getAll()
    listOfDetails = []
    for detail in details_array:
        listOfDetails.append(detail)

    return json.dumps(listOfDetails)


@app.route("/api/insertDetails", methods = ['POST'])
def insertDetails():
    res = json.dumps(request.json)
    resDict = json.loads(res)

    ad = resDict.get("ad")
    creationTime = resDict.get("creationTime")
    desc = resDict.get("desc")
    location = resDict.get("location")
    s_id = resDict.get("s_id")
    response = resDict.get("response")
    address = resDict.get("address") 

    return jsonify({"value": "success"})

    
if __name__ == '__main__':
    app.run()