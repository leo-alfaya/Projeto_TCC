from flask import Flask, request
import core

app = Flask("src")

base_html = u"""
	<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
	</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		dados_form = request.form.to_dict()

		page = core.get_page(dados_form['url'])
		posts = core.get_element(page, dados_form['elemento'])

		return base_html.format(title="Projeto TCC", body=posts)
	else:
		formulario = """
			<form method="post" action="/">
				<label>Url:
					<input type="text" name="url">
				</label>
				<br/>
				<label>Selector CSS:
					<input type="text" name="elemento">
				</label>
				<button type="submit" />Enviar
			</form>
		"""

		return base_html.format(title="Projeto TCC", body=formulario)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)