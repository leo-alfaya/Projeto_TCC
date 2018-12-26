
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        url = "http://webscraper.io/test-sites/e-commerce/allinone"
        search_params = {
                "img":".thumbnail .img-responsive",
                "titulo":".title",
                "preço":".price"
        }

        result = core.make_search(url, search_params)

        return jsonify(result)
    else:
        req = request.json
        result = core.make_search(req['url'], req['search_params'])

        return jsonify(result)

@app.route("/block", methods=["GET", "POST"])
def block():
    if request.method == "GET":
        url = "http://webscraper.io/test-sites/e-commerce/allinone"
        block = ".thumbnail"
        search_params = {
                "img":".img-responsive",
                "titulo":".title",
                "preço":".price"
        }

        result = core.make_search_by_block(url, block, search_params)

        return jsonify(result)
    else:
        req = request.json
        result = core.make_search_by_block(req['url'], req['block'], req['search_params'])

        return jsonify(result)
