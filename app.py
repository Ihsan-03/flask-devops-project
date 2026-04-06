
from flask import Flask,jsonify,request
from flask_restful import Resource, Api

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="ihsan",
    password="5656",
    database="assignment_db" )



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


##Simple REST API
##fakeDatabase = {
 ##   1:{'Name':'Ihsan'},
  ##  2:{'Status':'Unemployed'},
 ##  3:{'Current':'Applying'},
##}

##Create & Read Items
class Items(Resource):
    def get(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM items")
        data = cursor.fetchall()
        cursor.close()  
        return data

    def post(self):
        data = request.get_json()
        name = data['name']
        cursor =db.cursor()
        cursor.execute("INSERT INTO items(name) VALUES(%s)", (name,))
        db.commit()
        cursor.close()
        return {"message": "Item added"}, 201


##Read,update,delete items
class Item(Resource):
    def get(self, pk):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM items WHERE id=%s", (pk,))
        data = cursor.fetchone()
        cursor.close()
        return data if data else {"message": "Not found"}

    def put(self, pk):
        data = request.get_json()
        name = data['name']
        cursor = db.cursor()
        cursor.execute("UPDATE items SET name=%s WHERE id=%s", (name, pk))
        db.commit()
        cursor.close()
        return {"message": "Updated"}

    def delete(self, pk):
        cursor = db.cursor()
        cursor.execute("Delete from items where id=%s", (pk,))
        db.commit()
        cursor.close()
        return{"message":"Deleted"}



api.add_resource(Items, '/items')
api.add_resource(Item, '/items/<int:pk>')

if __name__ == '__main__':
   app.run(debug=True)

