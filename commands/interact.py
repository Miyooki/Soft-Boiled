
async def say(ws, msg):
    """
    Sends requests to websocket.
    """
    out = "|" + msg # All commands start with "|".
    print(">> {}".format(out))
    await ws.send(out)

async def challenge(ws, user, mode="gen7ou"):
    """
    Challenge another player in specified format.
    Defaults to Gen 7 OU.
    """
    msg = "/challenge {}, {}".format(user, mode)
    await say(ws, msg)

