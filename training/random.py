import random
from commands.interact import makemove, makeswitch

async def random_move(ws, moves, tag):
    choice = random.randint(0, len(moves) - 1)
    await makemove(ws, tag, moves[choice])

async def random_switch(ws, team, tag):
    choice = random.randint(0, len(team) - 1)
    await makeswitch(ws, tag, team[choice])
