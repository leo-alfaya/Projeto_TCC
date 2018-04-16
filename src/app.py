from flask import Flask, request, jsonify
import core

app = Flask("src")

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		data = {
			"tema":".feed-post-header",
			"titulo":".feed-post-body-title"
		}

		result = core.make_search("http://www.g1.globo.com", data)


		return jsonify(list(result.values()))


if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
