import json
from os import abort
from flask import Flask, jsonify, request, make_response, Response
from flask_restx import Api, Resource
from flask_cors import CORS
from responses import ApiException, OK, FALSE
import transfer
import metadata as _meta

app = Flask(__name__)
CORS(app)
api = Api(app)

# error
@app.errorhandler(404)
def page_not_found(e):
    return {'message':'page not found'}, 404

@app.errorhandler(ApiException)
def handle_bad_request(e):
    return_message = {'error_message':e.error_message, 'status': e.code}
    if e.result:
        return_message['result'] = e.result
    return jsonify(return_message), e.code

@app.after_request
def final_return(response):
    # custom error
    if 'error_message' in response.json:
        return Response(
                json.dumps({
                    'request url' : request.path,
                    'status code':response.json['status'],
                    'issuccess': FALSE,
                    'error message':response.json['error_message']
                    }),
                status = response.json['status'],
                mimetype = 'application/json'
        )
        
    # ststus error
    elif int(response.status.split(' ')[0]) != 200:
        return Response(
                json.dumps({
                    'request url' : request.path,
                    'status code':int(response.status.split(' ')[0]),
                    'issuccess': FALSE,
                    'error message':response.json['message']
                    
                    }),
                    status=int(response.status.split(' ')[0]),
                    mimetype = 'application/json'
               )
        
    # ok
    else:
        response = app.response_class(
            response = json.dumps({
                'request url' : request.path,   
                'status code':int(response.status.split(' ')[0]),
                'issuccess': OK,
                'result': response.json.get('data', response.json)
            }),
            mimetype = 'application/json'
        )
        return response

# index
@app.route('/')
def index():
    return jsonify({"message":"Wellcome to my site"})     


#validate-parameters
global Metadata
Metadata={}

@api.route('/meta/<_class>')
class ManagementMetadata(Resource):
    def post(self, _class):
        global Metadata
        self._class = _class
        if request.path in ['/meta/dataset', '/meta/model', '/meta/training']:
            _json = request.get_json()
            attr_n = 'dict_to_{}'.format(self._class)
            get_param_method = getattr(transfer, attr_n)
            meta_value=dict(get_param_method(_json))
            Metadata[self._class] = meta_value
            res=make_response(meta_value)
            return res
        else:
            raise ApiException(400,'page not found',None)
                

#start-training
@api.route('/starttraining')
class StartFromMetadata(Resource):
    def post(self):
        _json = dict(request.get_json())
        check=[]
        for key in _json.keys():
            if key in ['dataset','model','training']:
                check.append(key)

            if len(check) == 3:
                get_param_method = getattr(transfer, 'dict_to_metadata')
                meta_value=get_param_method(_json)

        return dict(meta_value)
        # 

        #Ai Model Training Management.run()
# inference
@api.route('/result')
class SendResult(Resource):
    def post(self):
        pass
        # 데이터를 받고 (규칙 미정) // data = request.
        # 모델 id번호를 받고// id = dict(request.get_json())['id']
        # 모델을 찾아서  // model=model.open(id) 
        # 모델에 데이터를 넣어서 // result=model(data)
        # 출력으로 결과값을 전달한다. // return result 


if __name__ == '__main__':
    status = False
    app.run(debug=True, host='0.0.0.0', port=5555)   