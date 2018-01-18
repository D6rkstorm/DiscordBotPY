import discord
import asyncio
import time
from random import randint

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
    await client.send_message(message.author, "```This is the TesterBot Discord Bot, Built for LasaCS Copyright Ethan Schaffer and Gabriel Manners 2018. For additional commands see below```"
                                              """1) Help: Lists basic commands and information about the bot. 
2) *For specific users* End: Forces the bot to crash by setting 2=1.
3) Dota: Gives a random hero from the current Dota 2 hero selection pool
4) Game: Takes up to two players for a rock paper scissors game. Currently in progress.
5) Echo: Repeats what was said, to an extent
6) PingMe: Pings the User
7) Purge: Can mention a user to clear their messages, or leave blank to clear my messages""")

async def end(message):
    trusted_users = ["Darkstorm#6481", "EthanSchaffer#7680"]
    if str(message.author) in trusted_users:
        await client.send_message(message.channel, "Goodnight")
        exit()
    else:
        await client.send_message(message.channel, "Insufficient permissions, contact D6rkstorm#6481 if you think this is in error")

async def dota(message):
    x = randint(0,114)
    mystr = """"Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe","Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster", "Bristleback", "Broodmother","Centaur Warrunner", "Chaos Knight", "Chen", "Clinkz", "Clockwerk", "Cyrstal Maiden","Dark Seer", "Dark Willow", "Dazzle", "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger","Earth Spriit", "Earthshaker", "Elder Titan", "Ember Spirit", "Enchantress", "Engima","Faceless Void","Gyrocopter","Huskar","Invoker", "Io","Jakiro", "Juggernaut","Keeper of the Light", "Kunkka","Legion Commander", "Leshrac", "Lich", "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan","Magnus", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling","Naga Siren", "Natures Prophet", "Necrophos", "Night Stalker", "Nyx Assassin","Ogre Magi", "Omniknight", "Oracle", "Outworld","Pangolier", "Phantom Assassin", "Phantom Lancer", "Pheonix", "Puck", "Pudge", "Pugna","Queen of Pain","Razor", "Riki", "Rubick","Sand King", "Shadow Demon", "Shadow Feind", "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark", "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit", "Sven","Techies", "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker", "Tiny", "Treat Protector", "Troll Warlod", "Tusk","Underlord", "Undying", "Ursa","Vengeful Spirit", "Venomancer", "Viper", "Visage","Warlock", "Weaver", "Windragner", "Winter Wyvern", "Witch Doctor", "Wraith King", "Zeus """
    mylist = mystr.split(",")
    await client.send_message(message.channel, mylist[x][2:-1])

async def game(message):
    await client.send_message(message.channel, "This doesnt work right now, even though it looks like it will, SORRY!")
    messageStr = message.content[len(commandStr):]
    messageList = messageStr.split(" ")
    player1 = False
    player2 = False

    if len(messageList) != 3:
        await client.send_message(message.channel, "Please ping two players to start this game")
    else:
        await client.send_message(message.channel, "You have started the game with the players " + messageList[1] + " and " + messageList[2])
        time.sleep(.01)
        await client.send_message(message.channel, "Please reply 'Ready' to begin")

        msg = await client.wait_for_message(timeout=7, content="Ready")
        print(msg)
        if msg.author == messageList[1]:
            print("help")
            player1 = True
        elif msg.author == messageList[2]:
            player2 = True
        msg = await client.wait_for_message(timeout=7, content="Ready")
        if msg.author == messageList[1]:
            player1 = True
        elif msg.author == messageList[2]:
            player2 = True




        if player1 == True and player2 == True:
            await client.send_message(message.channel, "Both players have said Ready, time to start")
            time.sleep(.01)
            await client.send_message(message.channel, "On the count of three, say rock, paper, or scissors")
            time.sleep(1)
            await client.send_message(message.channel, "1")
            time.sleep(1)
            await client.send_message(message.channel, "2")
            time.sleep(1)
            await client.send_message(message.channel, "3!!")
            time.sleep(.01)
        else:
            await client.send_message(message.channel, "Players didn't ready up in time, so sad :cry:")

