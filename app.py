
from flask import Flask,jsonify,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Creating flask application
@app.route('/')
def assign():
    return "Devops_Assign Project"


#Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200


#Simple REST API
fakeDatabase = {
    1:{'Name':'Ihsan'},
    2:{'Status':'Unemployed'},
    3:{'Current':'Applying'},
}

##Create & Read Items
class Items(Resource):
    def get(self):
        return fakeDatabase                         

    def post(self):
        data = request.get_json()
        new_id = len(fakeDatabase) + 1
        fakeDatabase[new_id] = data
        return data, 201

##Read,update,delete items
class Item(Resource):
    def get(self, pk):
        return fakeDatabase.get[pk,{"message":"Not found"}]

    def put(self, pk):
        data = request.get_json()
        fakeDatabase[pk] = data
        return data

    def delete(self, pk):
        fakeDatabase.pop(pk, None)
        return {"message": "Deleted"}




api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<int:pk>')

if __name__ == '__main__':
   app.run(debug=True)

