from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from util.Judge import Judge
from util.ErrorHandler import error_handle
import util.ConfigParser as ConfigParser

app = Flask(__name__)
api = Api(app)
error_handle(app)
CORS(app)

api.add_namespace(Judge, '/judge')

if __name__ == "__main__":
    parser = ConfigParser.read()
    host = parser["server"]["host"]
    port = int(parser["server"]["port"])
    app.run(debug=True, host=host, port=port) 
