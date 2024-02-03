# prompt users to enter account information 
# which is then stored in a database

class Account:
    def __init__(self): # any args?
        self.account_name = ""
        self.password = ""
        self.full_name = ""
        self.contact = ""
        self.past_projects = ""
        
        self.pitches = []


if __name__ == "__main__":
    """
    REPL to prompt user to enter information 
    """

    account = Account()

    while True:
        query = input("What would you like to search:")
        if query == ":quit":
            break
        q.handle_query(query)