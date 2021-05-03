#bot.py

# INFORMATIONS ----------------------------------- #
CREATOR = 'Hecos#4117'
CONTACT = 'thehecos@gmail.com'
PROJECT = 'Lithium Project'
VERSION = 'v1.0.0.0'

# LIBRARIES -------------------------------------- #
import os, random, discord, json, time, shutil, requests

from discord.ext import commands
from discord.ext.commands import has_permissions

# TOKEN ------------------------------------------ #
TOKEN = 'TOKEN'

# VARIABLES -------------------------------------- #
LIMITMAX = 134217726

# PREFIXES --------------------------------------- #
def get_prefix(bot, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(message.guild.id)]

    except (AttributeError):
        return '&'
    
# START ------------------------------------------ #
bot = commands.Bot(command_prefix=get_prefix)

bot.remove_command('help')

@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="&help"))
    now = time.localtime(time.time())
    print('Bot is ready !', time.strftime("\n%y/%m/%d %H:%M", now))
    print(VERSION, '\n')

# DETECTION MOT DANS MESSAGE --------------------- #
@bot.event
async def on_message(message):
    if str(message.content.lower()) == '<@!797164290490368051>':
        try:
            await lithium_help(message)
        except AttributeError:
            print (f"#HELP made by USER:{message.author} with MENTION")
        
    await bot.process_commands(message)

# PREFIXES --------------------------------------- #
@bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '&'
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop[str(guild.id)]
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.command(name='prefix')
@has_permissions(administrator=True)
async def changeprefix(ctx, prefix=str("none")):
    if prefix == "none":
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        isprefix = prefixes[str(ctx.guild.id)]
        await ctx.send(f'Préfixe actuel : **{isprefix}**')
        
    else:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'Nouveau préfixe : **{prefix}**')

# AFFICHAGE INFOS -------------------------------- #
@bot.command(name='lithium', aliases=['infos', 'info'])
async def dispinfo(ctx, lg=str('en')):
    if lg == 'fr':
        embedinfos = discord.Embed(title='Lithium Bot', color=int("2eaf8e",16))
        embedinfos.add_field(name="Nom du projet :", value=f"{PROJECT}", inline=True)
        embedinfos.add_field(name="᲼", value=f"᲼", inline=True)
        embedinfos.add_field(name="Version :", value=f"{VERSION}", inline=True)
        embedinfos.add_field(name="Créateur :", value=f"{CREATOR}", inline=True)
        embedinfos.add_field(name="᲼", value=f"᲼", inline=True)
        embedinfos.add_field(name="Contact :", value=f"{CONTACT}", inline=True)
    else:
        embedinfos = discord.Embed(title='Lithium Bot', color=int("2eaf8e",16))
        embedinfos.add_field(name="Project name :", value=f"{PROJECT}", inline=True)
        embedinfos.add_field(name="᲼", value=f"᲼", inline=True)
        embedinfos.add_field(name="Version :", value=f"{VERSION}", inline=True)
        embedinfos.add_field(name="Creator :", value=f"{CREATOR}", inline=True)
        embedinfos.add_field(name="᲼", value=f"᲼", inline=True)
        embedinfos.add_field(name="Contact :", value=f"{CONTACT}", inline=True)
    await ctx.send(embed=embedinfos)
    print (f"#INFOS made by USER:{ctx.message.author}")

# CLEAR ------------------------------------------ #
@bot.command(name='clear')
@has_permissions(administrator=True)
async def clearchat(ctx, amount=int(0)):
    if amount == 0:
        return
    else:
        await ctx.channel.purge(limit=amount+1)
    print (f"#CLEAR made by USER:{ctx.message.author} with AMOUNT:'{amount}'")

