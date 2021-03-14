

async def message_command_processor(ctx, data):
    await ctx.channel.send(data["data"])