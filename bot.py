import discord
import asyncio
import time

client = discord.Client()
commandStr = "`"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def help(message):

    await client.send_message(message.channel, "```You have executed the help command, see direct messages for more detail```")
    time.sleep(.1)
    await client.send_message(message.author, "This is the help message you requested")

@client.event
async def on_message(message):
    if(message.content[0:len(commandStr)] == commandStr):
        command = message.content[len(commandStr):]
        if command == "help":
            await help(message)

        trusted_users = ["Darkstorm#6481", "EthanSchaffer#7680"]
        if command == "please kill yourself":
            if str(message.author) in trusted_users:
                await client.send_message(message.channel, "Okay :cry:")
                exit()
            else:
                await client.send_message(message.channel, "Fuck off *THOT*")
with open('token_file.txt') as token_file:
    for line in token_file:
        login_token = line

client.run(login_token)