# HELP ------------------------------------------- #
@bot.command(name='help', aliases=['h'])
async def lithium_help(ctx, cmd=str('&')):
    if cmd == '&' or cmd == 'here' or cmd == 'public':
        embedhelp = discord.Embed(color=int("2eaf8e",16))
        embedhelp.set_author(name='LISTE DES COMMANDES DE LITHIUM :')
        embedhelp.add_field(name='avatar', value="Allows you to obtain the profile photo of a user.", inline=False)
        embedhelp.add_field(name='cat', value="Send a picture of a cute cat!", inline=False)
        embedhelp.add_field(name='clear', value="Delete the X previous messages.", inline=False)
        embedhelp.add_field(name='dog', value="Send a picture of a cute dog!", inline=False)
        embedhelp.add_field(name='help', value="Displays this message.", inline=False)
        embedhelp.add_field(name='infos', value="Displays various information about the bot.", inline=False)
        embedhelp.add_field(name='mix', value="Mix two colors.", inline=False)
        embedhelp.add_field(name='pfc', value="ShiFuMi !", inline=False)
        embedhelp.add_field(name='ping', value="Pong !", inline=False)
        embedhelp.add_field(name='poll', value="Allows you to create a vote/poll quickly.", inline=False)
        embedhelp.add_field(name='prefix', value="Allows to know and change the prefix of the bot.")
        embedhelp.add_field(name='roll', value="Simulates a roll of the dice.", inline=False)
        embedhelp.add_field(name='r6challenge', value="Generates a random Rainbow Six challenge.", inline=False)
        embedhelp.add_field(name='r6team', value="Generates a random Rainbow Six team.", inline=False)
        embedhelp.add_field(name='skcreate', value="Allows you to create a word list for skribbl.io.", inline=False)
        if cmd == 'here' or cmd == 'public':
            await ctx.send(embed=embedhelp)
        else:
            await ctx.author.send(embed=embedhelp)

    else:
        if cmd == 'mix':
            embedhelp = discord.Embed(description='mix <hex_color_1> <hex_color_2>')
        if cmd == 'pfc' or cmd =='rps':
            embedhelp = discord.Embed(description='rps <rock, paper or scissors>')
        if cmd == 'ping':
            embedhelp = discord.Embed(description='ping [d (default) | a (advanced)]')
        if cmd == 'r6team':
            embedhelp = discord.Embed(description='r6team <attackers or defenders> [number of players]')
        if cmd == 'roll':
            embedhelp = discord.Embed(description='roll [number of sides]\nroll <min> <max>')
        if cmd == 'help':
            embedhelp = discord.Embed(description='help [command]')
        if cmd == 'prefix':
            embedhelp = discord.Embed(description='prefix [new prefix]')
        if cmd == 'clear':
            embedhelp = discord.Embed(description='clear <number of messages>')
        if cmd == 'r6challenge':
            embedhelp = discord.Embed(description='r6challenge')
        if cmd == 'poll':
            embedhelp = discord.Embed(description='poll <question>')
        if cmd == 'skcreate' or cmd == 'skribbl':
            embedhelp = discord.Embed(description='skcreate')
        if cmd == 'avatar' or cmd == 'pp':
            embedhelp = discord.Embed(description='avatar [user]')
        if cmd == 'dog':
            embedhelp = discord.Embed(description='dog')
        if cmd == 'cat':
            embedhelp = discord.Embed(description='cat')
        if cmd == 'infos' or cmd == 'info':
            embedhelp = discord.Embed(description='infos [language]')
        await ctx.send(embed=embedhelp)

    print (f"#HELP made by USER:{ctx.message.author} with CMD:'{cmd}'")

# LANCER DE DE ----------------------------------- #
@bot.command(name='roll', aliases=['r'])
async def roll(ctx, mini=int(100), maxi=int(LIMITMAX)):
    if maxi == LIMITMAX:
        maxi = mini
        mini = 1
    if maxi >= LIMITMAX - 1 or mini > maxi:
        await ctx.send("So actually, no.")
        return
    
    dice = random.randint(mini, maxi)
    nb_faces = (maxi - mini) + 1

    embeddice=discord.Embed(title=f':game_die: {dice}', description=f'Die with {nb_faces} faces')
    embeddice.set_footer(text = f'{ctx.message.author}', icon_url = f'{ctx.message.author.avatar_url}')
    
    await ctx.send(embed=embeddice)
    print (f"#ROLL made by USER:{ctx.message.author} with MINI:'{mini}' and MAXI:'{maxi}'")

# PING ------------------------------------------- #
@bot.command(name='ping')
async def ping(ctx, mode=str('&')):
    latency=round(bot.latency*1000)
    
    if mode == '&':
        await ctx.channel.send("Pong !")

    elif mode == 'a':
        if latency < 180:
            embedping = discord.Embed(color=int("20a84e",16),title="Pong !", description = str(latency)+'ms')
        if latency > 340:
            embedping = discord.Embed(color=int("e94242",16),title="Pong !", description = str(latency)+'ms')
        if latency >= 180 and latency <340:
            embedping = discord.Embed(color=int("da861b",16),title="Pong !", description = str(latency)+'ms')
        await ctx.channel.send(embed=embedping)

    else:
        return

    print (f"#PING made by USER:{ctx.message.author} with PING:'{latency}'")

