import os, copy
from flask import Flask, jsonify, request, send_from_directory, make_response
app = Flask(__name__, static_url_path='')

# get root
@app.route("/")
def index():
    return app.make_response(open('app/index.html').read())

# send assets (ex. assets/js/random_triangle_meshes/random_triangle_meshes.js)
# blocks other requests, so your directories won't get listed (ex. assets/js will return "not found")
@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('app/assets/', path)

# API

import json 
data = []
with open('app/assets/data/api/yelp_academic_dataset_business.json') as f:
	for line in f:
		if "Las Vegas" in line:
			data.append(json.loads(line))

@app.route('/api/v1.0/data/some_data/', methods=['GET'])
def get_some_data():
	#return jsonify({'businesses':data})
	return json.dumps(data)
    #with open('app/assets/json/baseball.json') as data_file:
	#return json.dumps(json.load(data_file))


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5050))
	app.run(host='0.0.0.0', port=port, debug=False)

# set debug=True if you want to have auto-reload on changes
# this is great for developing

