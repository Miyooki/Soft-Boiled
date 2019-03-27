import websockets
import asyncio
import requests
import json

API_ENDPOINT = ("http://localhost.psim.us/action.php") # This is where we make our POST requests.
USERNAME = "snowbot_1" # Can change
PASSWORD = "snowsnow123"

async def hello():
    """
    Connects to websocket.
    """
    async with websockets.connect("ws://localhost:8000/showdown/682/dgton5pw/websocket") as ws:
        await message_handler(ws)

async def message_handler(ws):
    # Loop that handles messages incoming from WebSocket
    async for msg in ws:
        print(msg) # Curse that black star character.
        if msg.startswith("|challstr"):
            chall_token = ("|").join(msg.split("|")[2:4]) # Get the token.
            assertion = login(chall_token)
            print(assertion)
            await ws.send("|/trn {},0,{}".format(USERNAME, assertion))

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
    #websocket.enableTrace(True)
    #ws = websocket.WebSocketApp("ws://sim.psim.us:8000/showdown/websocket", on_message = on_message, on_error = on_error)
    asyncio.get_event_loop().run_until_complete(hello())
    """
    print(ws.recv())
            ws.send("/challenge snowbot_2 gen7randombattle")
    """


