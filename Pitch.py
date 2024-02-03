class Pitch:
    def __init__(self): # any args?
        self.title = ""
        self.blurb = ""
        self.account = None
        # image?
        self.likes = 0
        self.dislikes = 0 
        self.taken = False

    def display_pitch(self):
        print(self.title)
        print(self.blurb)