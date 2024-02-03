import make_account
import numpy as np

#random match can be the default/ackup if the algorithm fails or doesnt return anything

#
# input: set of accounts to randomly match
# output: list(?) of matches
# matching creator to ideas: matching developer account to a pitch
# pitch class and account class: match account to a pitch

#creates/adds one match, returns as part of a dictionary
random_pitch_dict = {}


def random_match(pitches, accounts):
    
    random_pitch = np.random(pitches)
    random_account = np.random(accounts)

    if random_account not in random_pitch_dict.keys():
        random_pitch_dict[random_account] = [random_pitch]
    else:
        random_pitch_dict[random_account].append(random_pitch)

    return random_pitch_dict



