import discord

import Secret

ozaidi_id = 145373751440179200
mary_id = 360530855741095936
tarek_id = 282296769767800835

client = discord.Client()


@client.event  # only runs when bot starts up, dont call it urself
async def on_ready():
    print("The bot is ready!")
    # await client.change_presence(game=discord.Game(name="Making a bot"))


# every single message in the discord server triggers this event
@client.event
async def on_message(message):
    if message.author == client.user:  # checking if author of message is the same as the bot
        return
    if message.content.lower() == "hello":  # if message says Hello, reply with hello back, mentioning user
        await message.channel.send("Hello " + message.author.mention)
    if message.content == "$joinedon":
        await message.channel.send(user_joined(message))
    if message.content.lower() == "men are":  # if message says men are, reply with trash can lolz
        emoji = await message.guild.fetch_emoji(658127740188229643)
        await message.channel.send(str(emoji))
    if message.content.lower() == "women are":  # if message says men are, reply with trash can lolz
        emoji = await message.guild.fetch_emoji(658112815294447643)
        await message.channel.send(str(emoji))
    if message.content == "$getaroom":
        ozaidi = message.guild.get_member(ozaidi_id)
        mary = message.guild.get_member(mary_id)
        tarek = message.guild.get_member(tarek_id)
        targetvoice = message.guild.get_channel(657804639009505319)
        await ozaidi.edit(voice_channel = targetvoice)
        await mary.edit(voice_channel = targetvoice)
        #await tarek.edit(voice_channel = targetvoice)
        await message.channel.send("here they go again")







def user_joined(message):
    return str(message.author.mention) + " joined on " + str(message.author.joined_at.strftime("%A, %B %d, %Y"))


client.run(Secret.bot_token)
