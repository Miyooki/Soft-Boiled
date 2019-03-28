from commands.interact import say
from training.random import random_move, random_switch
import json
import webbrowser

class Mew:
    """
    """
    def __init__(self):
        self.turns = 0
        self.my_team = None
        self.enemy_team = None
        self.current_pkm = None
        self.player_id = ""
        self.weather = ""
        self.screens = {
            "lightscreen": False,
            "reflect": False,
            "aurora-veil": False
        }

PLAYER_ID = None

async def battle_parser(ws, msg):
    global PLAYER_ID
    turns = 0 # Fix turns.
    msg = msg.splitlines()
    tag = msg[0].split("|")[0][1:] # Get the battle tag ID.
    for state in msg[1:]:
        state = state.split("|")

        if state[1] == "request" and PLAYER_ID == None:
            if len(state[2]) > 0:
                battle_data = json.loads(state[2])
                PLAYER_ID = battle_data["side"]["id"]

        elif state[1] == "turn":
            await random_move(ws, tag, turns) # Testing with random moves.

        elif state[1] == "faint":
            if PLAYER_ID == state[2][:2]:
                await random_switch(ws, tag, turns)

        elif state[1] == "win":
            await say(ws, "/savereplay", tag)
            replay = tag[7:] # Discard "battle-" as it's not needed for replay link.
            # webbrowser.open("https://replay.pokemonshowdown.com/" + replay)

        elif state[1] == "error":
            await random_move(ws, tag, turns) # Ghetto fix for now.

        elif state[1] == "c": 
            # A message was sent.
            continue