# PONG ------------------------------------------- #
@bot.command(name='pong')
async def pong(ctx):
    await ctx.channel.send("Ping !")

# VOTE ------------------------------------------- #
@bot.command(name='poll')
async def create_poll(ctx,*,msg=str('&')):

    if msg == '&':
        await lithium_help(ctx, 'poll')
        return
    
    channel=ctx.channel
    embedpoll=discord.Embed(title = f'{msg}', description = 'Vote with :white_check_mark: or :negative_squared_cross_mark:!')
    message_ = await channel.send(embed=embedpoll)
    await message_.add_reaction('✅')
    await message_.add_reaction('❎')
    await ctx.message.delete()
    print (f"#POLL made by USER:{ctx.message.author} with MESSAGE:'{msg}'")

# GENERE UNE TEAM R6 ----------------------------- #
@bot.command(name='r6team', aliases=['r6t','r6squad','r6s'])
async def squad(ctx, mode = str('&'), taille = int(5)):

    if mode == '&':
        await lithium_help(ctx, 'r6team')
        return
    
    R6ATQ = ["Flores", "Zero (EOR)", "Ace (Nighthaven)", "Iana (ASE)", "Kali (Nighthaven)", "Amaru (APCA)", "Nokk (Jaeger Corps)", "Gridlock (SASR)", "Nomad (GIGR)",
             "Maverick (ITUGS)", "Lion (NRBC)", "Finka (NRBC)", "Dokkaebi (707th SMB)", "Zofia (GROM)", "Ying (SDU)", "Jackal (GEO)", "Hibana (SAT)", "Capitao (BOPE)",
             "Blackbeard (NAVY SEAL)", "Buck (JTF2)", "Sledge (SAS)", "Thatcher (SAS)", "Ash (FBI SWAT)", "Thermite (FBI SWAT)", "Montagne (GIGN)", "Twitch (GIGN)",
             "Blitz (GSG9)", "Iq (GSG9)", "Fuze (Spetsnaz)", "Glaz (Spetznaz)"]
    R6DEF = ["Aruni (Nighthaven)", "Melusi (ITF)", "Oryx", "Wamai (Nighthaven)", "Goyo (Mexican Special Forces)", "Warden (US Secret Service)", "Mozzie (SASR)",
             "Kaid (GIGR)", "Clash (ITUGS)", "Maestro (GIS)", "Alibi (GIS)", "Vigil (707th SMB)", "Ela (GROM)", "Lesion (SDU)", "Mira (GEO)", "Echo (SAT)",
             "Caveira (BOPE)", "Valkyrie (NAVY SEAL)", "Frost (JTF2)", "Mute (SAS)", "Smoke (SAS)", "Castle (FBI SWAT)", "Pulse (FBI SWAT)", "Doc (GIGN)", "Rook (GIGN)",
             "Jager (GSG9)", "Bandit (GSG9)", "Tachanka (Spetsnaz)", "Kapkan (Spetsnaz)"]

    if taille > 5:
        taille = 5
    
    result = "__**Squad generated:**__ "
    
    if mode.lower() == "atk" or mode.lower() == "attackers":
        random.shuffle(R6ATQ)
        for i in range(taille):
          result += R6ATQ[i] + ", "
                
    if mode.lower() == "def" or mode.lower() == "defenders":
        random.shuffle(R6DEF)
        for i in range(taille):
          result += R6DEF[i] + ", "
            
    await ctx.send(result[0:-2])
    print (f"#R6TEAM made by USER:{ctx.message.author} with MODE:'{mode}' and TAILLE:'{taille}'")

# GENERE UN DEFI R6 ------------------------------ #
@bot.command(name='r6challenge', aliases=['r6c','r6defi','r6défi','r6d'])
async def r6defi(ctx):
    R6_DEFI = ["Only shotguns are allowed.",
               "It is forbidden to go to the objective room (except in case of emergency).",
               "Switch your hands between the mouse and the keyboard.",
               "It is forbidden to talk to each other (voice and written chat prohibited).",
               "It is forbidden to pass through anything but doors.",
               "Use gloves, socks, mittens, or other equivalents to play.",
               "Only the secondary weapon is allowed.",
               "You must destroy all the doors and windows you see.",
               "No one is allowed to enter or leave the building other than through windows.",
               "It is forbidden to use firearms during the first minute of the round.",
               "Mute the game, only voice chat is allowed.",
               "The use of drones/cameras is prohibited.",
               "Follow a wall throughout the game. Wherever that wall goes you will go.",
               "It is forbidden to destroy drones/cameras.",
               "When there is only one survivor left, his dead teammates must make as much noise as possible.",
               "Only one person is allowed to move until the end of the preparation phase.",
               "The weapons you will use must be equipped with silencers.",
               "You should constantly teabag during the round."]
    
    random.shuffle(R6_DEFI)
    result = "__Challenge :__ " + R6_DEFI[1]
    await ctx.send(result)
    print (f"#R6CHALLENGE made by USER:{ctx.message.author}")

