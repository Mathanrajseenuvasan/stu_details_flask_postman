from flask import Flask, request, json, jsonify
from flask.views import MethodView

app = Flask(__name__)

array = []
dictionary ={}

class Student(MethodView):
    
    def get(self):       
        return jsonify(array)
        
    # json format for post or put(update)
    # {"id":" ","name":" "}

    def post(self):
        dictionary = {'id' : request.json['id'], 'name' : request.json['name']}
        array.append(dictionary)
        return dictionary

    def put(self):
        for x in array:
            if x['id'] == request.json['id']:
                dictionary = x
                dictionary['name']=request.json['name']
            return dictionary
    
    # json format for delete
    # {"id":" "}

    def delete(self):
      for x in array:
        id = request.json['id']
        if x['id'] == id:
          dictionary = x
          array.remove(x)
      return 'successfully deleted'

app.add_url_rule('/student', view_func=Student.as_view('student'))

if __name__ == '__main__':
    app.run(debug=True)


