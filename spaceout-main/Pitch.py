from flask import Flask

class Pitch:
    def __init__(self, title, blurb, what_is, look_for): # any args?
        self.title = title
        self.blurb = blurb
        self.what_is = what_is
        self.look_for = look_for
        self.account = None
        # image?
        self.likes = 0
        self.dislikes = 0 
        self.taken = False

    def display_pitch(self):
        print(self.title)
        print(self.blurb)