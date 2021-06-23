import os
import random
import discord
import praw
from discord import user
from discord.ext import commands
import secrets
from os import path
from importlib.resources import path
import sys
sys.path.append('C:\\Users\\Soham Dhar\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\praw')

client = commands.Bot(command_prefix='.')

reddit = praw.Reddit(client_id="x",
                     client_secret="x", user_agent="x")


@client.event
async def on_ready():
    print('Bot is ready')


@client.command(aliases=['commands', 'Help', 'cmds'])
async def coms(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed.add_field(name="Command 1:", value="spam")
    embed.add_field(name="Command 2:", value="8ball")
    embed.add_field(name="Command 3:", value="rickroll")
    embed.add_field(name="Command 4:", value="pog")
    embed.add_field(name="Command 5:", value="clear")
    embed.add_field(name="Command 6:", value="f")
    embed.add_field(name="Command 7:", value="hmm")
    embed.add_field(name="Command 8:", value="be_humble")
    embed.add_field(name="Command 9:", value="ping")
    embed.add_field(name="Command 10:", value="jojo")
    embed.add_field(name="Command 11:", value="nani")
    embed.add_field(name="Command 12:", value="bowling")
    embed.add_field(name="Command 13:", value="meme")
    embed.add_field(name="Command 14:", value="hack")
    await ctx.send(embed=embed)


@client.command()
async def plswork(ctx):
    await ctx.send('Yes!')

@client.command()
async def plsdontwork(ctx):
    await ctx.send('No lol')
    
@client.command(aliases=['say'])
async def spam(ctx, *, word):
        i = 1
        if "@everyone" in word:
            await ctx.send(f"No U")
        if "{user}" in word:
            await ctx.send(f"No U")
        else:
            while(i <= 5):
                await ctx.send(word)
                i = i + 1

@client.command(aliases=['8ball', '8Ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.', 'Reply hazy, try again.', ' Ask again later.','Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', ' My sources say no.', 'Outlook not so good.','Very doubtful.']
    await ctx.send(random.choice(responses))

@client.command(aliases=['rick', 'rickroll'])
async def Rick(ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        await ctx.send(embed=embed)

@client.command()
async def pog(ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(
            url='https://qph.fs.quoracdn.net/main-qimg-4623467bd63c285526b042d85044803b')
        await ctx.send(embed=embed)

@client.command()
async def clear(ctx, amt=5):
        int(amt)
        await ctx.channel.purge(limit=amt)

@client.command()
async def f(ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(
            url='https://i2.kym-cdn.com/photos/images/facebook/000/858/776/f2e.jpg_large')
        await ctx.send(embed=embed)

@client.command()
async def hmm(ctx):
        embed = discord.Embed(color=discord.Color.red())
        responses = ['https://i.ytimg.com/vi/S6i9pMByi8E/maxresdefault.jpg',
                     'https://i.ytimg.com/vi/3CvMALbPoYE/maxresdefault.jpg']
        response = random.choice(responses)
        embed.set_image(url=response)
        await ctx.send(embed=embed)


@client.command(aliases=['be humble', 'sit down'])
async def be_humble(ctx):
    embed = discord.Embed(color=discord.Color.red())
    embed = discord.Embed(color=discord.Color.red())
    embed.set_image(url='https://www.youtube.com/watch?v=tvTRZJ-4EyI')
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send('Latency: {0}s'.format(round(client.latency, 1)))


@client.command()
async def jojo(ctx):
        embed = discord.Embed(color=discord.Color.red())
        responses = ['https://i.redd.it/lbw5nfg737431.jpg',
                     'https://i.ytimg.com/vi/S99uVzt4HHQ/maxresdefault.jpg', 'https://i.redd.it/lbw5nfg737431.jpg']
        response = random.choice(responses)
        embed.set_image(url=response)
        await ctx.send(embed=embed)

@client.command()
async def nani(ctx):
        embed = discord.Embed(color=discord.Color.red())
        responses = ['https://i.ytimg.com/vi/L_OuM9cu-G8/maxresdefault.jpg', 'https://i.ytimg.com/vi/vxKBHX9Datw/maxresdefault.jpg',
                     'https://picon.ngfiles.com/713000/flash_713153_largest_crop.png?f1529947246']
        response = random.choice(responses)
        embed.set_image(url=response)
        await ctx.send(embed=embed)

@client.command()
async def bowling(ctx):
        embed = discord.Embed(color=discord.Color.red())
        embed = discord.Embed(color=discord.Color.red())
        embed.set_image(
            url='https://nerdbacon.com/wp-content/uploads/2015/02/roman_sure_loves_bowling_by_robinolsen2011-d8057a0.jpg')
        await ctx.send(f'You: Recieves Phone Call.')
        await ctx.send(f'Roman: Nico!! Its Roman, lets go bowling!')
        await ctx.send(embed=embed)

@client.command(aliases=['memes'])
async def meme(ctx):
        submission = reddit.subreddit("memes").random() 
        embed = discord.Embed(color=discord.Color.red()) 
        embed.add_field(name= submission.title,value = "lol")  
        embed.set_image(url = submission.url)
        await ctx.send(embed = embed)

@client.command()
async def hack(ctx):
        hack = secrets.token_hex(1000)
        await ctx.send(hack)

client.run('x')
