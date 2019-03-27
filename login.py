import websockets
import asyncio
import requests
import json
import sys
from commands.interact import say, challenge

API_ENDPOINT = "http://play.pokemonshowdown.com/action.php?" # This is where we make our POST requests.
WEBSOCKET = "ws://sim.smogon.com:8000/showdown/websocket" # Address of the websocket.
# "ws://localhost:8000/showdown/682/dgton5pw/websocket" Localhost websocket.
USERNAME = "" # Test user. Challenge snowbot_2 as snowbot_1.
PASSWORD = ""

async def hello():
    """
    Connects to Showdown websocket and handles messages being sent.
    """
    async with websockets.connect(WEBSOCKET) as ws:
        await message_handler(ws)

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
                # await challenge(ws, "snowbot_2", "gen7randombattle")
            if data[1] == "updatechallenges":
                print(">> Challenged by: " + data[2])

def login(token):
    login_request = {"act": "login",
                    "name": USERNAME,
                    "pass": PASSWORD,
                    "challstr": token}
    resp = requests.post(url = API_ENDPOINT, data = login_request)
    assertion = json.loads(resp.text[1:])["assertion"] # Convert to JSON format and get the assertion value.
    # The first char of resp.text is "]", hence [1:].
    return assertion

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:\tlogin.py USERNAME PASSWORD\n")
        exit(1)
    else:
        USERNAME = sys.argv[1]
        PASSWORD = sys.argv[2]

    asyncio.get_event_loop().run_until_complete(hello())
