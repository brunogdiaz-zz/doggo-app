from flask import Flask, request
app = Flask(__name__, instance_relative_config=True)

'''
GET /dogs - List all dogs
POST /dogs - Add a new dog 😄
GET /dogs/:id - Get details for one dog
PUT /dogs/:id - Update details for one dog
DELETE /dogs/:id - Remove a dog ☹️
'''
@app.route('/dogs', methods=['GET', 'POST'])
def dogs():
    return "Hello World!"

@app.route('/dogs/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dogs_id(id):
    return str(id)

if __name__ == '__main__':
    app.run()
