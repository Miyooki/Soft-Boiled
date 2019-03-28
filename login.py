import websockets
import asyncio
import requests
import json
import sys
from commands.interact import say, challenge
from commands.battle import battle_parser

API_ENDPOINT = "http://play.pokemonshowdown.com/action.php?" # This is where we make our POST requests.
WEBSOCKET = "ws://sim.smogon.com:8000/showdown/websocket" # Address of the websocket.
# "ws://localhost:8000/showdown/682/dgton5pw/websocket" Localhost websocket.
USERNAME = "snowbot_1" # Test user. Challenge snowbot_2 as snowbot_1.
PASSWORD = "snowsnow123"

async def hello():
    """
    Connects to Showdown websocket and handles messages being sent.
    """
    async with websockets.connect(WEBSOCKET) as ws:
        await message_handler(ws)

def login(token):
    login_request = {"act": "login",
                    "name": USERNAME,
                    "pass": PASSWORD,
                    "challstr": token}
    resp = requests.post(url = API_ENDPOINT, data = login_request)
    assertion = json.loads(resp.text[1:])["assertion"] # Convert to JSON format and get the assertion value.
    # The first char of resp.text is "]", hence [1:].
    return assertion

async def message_handler(ws):
    # Loop that handles messages incoming from WebSocket
    async for msg in ws:
        print(msg.encode("utf-8")) # Curse that black star character.
        data = msg.split("|")
        if len(data) > 1: # Check that data is valid.

            if data[1] == "challstr":
                chall_token = ("|").join(data[2:4]) # Get the token.
                assertion = login(chall_token)
                await say(ws, "/trn {},0,{}".format(USERNAME, assertion))

            if data[1] == "updateuser":
                print(">> Sucessfully logged in as: " + USERNAME)

            if data[1] == "updatechallenges":
                chall_users = json.loads(data[2])
                chall_from = chall_users["challengesFrom"]
                chall_to = chall_users["challengeTo"]
                for users in chall_from:
                    print(">> Challenged by: {} to {}".format(users, chall_from[users]))
                    await say(ws, "/accept {}".format(users))

            if "battle" in data[0]:
                await battle_parser(ws, msg) # Battle starts and is sent to the parser.


if __name__ == "__main__":
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Usage:\tlogin.py USERNAME PASSWORD\n")
        exit(1)
    elif len(sys.argv) == 3:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]

    asyncio.get_event_loop().run_until_complete(hello())
