from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

data = [
    {"name": "test1", "desc": "test1", "id": 1},
    {"name": "test2", "desc": "test2", "id": 2},
    {"name": "test3", "desc": "test3", "id": 3},
]

task_does_not_exist = {"msg": "task does not exist"}
names = ['test1', 'test2', "test3"]
task_exist = {"msg": "name is exist"}


@app.route('/api/tasks/<string:name>')
def get_task(name):
    if len(name) > 0 and name in names:
        for content in data:
            if name == content['name']:
                return make_response(jsonify(content), 200)
    else:
        return make_response(jsonify(task_does_not_exist), 404)


@app.route('/api/tasks/<string:name>', methods=['PUT'])
def update_task(name):
    if len(name) > 0 and name in names:
        for content in data:
            if name == content['name']:
                id = content["id"]
                data[id - 1] = request.json
        return make_response(jsonify(data[id - 1]), 204)
    else:
        abort(404)


@app.route('/api/tasks/<string:name>', methods=['DELETE'])
def delete_task(name):
    if len(name) > 0 and name in names:
        return make_response(jsonify(data), 204)
    else:
        abort(404)


@app.route('/api/tasks/', methods=['GET', 'POST'])
def create_task():
    if request.method == "GET":
        return make_response(jsonify(data), 200)
    name = request.json['name']
    if name in names:
        return make_response(task_exist, 400)
    else:
        names.append(name)
        data.append(request.json)
    return make_response(request.json, 201)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
