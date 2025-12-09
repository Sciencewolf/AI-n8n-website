from flask import Flask, request
import json

app = Flask(__name__)
app.config['stories_dir'] = '/home/aron/AI-n8n-website/backend/stories'

@app.route('/')
def index():
    return 'Hello World'

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        get_body = request.json
        title = str(get_body['title']).replace(' ', '_')

        with open(f"{app.config['stories_dir']}/{title}.json", 'w') as file:
            json.dump(get_body, file)

        return f"'{title}' added.", 200

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  