from commands.interact import say, leaveroom
from training.random import random_move, random_switch
import json

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

# Global Variables
PLAYER_ID = None
CURRENT_POKE = None
POKE_TEAM = []
POKE_ALIVE = []
ALL_MOVES = []
USABLE_MOVES = []

async def battle_parser(ws, msg):
    global PLAYER_ID, CURRENT_POKE, POKE_TEAM, POKE_ALIVE, ALL_MOVES, USABLE_MOVES
    turns = 0 # Fix turns.
    msg = msg.splitlines()
    tag = msg[0].split("|")[0][1:] # Get the battle tag ID.
    for state in msg[1:]:
        state = state.split("|")

        if state[1] == "request" and PLAYER_ID == None:
            # Initial info update.
            if len(state[2]) > 0:
                battle_data = json.loads(state[2])
                PLAYER_ID = battle_data["side"]["id"]
                for species in battle_data["side"]["pokemon"]: # A list object.
                    POKE_TEAM.append(species["ident"][4:].lower())
                for move in battle_data["active"][0]["moves"]:
                        if move["disabled"] == False:
                            USABLE_MOVES.append(move["id"])
                POKE_ALIVE = POKE_TEAM
                await say(ws, "glhf c:", tag) # Appear friendly.

        elif state[1] == "request":
            if len(state[2]) > 0:
                battle_data = json.loads(state[2])
                CURRENT_POKE = battle_data["side"]["pokemon"][0]["ident"][4:].lower() # Get ID of current Pokemon.
                if "forceSwitch" in battle_data:
                    POKE_ALIVE.remove(CURRENT_POKE)
                    if battle_data["side"]["pokemon"][0]["condition"] == "0 fnt": # Current Pokemon fainted.
                        await random_switch(ws, POKE_ALIVE, tag, turns)
                    else:
                        await random_switch(ws, POKE_ALIVE, tag, turns) # Current Pokemon got switched out.
                        POKE_ALIVE.append(CURRENT_POKE)

                if "active" in battle_data: # Get non-disabled moves.
                    USABLE_MOVES = [] # Clear moves memory.
                    for move in battle_data["active"][0]["moves"]:
                        if move["disabled"] == False:
                            USABLE_MOVES.append(move["id"])

        elif state[1] == "turn":
            await random_move(ws, USABLE_MOVES, tag, turns) # Testing with random moves.

        elif state[1] == "win":
            await say(ws, "ggwp c:", tag)
            await say(ws, "/savereplay", tag)
            await leaveroom(ws, tag)

        elif state[1] == "error":
            await random_move(ws, tag, turns) # Ghetto fix for now.

        elif state[1] == "c": 
            # A message was sent or received.
            # await say(ws, "don't talk to me kiddo.", tag)
            continue
