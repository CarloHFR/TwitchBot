import os
from dotenv import load_dotenv
from twitchio.ext import commands
from commands.command_processor import command_process


def main():

    load_dotenv()

    irc_token = os.getenv('TMI_TOKEN')
    client_id = os.getenv('CLIENT_ID')
    bot_nick = os.getenv('BOT_NICK')
    prefix = os.getenv('BOT_PREFIX')
    channel = os.getenv('CHANNEL')


    bot = commands.Bot(
        irc_token = irc_token,
        client_id = client_id,
        nick = bot_nick,
        prefix = prefix,
        initial_channels = [channel]
    )


    @bot.event
    async def event_ready():
        print(f"bot is online!")
        ws = bot._ws  # this is only needed to send messages within event_ready
        await ws.send_privmsg(channel, f"/me online!")


    @bot.event
    async def event_message(ctx):
        # make sure the bot ignores itself
        if ctx.author.name.lower() == bot_nick.lower():
            return

        if ctx.content.lower().startswith(prefix):
            await command_process(ctx, ctx.content.lower())
        

    # Starting the bot
    bot.run()


if __name__ == "__main__":
    main()
