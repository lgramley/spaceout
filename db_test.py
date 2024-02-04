from Account import Account
from Pitch import Pitch
from Database import PitchDatabase, AccountDatabase
import numpy as np
from Manage import ManageGeneral

def model():
    manager = ManageGeneral()

    user1 = Account("user1", "1234", "User One", "123-456-7890", "front end", "I like frogs")
    user2 = Account("user2", "5678", "User Two", "u2@email.com", "full stack", "I like mustaches")
    user3 = Account("user3", "password", "User Three", "", "none", "I am creative")
    user4 = Account("user4", "password343", "User Four", "", "", "")

    manager.account_db.accounts = [user1, user2, user3, user4]
    manager.account_db.usernames = {"user1": user1, "user2": user2, "user3": user3, "user4": user4}

    pitch1 = Pitch("Pitch One", "this is a really creative pitch")
    pitch1.account = user1
    pitch2 = Pitch("Pitch Two", "this is a really smart pitch")
    pitch2.account = user3
    pitch3 = Pitch("Pitch Three","PITCH")
    pitch3.account = user3
    pitch4 = Pitch("Pitch Four", "this is another pitch")
    pitch4.account = user2

    manager.pitch_db.pitches = [pitch1, pitch2, pitch3, pitch4]

    user1.my_pitches = [pitch1]
    user2.my_pitches = [pitch4]
    user3.my_pitches = [pitch2, pitch3]

    pitch5 = user1.create_pitch("Pitch 5", "blurb blurb blurb")
    pitch6 = user2.create_pitch("Pitch 6", "words")
    pitch7 = user3.create_pitch("Pitch 7", "info")
    pitch8 = user4.create_pitch("Pitch 8", "stuff")
    pitch9 = user4.create_pitch("Pitch 9", "wowowowowo")
    pitch0 = user2.create_pitch("Pitch 0", "sfjdosdhff")
    pitch10 = user3.create_pitch("Pitch 10", "sfegsegs")

    manager.pitch_db.pitches.extend([pitch5, pitch6, pitch7, pitch8, pitch9, pitch0, pitch10])

    user5 = manager.make_account("user5", "73234567", "User Five", "me", "", "")
    user6 = manager.make_account("user6", "afesas", "User Six", "", "34567832", "")
    user7 = manager.make_account("user7", "adfew", "User Seven", "me", "", "")
    user8 = manager.make_account("user8", "65224", "User Eight", "me", "", "")
    user9 = manager.make_account("user9", "1232456", "User Nine", "me", "", "")

    return manager

# def random_match(account):
    
#     random_pitch = np.random.choice(manager.pitch_db.pitches)

#     return random_pitch

# while True:
#     p = random_match(user4)
#     while p.account == user4:
#         p = random_match(user4)
#     p.display_pitch()
#     prompt = input("Type L to like, D to dislike, or Q to quit:")
#     if prompt == "L":
#        user4.liked_pitches.append(p)
#        p.likes += 1
#     if prompt == "D":
#         p.dislikes += 1
#     if prompt == "Q":
#         break