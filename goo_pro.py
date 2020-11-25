#importing packages

import discord
from discord.ext import commands
import pandas as pd

client = commands.Bot(command_prefix='!')

# Performing functions
@client.command(name='version')
async def version(context):

        Myembed = discord.Embed(title = "Current Version", description= "The bot is in version 1.0!", color=0x00ff05)
        Myembed.add_field(name = "Version Code:", value="v1.0.0",inline=False)
        Myembed.add_field(name="Date of release:",value="November 20, 2020", inline=False)
        Myembed.set_footer(text= "This is a sample footer")
        Myembed.set_author(name="Menexiam")

        await context.message.channel.send(embed=Myembed)


@client.command(name='kick', pass_context = True)
@commands.has_permissions(kick_member = True)
async def kick(context, member: discord.Member):
    await member.kick()
    await context.send('User '+ member.display_name + 'has been kicked')



@client.event
async def on_message(message):
    
    if message.content == 'what is the version of this bot' :
        general_channel = client.get_channel(#enter the Id of the channel)

        Myembed = discord.Embed(title = "Current Version", description= "The bot is in version 1.0!", color=0x00ff05)
        Myembed.add_field(name = "Version Code:", value="v1.0.0",inline=False)
        Myembed.add_field(name="Date of release:",value="November 20, 2020", inline=False)
        Myembed.set_footer(text= "This is a sample footer")
        Myembed.set_author(name="Mayank Maurya")

        await general_channel.send(embed=Myembed)

    if message.content == 'send a DM':
        await message.author.send('This is a dm have a good day fella!!')   

    if message.content == "Append":
        df = pd.read_csv('C:/Users/mayan/Desktop/bot/output.csv', index_col=0)
        df = df.append({"A": 'This is the message , i want to append.'}, ignore_index = True)
        df.to_csv('C:/Users/mayan/Desktop/bot/output.csv')

    await client.process_commands(message)

@client.event
async def on_ready():
    # the main stuff
    await client.change_presence(status=discord.Status.online,activity=discord.Game('Playing with the life of the developer ;)'))

    
#run the client on server(enter your own token)
client.run('TOKEN')
