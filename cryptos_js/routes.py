from cryptos_js import app

@app.route("/")
def index():
    return "Flask rulando"
