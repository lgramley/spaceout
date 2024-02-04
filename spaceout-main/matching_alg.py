import numpy as np
from Account import Account
from Pitch import Pitch
from Database import PitchDatabase, AccountDatabase
import random

#Gale-Shapely algorithm::

account_db = AccountDatabase()
pitch_db = PitchDatabase()

accounts =  account_db.accounts #populates these/call on something
pitches =  pitch_db.pitches #populates these/call on something

#preference creation

#creators that pitches prefer: (M)
pitch_pref = {} #populate this key: pitch, value: list of creators the pitcher likes
for pitch in pitches:
    shuffled_accounts = random.shuffle(accounts)
    pitch_pref[pitch] = shuffled_accounts #randomize order of accounts

#pitches that creators prefer: (W) / for accounts looking to create
account_pref = {} #populate this key: creator, Value: list of pitches that creator likes
for creator in account_pref:
    shuffled_pitches = random.shuffle(pitches)
    account_pref[creator] = shuffled_pitches #randomize order of pitches

def match_alg():
    #Gale-Shapely

    #self.taken = False or True --> all initialized to False
    free_pitches = []
    #I think once pitches are claimed they go away but accounts always stay visible until removed from the app


    # free_account = []
    # #maybe just start with all creators and pitchers
    # for account in accounts: #techincally pitches are parts of accounts
    #     if not account.taken:
    #         free_account.append(creator)
    for pitch in pitches:
        if not pitch.taken:
            free_pitches.append(pitch)

    matches = {} #will add to this as we populate dict
    #key: pitch, value: creator matched to !!It is my understanding this is a final match
    
    #while there are remaining pitches that have not been claimed
    while(len(free_pitches) > 0):
        for pitch in matches.keys():
            for creator in pitch_pref[pitch]:
                if creator not in list(matches.values()):
                    matches[pitch] = creator
                    # free_account.remove(creator)
                    break
                elif creator in list(matches.values()):
                    current_potential_match = list(matches.keys())[list(matches.values()).index(creator)] #?? --> need to index these
                    creator_list = account_pref.get(creator)
                    if creator_list.index(pitch) < creator_list.index(current_potential_match):#entries seem to be indexed could probably weight indeces
                        matches[pitch] = creator
                        free_pitches.remove(pitch)
                        matches[current_potential_match] = ''
                        free_pitches.append(current_potential_match)
    
    return matches






