class PitchDatabase:
    def __init__(self):
        self.pitches = []
    
    def add_pitch(self, pitch):
        self.pitches.append(pitch)
    
    def delete_pitch(self, pitch):
        self.pitches.remove(pitch)

class AccountDatabase:
    def __init__(self):
        self.accounts = []
        self.usernames = {}
    
    def add_account(self, account):
        self.accounts.append(account)
        self.usernames[account.username] = account
    
    def delete_account(self, account):
        self.accounts.remove(account)
        del self.usernames[account.username]