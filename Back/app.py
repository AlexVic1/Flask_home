from flask import Flask,request
from flask_cors import CORS
api = Flask(__name__)
CORS(api)
myData=[{"name":"alex","age":25,"city":"ashqelon"}]

@api.route('/')
def hello():
    return 'Hello, World! Alex Homework'

@api.route('/students',methods=['GET','POST','DELETE'])
def students():
    if request.method =="GET":
       return myData
    if request.method =="POST":
        myData.append({"name":"yuval","age":25})
        return myData
    #if request.method =="DELETE":
       #return myData
 
if __name__ == '__main__':
    api.run(debug=True)