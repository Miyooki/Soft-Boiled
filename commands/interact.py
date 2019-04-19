
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

async def challenge(ws, user, mode="gen7randombattle"):
    """
    Challenge another player in specified format.
    Defaults to Gen 7 Random Battle.
    """
    msg = "/challenge {}, {}".format(user, mode)
    print(msg)
    await say(ws, msg)

async def makemove(ws, tag, move):
    """
    """
    msg = "/choose move {}".format(move)
    await say(ws, msg, tag)

async def makeswitch(ws, tag, switch):
    """
    """
    msg = "/choose switch {}".format(switch)
    await say(ws, msg, tag)

async def leaveroom(ws, tag):
    """
    """
    msg = "/leave"
    await say(ws, msg, tag)
