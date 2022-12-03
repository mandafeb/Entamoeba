from flask import Flask
from . import views

# Create a Flask Application
app = Flask(__name__)
app.register_blueprint(views.model)

def run():
    app.run(debug=True)