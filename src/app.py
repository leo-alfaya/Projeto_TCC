from flask import Flask, request, jsonify
import core

app = Flask("src")

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		page = core.get_page("http://www.g1.globo.com")
		result = core.get_element(page, ".bstn-fd-cover-picture img")

		"""return jsonify({"success":"ok", "data":result})"""
		return "<h1>Teste</h1>"
if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
