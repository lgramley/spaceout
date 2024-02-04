# prompt users to enter account information
# which is then stored in a database
from Pitch import Pitch

class Account:
    def __init__(self, username, password, full_name, contact, past_projects, about_me): # any args?
        self.username = username
        self.password = password
        self.full_name = full_name
        self.contact = contact
        self.past_projects = past_projects
        self.about_me = about_me
        
        self.my_pitches = [] # have make pitch function 

        self.liked_pitches = [] #pitches you have liked 
        
    def create_pitch(self, title, blurb, what_is, look_for):
        pitch = Pitch(title, blurb, what_is, look_for)

        pitch.account = self
        self.my_pitches.append(pitch)

        return pitch

    