import random
from commands.interact import makemove, makeswitch

async def random_move(ws, tag, turns):
    choice = random.randint(1, 4)
    await makemove(ws, tag, choice, turns)

async def random_switch(ws, tag, turns):
    choice = random.randint(1, 6)
    await makeswitch(ws, tag, choice, turns)
