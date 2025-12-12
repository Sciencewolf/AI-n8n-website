from flask import Flask, request, jsonify
import json
import os

# todo: migration to supabase

app = Flask(__name__)
app.config['stories_dir'] = '/home/aron/AI-n8n-website/backend/stories'
app.config['story_ids_path'] = app.config['stories_dir'] + '/' + 'story_ids.json'

@app.route('/')
def index():
    return 'Hello World'

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        get_body = request.json
        title = str(get_body['title']).replace(' ', '_')
        _id = str(get_body['id'])

        story_path = f"{app.config['stories_dir']}/{title}.json"

        with open(story_path, 'w') as file:
            json.dump(get_body, file, indent=4)

        ids_path = f'{app.config["stories_dir"]}/story_ids.json'

        if os.path.exists(ids_path):
            with open(ids_path, 'r') as file:
                story_ids = json.load(file)
        else:
            story_ids = {}

        story_ids[_id] = title

        with open(ids_path, 'w') as file:
            json.dump(story_ids, file, indent=4)

        return jsonify({'info': f"'{title}' added."}), 200
    
    return None


@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        _id = str(request.args.get('id'))

        with open(app.config['story_ids_path'], 'r') as file:
            ids = json.load(file)

            for i in ids:
                if i == _id:
                    with open(f"{app.config['stories_dir']}/{ids[i]}.json", 'r') as file:
                        story = json.load(file)
                        return story, 200
        
        return jsonify({'info': "No story found."}), 200
    
    return None


@app.route('/get_all', methods=['GET'])
def get_all():
    if request.method == 'GET':
        stories_json_dir = os.listdir(app.config['stories_dir'])
        stories = list()

        for story_file in stories_json_dir:
            if story_file not in ['.gitignore', 'story_ids.json']:
                path = app.config['stories_dir'] + '/' + story_file

                with open(path, 'r') as file:
                    stories.append(json.load(file))
        
        return jsonify(stories), 200
    
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  