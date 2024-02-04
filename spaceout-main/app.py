from flask import Flask, render_template, request, jsonify
from Account import Account
from Database import AccountDatabase, PitchDatabase
from Pitch import Pitch
from db_test import model
from flask import json
import numpy as np

app = Flask(__name__)

# look at why launch does not raise error 
@app.route('/')
def index():

    manager = model()
    json_lst = []
    for pitch in manager.pitch_db.pitches:
        if pitch.account != manager.curr_acc:
            cur_pitch = {"title": pitch.title, "blurb": pitch.blurb, "what_is": pitch.what_is, "look_for": pitch.look_for, "account": {"full_name": pitch.account.full_name}}
            json_lst.append(cur_pitch)

    np.random.shuffle(json_lst)

    return render_template('index.html', user=manager.curr_acc, pitches=json_lst)

@app.route('/increment_likes/<string:pitch_title>', methods=['POST'])
def increment_likes(pitch_title):
    # Find the item in the dataset with the given ID
    manager = model()
    item = next((pitch for pitch in manager.pitch_db.pitches if pitch.title == pitch_title), None)
    if item:
        # Increment the count
        item.likes += 1
        manager.curr_acc.liked_pitches.append(item)
        return item.title
    else:
        # Return an error response with status code 404
        return jsonify({"error": "Item not found"}), 404

@app.route('/increment_dislikes/<string:pitch_title>', methods=['POST'])
def increment_dislikes(pitch_title):
    # Find the item in the dataset with the given ID
    manager = model()
    item = next((pitch for pitch in manager.pitch_db.pitches if pitch.title == pitch_title), None)
    if item:
        # Increment the count
        item.dislikes += 1
        return item.title
    else:
        # Return an error response with status code 404
        return jsonify({"error": "Item not found"}), 404
