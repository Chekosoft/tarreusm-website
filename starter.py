from flask import *
from tournament_organizer import *
from mongoengine import connect

app = Flask(__name__)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

db = connect('tarreusm')