# PIERRE FEUILLE CISEAUX ------------------------- #
@bot.command(name='rps', aliases=['sfm','shifumi',])
async def pfc(ctx, pierre_feuille_ou_ciseaux: str):
    pfcanswer = ['ROCK','PAPER','SCISSORS'] 
    pfcbot = pfcanswer[random.randint(0,2)]
    if pierre_feuille_ou_ciseaux.upper() in pfcanswer:
        if pfcbot.lower() == 'rock':
            if pierre_feuille_ou_ciseaux.lower() == 'paper':
                await ctx.send(f"**WELL PLAYED!** *I said {pfcbot} !*")
            else:
                await ctx.send(f"**YOU LOST!** *I said {pfcbot} !*")
        if pfcbot.lower() == 'paper':
            if pierre_feuille_ou_ciseaux.lower() == 'scissors':
                await ctx.send(f"**WELL PLAYED!** *I said {pfcbot} !*")
            else:
                await ctx.send(f"**YOU LOST!** *I said {pfcbot} !*")
        if pfcbot.lower() == 'scissors':
            if pierre_feuille_ou_ciseaux.lower() == 'rock':
                await ctx.send(f"**WELL PLAYED!** *I said {pfcbot} !*")
            else:
                await ctx.send(f"**YOU LOST!** *I said {pfcbot} !*")
    elif pierre_feuille_ou_ciseaux.lower() == 'well':
        await ctx.send("...")
    else:
        await ctx.send("So actually, no.")
    print (f"#PFC made by USER:{ctx.message.author} with PFC:'{pierre_feuille_ou_ciseaux}'")

# MELANGE DEUX COULEURS EN HEX ------------------- #
@bot.command(name='mix')
async def mixcolor(ctx, hex_color_1 = str('&'), hex_color_2 = str('&')):
    if hex_color_1 == '&' or hex_color_2 == '&':
        await lithium_help(ctx, 'mix')
        return

    if len(hex_color_1) != 7 and hex_color_1[0] != '#':
        hex_color_1 = '#' + hex_color_1
    if len(hex_color_2) != 7 and hex_color_2[0] != '#':
        hex_color_2 = '#' + hex_color_2
    if (len(hex_color_1) != 7 and hex_color_1[0] == '#') or (len(hex_color_2) != 7 and hex_color_2[0] == '#'):
        await ctx.send('Alors, non.')
        return
        
    r1, r2 = int(hex_color_1[1:3], 16), int(hex_color_2[1:3], 16)
    g1, g2 = int(hex_color_1[3:5], 16), int(hex_color_2[3:5], 16)
    b1, b2 = int(hex_color_1[5:7], 16), int(hex_color_2[5:7], 16)

    rf = round((r1+r2)/2)
    gf = round((g1+g2)/2)
    bf = round((b1+b2)/2)

    rf = str(hex(rf)[2:])
    gf = str(hex(gf)[2:])
    bf = str(hex(bf)[2:])

    if len(rf)==1:
        rf='0'+rf
    if len(gf)==1:
        gf='0'+gf
    if len(bf)==1:
        bf='0'+bf
        
    mixed='#'+rf+gf+bf

    embedmixed=discord.Embed(title=mixed, color=int(mixed[1:], 16))

    await ctx.send(embed=embedmixed)
    print (f"#MIX made by USER:{ctx.message.author} with HEX1:'{hex_color_1}' and HEX2:'{hex_color_2}'")

