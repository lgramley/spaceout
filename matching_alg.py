import numpy as np
import pandas as pd
import make_account
import make_pitch

#want a getter to get all accounts
#want a getter to get all pitches
#populate these into a dictionary


#Gale-Shapely algorithm::

#initialization:

# #dataframe for accounts
# accounts = pd.DataFrame(getAccounts())
# accounts.index = []

# #dataframe for pitches
# pitches = pd.DataFrame(getPitches())
# pitches.index = []

accounts = [getAccounts()] #populates these/call on something
pitches = [getPitches()] #populates these/call on something

#preference creation

#creators that pitches prefer: (M)
pitch_pref = {} #populate this key: pitch, value: list of creators the pitcher likes

#pitches that creators prefer: (W) / for accounts looking to create
creator_pref = {} #populate this key: creator, Value: list of pitches that creator likes

def match_alg():
    #Gale-Shapely

    #self.taken = False or True --> all initialized to False
    free_pitches = []
    free_creators = []
    #maybe just start with all creators and pitchers
    for creator in accounts: #techincally pitches are parts of accounts
        if not creator.taken:
            free_creators.append(creator)
    for pitch in pitches:
        if not creator.taken:
            free_pitches.append(pitch)

    matches = {} #will add to this as we populate dict
    #key: pitch, value: creator matched to !!It is my understanding this is a final match
    
    #while there are remaining pitches that have not been claimed
    while(len(free_pitches) > 0):
        for pitch in matches.keys():
            for creator in pitch_pref[pitch]:
                if creator not in list(matches.values()):
                    matches[pitch] = creator
                    free_creators.remove(creator)
                    break
                elif creator in list(matches.values()):
                    current_potential_match = list(matches.keys())[list(matches.values()).index(creator)] #?? --> need to index these
                    creator_list = creator_pref.get(creator)
                    if creator_list.index(pitch) < creator_list.index(current_potential_match):#entries seem to be indexed could probably weight indeces
                        matches[pitch] = creator
                        free_pitches.remove(pitch)
                        matches[current_potential_match] = ''
                        free_pitches.append(current_potential_match)


#---------------------------------------------------------------
#check if account is a match --> move somewhere else later
def isMatch(account, pitch):
    pass

#gets info from pitch for account if account is a match
def getInfo(account, pitch):
    pass



