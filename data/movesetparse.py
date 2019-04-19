import json
import pickle

"""
Parse the movesets.json into a dictionary with "name": ["move"].
Save the dictionary as a pickle file.
"""
move_dict = {}
with open("data\movesets.json", "r") as data:
    move_sets = json.loads(data.read())
    for token in move_sets:
        if "randomBattleMoves" in move_sets[token]:
            move_dict[token] = move_sets[token]["randomBattleMoves"]
    
    data.close()
    pickle_on = open("random-movesets.pickle", "wb")
    pickle.dump(move_dict, pickle_on)
    pickle_on.close()
