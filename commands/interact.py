
async def say(ws, msg, prefix="", suffix=""):
    """
    Sends requests to websocket.
    """
    if len(suffix) > 0:
        out = prefix + "|" + msg + "|" + suffix
    else:
        out = prefix + "|" + msg # All commands start with "|".
    print(">> {}".format(out))
    await ws.send(out)

async def challenge(ws, user, mode="gen7ou"):
    """
    Challenge another player in specified format.
    Defaults to Gen 7 OU.
    """
    msg = "/challenge {}, {}".format(user, mode)
    await say(ws, msg)

async def makemove(ws, tag, move, turns):
    """
    """
    msg = "/choose move {}".format(move)
    await say(ws, msg, tag)

async def makeswitch(ws, tag, switch, turns):
    """
    """
    msg = "/choose switch {}".format(switch)
    await say(ws, msg, tag)

