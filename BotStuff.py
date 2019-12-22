import discord
import Secret
import OtherStuff

client = discord.Client()


@client.event #only runs when bot starts up, dont call it urself
async def on_ready():
    print("The bot is ready!")
    # await client.change_presence(game=discord.Game(name="Making a bot"))


#every single message in the discord server triggers this event
@client.event
async def on_message(message):
    if message.author == client.user: #checking if author of message is the same as the bot
        return
    if message.content.lower() == "hello": #if message says Hello, reply with hello back, mentioning user
        await message.channel.send("Hello "+message.author.mention)
    if message.content == "$joinedon":
        await message.channel.send(user_joined(message))

def user_joined(message):
    return str(message.author.mention) +" joined on "+str(message.author.joined_at.strftime("%A, %B %d, %Y"))

client.run(Secret.bot_token)
