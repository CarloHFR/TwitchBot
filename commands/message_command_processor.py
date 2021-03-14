# This module will display the message 

async def message_command_processor(ctx, data):

    # precisa validar se a pessoa tem permissão para executar o comando

    await ctx.channel.send(data["data"])