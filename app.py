from flask import Flask, render_template
from Account import Account
from Database import AccountDatabase, PitchDatabase
from Pitch import Pitch
from db_test import model

app = Flask(__name__)

@app.route('/')
def index():
    user = Account("mwalsh", "1234", "Mikayla Walsh", "mikayla_walsh@brown.edu", "back end dev", "I am student at Brown.")
    user.create_pitch("My Pitch", "This is my pitch about a pitch.")

    manager = model()

    return render_template('index.html', user=user, account_db=manager.account_db, pitch_db=manager.pitch_db)