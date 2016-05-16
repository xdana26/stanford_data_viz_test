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

@app.route('/api/limit/<int:n_entries>/', methods=['GET'])
def get_some_data(n_entries):
	with open('app/data/api/yelp_academic_dataset_business.json') as data_file:
		return json.dumps(json.load(data_file)[0:n_entries])


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5050))
	app.run(host='0.0.0.0', port=port, debug=False)

# set debug=True if you want to have auto-reload on changes
# this is great for developing

