from flask import Flask
from prediction import prediction


app = Flask(__name__)
FLASK_APP=app
FLASK_DEBUG = 1
app.register_blueprint(prediction)

FLASK_APP=app
if __name__ == '__main__':
    app.run(port=9200)