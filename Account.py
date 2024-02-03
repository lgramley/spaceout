# prompt users to enter account information 
# which is then stored in a database
from Pitch import Pitch

class Account:
    def __init__(self): # any args?
        self.username = ""
        self.password = ""
        self.full_name = ""
        self.contact = None
        self.past_projects = None
        self.about_me = None 
        
        self.my_pitches = [] # have make pitch function 

        self.liked_pitches = [] #pitches you have liked 
        
    def create_pitch(self):
        pitch = Pitch()

        title = input("Title:")
        pitch.title = title

        blurb = input("Blurb:")
        pitch.blurb = blurb

        pitch.account = self
        self.my_pitches.append(pitch)

        return pitch

    