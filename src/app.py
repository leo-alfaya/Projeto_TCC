from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import core

app = Flask(__name__, 
            static_folder = "./dist/static",
            template_folder = "./dist")
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


# fetch('http://localhost:5000/', {
#             method:'POST',
#             headers:{
#                 'Content-Type':'application/json'
#             },
#             body:JSON.stringify({
#				 "url":"http://webscraper.io/test-sites/e-commerce/allinone",
#				 "search_params":{
# 					"img":".img-responsive",
# 					"titulo":".title",
# 					"preço":".price"
# 				}
#			 })
#         })
#         .then(response=>response.json())
#         .then(data=>{
#             console.log(data);
#         })
#         .catch(data=>console.log(data))
