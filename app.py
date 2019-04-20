from flask import Flask, request, jsonify
import json
app = Flask(__name__, instance_relative_config=True)

@app.route('/dogs', methods=['GET', 'POST'])
def dogs():
    if request.method == 'POST':
        dog = request.get_json()
        with open('dogs.json', 'r') as db:
            data = json.load(db)
        new_id = data['lastAdded'] + 1
        data['lastAdded'] = new_id
        data['dogs'][new_id] = dog
        with open('dogs.json', 'w') as db:
            json.dump(data, db)
        return ''
    elif request.method == 'GET':
        with open('dogs.json', 'r') as db:
            db = json.load(db)
            return jsonify(db['dogs'])

@app.route('/dogs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dog(id):
    id = str(id)
    with open('dogs.json', 'r') as db:
        data = json.load(db)
    if id not in data['dogs']:
        return '', 400
    if request.method == 'DELETE':
        del data['dogs'][id]
        with open('dogs.json', 'w') as db:
            json.dump(data, db)
        return ''
    elif request.method == 'PUT':
        data['dogs'][id] = request.get_json()
        with open('dogs.json', 'w') as db:
            json.dump(data, db)
        return ''
    elif request.method == 'GET':
        return jsonify(data['dogs'][id])

