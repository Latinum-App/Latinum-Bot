import itertools
import discord
from discord.ext import commands
import aiohttp
import random
from discord.ext.commands.core import command
import io
import json
import asyncio
import sqlite3 as sl

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.messages = True
bot = commands.Bot(command_prefix = ".", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print("Hello World.")
    con = sl.connect('vocabulary.db')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOUR STATUS HERE"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.NSFWChannelRequired):
        await ctx.send("You can only use this command in an NSFW channel.")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all requirements for the command.")

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the permissions to use this command.")

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I don't know a command like this.")

    if isinstance(error, commands.MemberNotFound):
        await ctx.send("Looks like this User isn't on the server.")

    if isinstance(error, commands.ChannelNotFound):
        await ctx.send("Looks like this channel doesn't exist.")

    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have permission to do that.")

@bot.command()
async def challenge(ctx):
    score = 0
    if str(ctx.channel.type) == "private":
        dm = await ctx.send("❓ Do you really want to start the Vocabulary Challenge?")
        await dm.add_reaction("✅")
        await dm.add_reaction("⛔")

        emojis = ["✅", "⛔"]
        moreoma = ctx.author.id
        def check(reaction, user):
            return user.id == moreoma and str(reaction.emoji) in emojis

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=10, check=check)
        except asyncio.TimeoutError:
            await ctx.send("❗ Automatically canceled after 10s.")
        else:
            if reaction.emoji == "✅":
                game = True
                await ctx.send("Ok. I will start!")

                while game == True:
                    con = sl.connect('vocabulary.db')

                    with con:
                        data = con.execute("SELECT * FROM Vocabulary ORDER BY RANDOM() LIMIT 1;")
                        for row in data:
                            one = (row[0])
                            two = (row[1])
                            
                            choices = [one, two]
                            first = random.choice(choices)

                            if first == one:
                                second = two
                            else:
                                second = one

                    em = discord.Embed(title="Let's see if you can translate that...", description = f"Please translate the word **{first}**!")
                    em.set_footer(text="You can always get the answer with .help and you can stop the challenge with .stop")
                    dm = await ctx.send(embed=em)

                    def check(m): return m.author == ctx.author and m.channel == ctx.channel
                    msg = await bot.wait_for('message', check=check, timeout=None)
                    if str(msg.content) == second:
                        await ctx.send("✅ Thats right! Let's see if you get the next one.")
                        score = score + 1
                    elif str(msg.content) == ".help":
                        await ctx.send(f"💡 The right answer would be **{second}**! Maybe ypu gat the next one right.")
                    elif str(msg.content) == ".stop":
                        game = False
                        await ctx.send(f"Ok, I will stop the Game. I hope to see you again soon!")
                    else:
                        await ctx.send(f"❌ Sadly, thats wrong. The answer was **{second}**, but atleast you got {score} right before your made the mistake!")
                        game = False

                        em = discord.Embed(title="Another try or not?", description = "Want to play again?")
                        em.set_footer(text="If you want to play again press ✅, if you don't want to play anymore press ⛔.")
                        dm2 = await ctx.send(embed=em)
                        await dm2.add_reaction("✅")
                        await dm2.add_reaction("⛔")

                        emojis = ["✅", "⛔"]
                        moreoma = ctx.author.id
                        def check2(reaction, user):
                            return user.id == moreoma and str(reaction.emoji) in emojis

                        try:
                            reaction, user = await bot.wait_for('reaction_add', timeout=10, check=check2)
                        except asyncio.TimeoutError:
                            await ctx.send("❗ Automatically canceled after 10s.")
                        else:
                            if reaction.emoji == "✅":
                                await ctx.send("Ok. Let's start again!")
                                game = True
                            elif reaction.emoji == "⛔":
                                await ctx.send("Ok. I hope to see you again soon!")

    if str(ctx.channel.type) != "private":
        await ctx.send("You can only use this command in my DM's.")

@bot.command()
async def addvocabulary(ctx, latein, deutsch):
    con = sl.connect('vocabulary.db')

    sql = 'INSERT INTO Vocabulary (word1, word2) values(?, ?)'
    data = [(latein, deutsch)]

    with con:
        con.executemany(sql, data)

    await ctx.send(f"I added {latein} - {deutsch} to my vocabulary list.")

bot.run("YOUR TOKEN HERE!")
