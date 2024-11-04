from flask import Flask,request,jsonify,Response
import base64
import json
import random
from collections import OrderedDict


app = Flask(__name__)


@app.route('/patient_details',methods=['POST'])
def patient_details():
    data = request.get_json()
    signalId = data.get('reqMessageObj', {}).get('signalId')
    mimeType = data.get('reqMessageObj', {}).get('mimeType')
    fileName = data.get('reqMessageObj', {}).get('fileName')
    fromId = data.get('reqMessageObj', {}).get('fromId')
    taskId = data.get('reqMessageObj', {}).get('taskId')
    parentId = data.get('reqMessageObj', {}).get('parentId')
    databaseName = data.get('reqMessageObj', {}).get('databaseName')
    
    botUserId = data.get('botUserId','')
    botDatabaseName = data.get('botDatabaseName','')
    reqMessageObj = data.get('reqMessageObj',None)
    url = 'https://google.com'

    
    # Decode the Base64 string
    #decoded_file_name = base64.b64decode(fileName).decode('utf-8')

     # Encode the fileName to Base64
    encoded_url = base64.b64encode(url.encode('utf-8')).decode('utf-8')

    try: 

        if  botUserId and botDatabaseName and reqMessageObj:
            response_data = OrderedDict([
                ("resultCode", '0'),
                ("resultText", "Success"),
                ("resMessageObj", OrderedDict([
                    ("taskId", taskId),
                    ("fromId", botUserId),
                    ("signalId", str(random.random())[2:20]),  # Random signalId
                    ("parentId", signalId),
                    ("mimeType", mimeType),
                    ("databaseName", databaseName),
                    ("fileName", encoded_url),
                ])),
                ("fromServer", 'localserver'),
                ("eoState", "stop"),
                ('reqMessageObj',reqMessageObj)#return  which is came
            ])


            json_response = json.dumps(response_data)
            return Response(json_response, mimetype='application/json')
        else:
            return jsonify( {
                "resultCode": '1',
                "resultText": "Failure",
                "fromServer": 'localserver',
                "eoState": "stop",
                })
    except Exception as e:
          
          return jsonify( {
                "resultCode": '1',
                "resultText": "Failure",
                "fromServer": 'localserver',
                "eoState": "stop",
                })

         

if __name__ == '__main__':
    app.run(debug=True)    