# AVATAR ----------------------------------------- #
@bot.command(name='avatar', aliases=['pp'])
async def get_avatar(ctx, member:discord.Member = str('0#0'), size = 512):
    if member == '0#0':
        member = ctx.message.author
    if size < 32:
        size = 32
    elif size > 4096:
        size = 4096

    ppurl = str(member.avatar_url)
    
    if ppurl[-15:-10] == '.webp':
        ppurl = str(member.avatar_url)[:-15] + f'.png?size={size}'
    elif ppurl[-15:-11] == '.gif':
        ppurl = str(member.avatar_url)[:-14] + f'.gif?size={size}'
        
    embedavatar=discord.Embed(title=f'{member}')
    embedavatar.set_image(url=f'{ppurl}')
    
    await ctx.send(embed=embedavatar)
    print (f"#AVATAR made by USER:{ctx.message.author} with MEMBER:'{member}'")

# DOG -------------------------------------------- #
@bot.command(name='dog', aliases = ['woof', 'chien', 'wouf'])
async def random_dog(ctx):
    requete = requests.get('https://dog.ceo/api/breeds/image/random')
    page = requete.content
    dogurl = str(page)[14:-22].replace('\\', '')
    
    embeddog=discord.Embed(title='Woof!')
    embeddog.set_image(url=f'{dogurl}')
    
    await ctx.send(embed=embeddog)
    print (f"#DOG made by USER:{ctx.message.author}")

# CAT -------------------------------------------- #
@bot.command(name='cat', aliases = ['miaou', 'meow', 'chat'])
async def random_cat(ctx):
    requete = requests.get('https://api.thecatapi.com/v1/images/search')
    cats = json.loads(requete.content)
    for url in cats:
        caturl = url['url']
    
    embedcat=discord.Embed(title='Meow!')
    embedcat.set_image(url=f'{caturl}')
    
    await ctx.send(embed=embedcat)
    print (f"#CAT made by USER:{ctx.message.author}")

# SKRIBBL.IO ------------------------------------- #
@bot.command(name='skcreate', aliases=['skribbl'])
async def skribbl_create(ctx):

#CLEAR
    now = time.localtime(time.time())
    day = time.asctime(now)[:3]
        
    if day in ["Tue", "Wed", "Thu"]:
        shutil.rmtree('skribbl/1')
        os.mkdir('skribbl/1')
        with open(f'skribbl/idlist-1.txt', 'w') as file:
            file.write('')
        
    if day in ["Sat", "Sun"]:
        shutil.rmtree('skribbl/2')
        os.mkdir('skribbl/2')
        with open(f'skribbl/idlist-2.txt', 'w') as file:
            file.write('')

#ID ATTRIBUTION
    idsk = 0
    
    if day in ["Mon", "Tue", "Wed", "Thu"]:
        with open('skribbl/idlist-2.txt') as file:
            idlist = file.read()
        while str(idsk) in idlist:
            idsk += 1
        idlist += '/' + str(idsk)
        with open('skribbl/idlist-2.txt', 'w') as file:
            file.write(idlist)
        dayid = 2
                
    elif day in ["Fri", "Sat", "Sun"]:
        with open('skribbl/idlist-1.txt') as file:
            idlist = file.read()
        while str(idsk) in idlist:
            idsk += 1
        idlist += '/' + str(idsk)
        with open('skribbl/idlist-1.txt', 'w') as file:
            file.write(idlist)
        dayid = 1

    else:
        return

    while len(str(idsk)) != 5:
        idsk = '0' + str(idsk)
    gameid = str(dayid) + str(idsk)
    with open(f'skribbl/{dayid}/{gameid}.txt', 'w') as file:
        file.write('')

    embedsk = discord.Embed(title = f'ID : {gameid}', description=f"Use 'sk {gameid} <word(s)>' to add words to your list. Use 'skprint {gameid}' to get the words from the list.")
    await ctx.send(embed=embedsk)

#WORDS
@bot.command(name='sk')
async def skribbl(ctx, gameid:str, *, word:str):
    dayid = gameid[:1]
            
    if os.path.isfile(f'skribbl/{dayid}/{gameid}.txt'):
        with open(f'skribbl/{dayid}/{gameid}.txt', 'a') as file:
            file.write(f', {word}')
        await ctx.send("Got it!")

    else:
        await ctx.send("ERROR: This ID is not assigned.")

#RETURN
@bot.command(name='skprint')
async def skribbl_print(ctx, gameid:str):
    dayid = gameid[:1]
    if os.path.isfile(f'skribbl/{dayid}/{gameid}.txt'):
        with open(f'skribbl/{dayid}/{gameid}.txt') as file:
            await ctx.author.send(f'__List of words:__ ||{file.read()[2:]}||')
            
    else:
        await ctx.send("ERROR: This ID is not assigned.")

bot.run(TOKEN)
