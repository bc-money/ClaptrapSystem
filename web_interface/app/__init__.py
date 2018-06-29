import os
from flask import Flask
import db
import mapBlueprint

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'server/db.frm'),
)

# Load the config file
app.config.from_pyfile('server/config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

# connect the db functionality to the app object
db.init_app(app)

# connect the blueprints to the app object
app.register_blueprint(mapBlueprint.bp)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)