import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '**')
Clientdiscord = discord.Client()
command_prefix = '**

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='as a referee! (' + str(command_prefix) + 'help)'))
    print('Ready') 


@client.event
async def on_message(message):
    
    #Help Command
    if message.content == str(command_prefix) + 'Help':
        await client.send_message(message.channel,'''
Help - Gets you this screen
Prefix - Change prefix (prefix [new prefix])
StartDuel - Send duel request (StartDuel [invite recipient] [judge (leave blank for community vote)]
Forfeit - Forfeit a your current duel
''')

    #Prefix Command
    if str(command_prefix) + 'Prefix ' in message.content:
        await client.send_message(message.channel,"Discord Duel's prefix has been changed to " + message.content[len(str(command_prefix) + 'Prefix '):])
        command_prefix = message.content[len(str(command_prefix) + 'Prefix '):]
        
    #Forfeit Command
    if message.content == str(command_prefix) + 'Forfeit':
        await client.send_message(message.channel,'Are you sure? Type ' + str(command_prefix) + 'Accept to confirm')
    
    #Accept Command
    if message.content == str(command_prefix) + 'Accept':
        await client.send_message(message.channel, 'Current duel forfeited, the winnder is' + str(opponent) + 'by default!')
client.run('NDk2NzE3NDUwMzk0NzMwNTEy.DpWfMA.UrjW-P3IaEQOlyYZFeVCjNh11bw')
