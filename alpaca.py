from flask import Flask, request

app = Flask(__name__)

endpoints = {}


@app.route('/__clear', methods=['POST'])
def clear():
    global endpoints
    endpoints = {}
    return '', 204, {'Content-Type': 'application/json'} 


@app.route('/__setup/<path:endpoint>', methods=['POST'])
def setup(endpoint):
    global endpoints
    args = request.args
    headers = {}
    method = args.get('method', 'GET')
    status = args.get('status', 200)
    for k, v in args.items():
        if k in ['method', 'status']:
            continue
        headers[k] = v
    endpoints[(method, endpoint)] = (request.data, status, headers)
    return '', 204, {'Content-Type': 'application/json'}


@app.route('/<path:endpoint>')
def spit(endpoint, methods=['GET', 'POST']):
    return endpoints.get(
        (request.method, endpoint),
        ('', 404, {'Content-Type': 'application/json'})
    )