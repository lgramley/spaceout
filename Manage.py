from Pitch import Pitch
from Account import Account
from Database import PitchDatabase
from Database import AccountDatabase
import numpy as np

class ManageGeneral:
    def __init__(self):
        self.pitch_db = PitchDatabase()
        self.account_db = AccountDatabase()

    def make_account(self, username, password, full_name, about, contact, past_projects):
        account = Account()

        while username in self.account_db.usernames:
            print("That username is not available. Please enter a new username.")
        account.username = username 
        self.account_db.usernames[username] = account
        account.password = password
        account.full_name = full_name
        account.about_me = about
        account.contact = contact
        account.past_projects = past_projects

        self.account_db.add_account(account)

        return account

    def sign_in(self, username, password):
        if username in self.account_db.usernames:
            account = self.account_db.usernames[username]
            if account.password != password:
                print("Username or password is incorrect. Please try again.")
                return
        else: 
            print("Username or password is incorrect. Please try again.")
            return
        
        return account

if __name__ == "__main__":
    """
    REPL to prompt user to enter information 
    """
    manager = ManageGeneral()
    prompt = input("Welcome to Space Out!\nWould you like to Sign In or Create an Account?\n")

    if prompt.lower() == "sign in":
        username = input("Please enter a username:\n")
        password = input("Please enter a password:\n")
        account = manager.sign_in(username, password)
    elif prompt.lower() == "create an account":
        username = input("Please enter a username:\n")
        password = input("Please enter a password:\n")
        full_name = input("Please enter your full name:\n")
        about = input("Please enter a blurb about yourself:\n")
        contact = input("Please enter your contact information:\n")
        past_projects = input("Please enter your past projects:\n")

        account = manager.make_account(username, password, full_name, about, contact, past_projects)
    else: 
        print("not recognized")

    while True:
        #clear term? 
        prompt = input("Welcome to your Account! Type c to create a pitch or b to browse pitches:\n")

        if prompt == "c":
            pitch = account.create_pitch()
            manager.pitch_db.add_pitch(pitch)
        elif prompt == "b": 
            while True:
                p = np.random.choice(manager.pitch_db.pitches)
                print(p)
                prompt = input("Type L to like, D to dislike, or Q to quit:")
                if prompt == "L":
                    account.liked_pitches.append(p)
                if prompt == "Q":
                    break
        else:
            print("not recognized")
            

