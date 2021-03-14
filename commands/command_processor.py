# This module process the commands and redirect to specific function

import os
from tinydb import TinyDB, Query
from commands.add_command import add_command
from commands.message_command_processor import message_command_processor


native_commands = {
    "!addcmd" : add_command,
    "!delcmd" : "",
    "!enablecmd" : "",
    "!disablecmd" : "",
    "!chperm" : ""
}


async def command_process(ctx, command):

    command_database = os.getenv('CMD_DATABASE')
    
    # check if command is native
    if command.split(" ")[0] in native_commands.keys():
        await native_commands[command.split(" ")[0]](ctx, command)
        return 

    # if is a custom command, search for this data on commands.json and redirect to processor
    db = TinyDB(command_database)
    db_command = Query()

    cmd_name = command.split(" ")[0]
    cmd_name = command.split("!")[1]
    cmd_data = db.search(db_command.name == cmd_name)

    if cmd_data != []:
        cmd_data = cmd_data[0]

        if cmd_data["type"] == "msg":
            await message_command_processor(ctx, cmd_data)
