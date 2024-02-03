from Account import Account
from Pitch import Pitch
from Database import PitchDatabase, AccountDatabase
import numpy as np

user1 = Account()
user1.username = "user1"
user1.password = "1234"
user1.full_name = "User One"
user1.contact = "123-456-7890"
user1.past_projects = "front end"
user1.about_me = "I like frogs"

user2 = Account()
user2.username = "user2"
user2.password = "5678"
user2.full_name = "User Two"
user2.contact = "u2@email.com"
user2.past_projects = "full stack"
user2.about_me = "I like mustaches"

user3 = Account()
user3.username = "user3"
user3.password = "password"
user3.full_name = "User Three"
user3.contact = ""
user3.past_projects = "none"
user3.about_me = "I am creative"

user4 = Account()
user4.username = "user4"
user4.password = "password343"
user4.full_name = "User Four"
user4.contact = ""
user4.past_projects = ""
user4.about_me = ""

account_db = AccountDatabase()
account_db.accounts = [user1, user2, user3]
account_db.usernames = {"user1": user1, "user2": user2, "user3": user3}

pitch1 = Pitch()
pitch1.title = "Pitch One"
pitch1.blurb = "this is a really creative pitch"
pitch1.account = user1

pitch2 = Pitch()
pitch2.title = "Pitch Two"
pitch2.blurb = "this is a really smart pitch"
pitch2.account = user3

pitch3 = Pitch()
pitch3.title = "Pitch Three"
pitch3.blurb = "PITCH"
pitch3.account = user3

pitch4 = Pitch()
pitch4.title = "Pitch Four"
pitch4.blurb = "this is another pitch"
pitch4.account = user2

pitch_db = PitchDatabase()
pitch_db.pitches = [pitch1, pitch2, pitch3, pitch4]

user1.my_pitches = [pitch1]
user2.my_pitches = [pitch4]
user3.my_pitches = [pitch2, pitch3]

def random_match(account):
    
    random_pitch = np.random.choice(pitch_db.pitches)

    return random_pitch

while True:
    p = random_match(user4)
    while p.account == user4:
        p = random_match(user4)
    p.display_pitch()
    prompt = input("Type L to like, D to dislike, or Q to quit:")
    if prompt == "L":
       user4.liked_pitches.append(p)
       p.likes += 1
    if prompt == "D":
        p.dislikes += 1
    if prompt == "Q":
        break