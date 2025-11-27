from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        pass

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        pass

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        pass

@app.route('/get/<id>', methods=['GET'])
def get(id):
    if request.method == 'GET':
        pass

@app.route('/get_all', methods=['GET'])
def get_all():
    if request.method == 'GET':
        pass
