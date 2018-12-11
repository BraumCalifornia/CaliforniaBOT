import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import os
from discord import Game
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()



@client.event
async def on_ready():
    await client.change_presence(game=Game(name='CaliforniaRP', type = 3))
    print('Ready, Freddy')

@client.event
async def on_message(message):
    if message.content == 'ip':
        await client.send_message(message.channel,'**IP serwera CaliforniaRP to 91.134.188.139**')
    if message.content == 'IP':
        await client.send_message(message.channel,'**IP serwera CaliforniaRP to 91.134.188.139**')
    if ('https://discord.gg/') in message.content:        await client.delete_message(message)
    if message.content.startswith('$random'):
        randomlist = ["hello","goodbye"]
        await client.send_message(message.channel,(random.choice(randomlist)))
@client.event
async def on_member_join(member):
        role = discord.utils.get(member.server.roles, name='test')
        await client.add_roles(member, role)
@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Witamy na CaliforniRP! ')

    print('Sent message to ' + member.name)
@client.event
async def on_member_join(member):
    print('Weclome ' + member.name)
    await client.send_message(discord_Channel01, 'Welcome!')
@client.event
async def on_message(message):
    if message.content == 'Bot':
        await client.send_message(message.channel, '**Jaki bot?**')
    if message.content == 'bot':
        await client.send_message(message.channel, '**Jaki bot?**')

client.run('NTE4NDQwMzQ5ODYyMDY4MjI3.DuQzBg.zyxQRiHlYgQsQHC3tlLzBI-GkGE')