async def quote(message):
    x = randint(0, 47)
    quoteStr = '"Yousa thinking yousa people ganna die?”,“I don’t care what universe you’re from, that’s got to hurt!”,“Love won’t save you, Padme. Only my new powers can do that.”,“…Don’t try it, Anakin. I have the high ground!”,“There’s always a bigger fish.”,“I’m haunted by the kiss that you should never have given me.”,“Are you an angel?”,“I don’t like sand. It’s coarse and rough and irritating and it gets everywhere.”,“Ye gods, whatta meesa sayin’?”, “I sense Count Dooku.”,“Ani? My goodness, you’ve grown!”,“How wude!”,“I can’t take Dooku alone! I need you!”,“I’ve been wondering… what are midi-chlorians?”,“Chesco, Sebulba. Chipoka oomen geesa. Me teesa radical fbombati chop chawa.”,“I have the POWER! UNLIMITED… POWER!”,“Droidekas!”,“Uh! So uncivilized.”,“Now this is pod racing!”,“So this is how liberty dies… with thunderous applause.”,“…It is only natural. He cut off your arm, and you wanted revenge.”,“Always two there are, no more, no less.”,“Mom, you said that the biggest problem in the universe is no one helps each other.”,“He owes me what you’d call a ‘life-debt.’ Your gods demand that his life belongs to me.”,“From my point of view, the Jedi are evil!”,“I thought we had decided not to fall in love. That we’d be forced to live a lie and that it would destroy our lives.”,“A vengence, you say?”,“Now that I’m with you again, I’m in agony. My heart is beating, hoping that that kiss will not become a scar.”,“No loose wire jokes.”,“Your mother had gone out early, like she always did, to pick mushrooms that grow on the vaporators.”,“For reasons we can’t explain, we are losing her.”,“…Well, then you really are lost!”,“He said… you killed younglings!”,“What if the democracy we thought we were serving no longer exists, and the Republic has become the very evil we have been fighting to destroy?”,“I have waited a long time for this moment, my little green friend.”,“…I’ll try spinning. That’s a good trick. Whoa-ah!”,“Train yourself to let go… of everything you fear to lose.”,“There was no father. I carried him, I gave birth, I raised him. I can’t explain what happened.”,“You were banished because you were clumsy?”,“You are in my very soul, tormenting me…”,“…We used to come here for school retreat. We would swim to that island every day. I love the water. We used to lie out on the sand and let the sun dry us and try to guess the names of the birds singing.”,“At an end your rule is, and not short enough was it.”,“Ray shields!”,“Just being around her again is… intoxicating.”,“Your new Empire?”,“Symbionts?”,“They live inside me?”,“I don’t understand.”,“Your presence is soothing.”,“…We live in a real world, come back to it. You’re studying to become a Jedi, I’m… I’m a senator.”'
    quoteList = quoteStr.split('”,“')
    await client.send_message(message.channel, quoteList[x])

async def echo(message):
    if ("`" not in message.content[len(commandStr) + 4:]) and ("@" not in message.content[len(commandStr) + 4:]):
        await client.send_message(message.channel, message.content[len(commandStr) + 4:])
    else:
        await client.send_message(message.channel, "Please try not to loop me or ping people, its just annoying")

async def pingme(message):
    await client.send_message(message.channel, message.author.mention)

async def purge(message):
    if message.content[len(commandStr):].lower() == "purge":
        def is_me(message):
            return message.author == client.user

        deleted = await client.purge_from(message.channel, limit=1000, check=is_me)
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))
    else:
        def is_else(message):
            return message.content[len(commandStr) + 5:]
        deleted = await client.purge_from(message.channel, limit=1000, check=is_else)
        await client.send_message(message.channel, 'Deleted {} message(s)'.format(len(deleted)))

@client.event
async def on_message(message):
    if message.content[0:len(commandStr)] == commandStr:
        command = message.content[len(commandStr):].lower()
        if command == "help":
            await help(message)
        if command == "end":
            await end(message)
        if command == "dota":
            await dota(message)
        if "echo" in command[0:4]:
            await echo(message)
        if command == "quote":
            await quote(message)
        if "pingme" in command[0:6]:
            await pingme(message)
        if "purge" in command[0:5]:
            await purge(message)


with open('token_file.txt') as token_file:
    for line in token_file:
        login_token = line

client.run(login_token)
