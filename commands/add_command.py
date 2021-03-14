# This module adds a custom commands

import os
from tinydb import TinyDB, Query


async def add_command(ctx, command):

    command_types = os.getenv('CMD_TYPES')
    permissions = os.getenv('CMD_PERMISSIONS')
    command_database = os.getenv('CMD_DATABASE')
    

    # check if the user has permission
    if not ctx.author.is_mod:
        return

    # check if command has all fields (cmd type perm name data)
    if len(command.split(" ")) < 5:
        return

    cmd_type = command.split(" ")[1]
    cmd_perm = command.split(" ")[2]
    cmd_name = command.split(" ")[3]
    cmd_data = command.split(" ")[4:]
    cmd_data = " ".join(cmd_data)

    if not cmd_type in command_types:
        return

    if not cmd_perm in permissions:
        return

    # check if command already exists
    db = TinyDB(command_database)

    command = Query()
    if db.search(command.name == cmd_name):
        await ctx.channel.send(f"@{ctx.author.name} comando já existe!")
        return 

    # save the command
    new_cmd = {
        "name" : cmd_name,
        "type" : cmd_type,
        "perm" : cmd_perm,
        "data" : cmd_data
    }

    db.insert(new_cmd)

    # return response for user
    await ctx.channel.send(f"@{ctx.author.name} comando adicionado!")
