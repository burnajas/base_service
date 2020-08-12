import logging
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sys

app = Flask(__name__)

# Where are we?
# dir_path = os.path.dirname(os.path.realpath(__file__))

# Get production database parameters
DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_URL = os.environ.get('DATABASE_URL')
DATABASE = os.environ.get('DATABASE')

# Configure database depending on environment
db = None
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if os.environ.get('ENVIRONMENT_TYPE') == 'production':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}:5432/{db}'.format(user=DATABASE_USERNAME,
                                                                                                 pw=DATABASE_PASSWORD,
                                                                                                 url=DATABASE_URL,
                                                                                                 db=DATABASE)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}'.format(DATABASE_USERNAME, DATABASE_PASSWORD,
    #                                                                   DATABASE_URL)
    db = SQLAlchemy(app)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # Create database
    db = SQLAlchemy(app)

ma = Marshmallow(app)

# Logging important!
logger = logging.getLogger("pylog")
logger.setLevel(logging.DEBUG)
h1 = logging.FileHandler(filename="/tmp/records.log")
h1.setLevel(logging.INFO)
h2 = logging.StreamHandler(sys.stderr)
h2.setLevel(logging.ERROR)
logger.addHandler(h1)
logger.addHandler(h2)


@app.route('/')
def alive():
    '''
    An endpoint to work with.
    :return:
    '''

    test_1 = Test(name="Name")
    logger.info("{}".format(test_1))
    db.session.add(test_1)
    db.session.commit()
    ans = Test.query.first()
    logger.info("{}".format(ans))
    # return 'Application service is working.'

    test_schema = TestSchema()

    return test_schema.dump(ans)


# Define database tables
class Test(db.Model):
    # __table__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(63))

    def __repr__(self):
        return '<name %r>' % self.name


# Define Marshmallow schemas (eases object serialisation)
class TestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Test

    id = ma.auto_field()
    name = ma.auto_field()


# Build a database to use of working outside production environment
if os.environ.get('ENVIRONMENT_TYPE') != 'production':
    # Create test database tables
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
