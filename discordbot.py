import os
import json
import time
import discord
from discord.ext import commands
import webbrowser
import requests
from requests.structures import CaseInsensitiveDict

# Strava API Key
api_key = os.environ.get('strava-api', None)

# Bot Prefix
bot = commands.Bot(command_prefix='!')

# Club Codes
codesFile = r"codedb.json"

# Current Date
seconds = time.time()
local_time = time.ctime(seconds)

def stravaData(curso, club):
    # Get JSON data from Strava with an HTTP GET request
    url = ("https://www.strava.com/api/v3/clubs/" + club + "/activities?page=1&per_page=200")
    url2 = ("https://www.strava.com/api/v3/clubs/" + club + "/activities?page=2&per_page=200")
    #url3 = ("https://www.strava.com/api/v3/clubs/" + club + "/activities?page=3&per_page=200")
 
    headers = CaseInsensitiveDict()
    headers["Authorization"] = ("Bearer " + api_key)
    
    global r

    r = requests.get(url, headers=headers)
    r2 = requests.get(url2, headers=headers)
    #r3 = requests.get(url3, headers=headers)

    # Store the data in JSON
    data = r.json()
    data2 = r2.json()
    #data3 = r3.json()
 
    # Create an empty list to fill later
    walkingData = []
    runningData = []
    ridingData = []
 
    # Iterate over the values and store them in lst
    for i in data:
        actType = (i["type"])
        if actType == ("Walk"):
            walkDistance = int(i["distance"])
            walkingData.append(walkDistance)
        elif actType == ("Run"):
            runDistance = int(i["distance"])
            runningData.append(runDistance)
        elif actType == ("Ride"):
            rideData = int(i["distance"])
            ridingData.append(rideData)
 
    for i in data2:
        actType = (i["type"])
        if actType == ("Walk"):
            walkDistance = int(i["distance"])
            walkingData.append(walkDistance)
        elif actType == ("Run"):
            runDistance = int(i["distance"])
            runningData.append(runDistance)
        elif actType == ("Ride"):
            rideData = int(i["distance"])
            ridingData.append(rideData)
 
    # for i in data3:
    #     actType = (i["type"])
    #     if actType == ("Walk"):
    #         walkDistance = int(i["distance"])
    #         walkingData.append(walkDistance)
    #     elif actType == ("Run"):
    #         runDistance = int(i["distance"])
    #         runningData.append(runDistance)
    #     elif actType == ("Ride"):
    #         rideData = int(i["distance"])
    #         ridingData.append(rideData)
 
    global rawWalkingData, rawRunningData, rawRidingData, adjustedRidingData, totalDistance
    rawWalkingData = sum(walkingData) / 1000
    rawRunningData = sum(runningData) / 1000
    rawRidingData = (sum(ridingData) / 1000)
    adjustedRidingData = (sum(ridingData) / 1000) * 0.2
 
    totalDistance = (rawWalkingData + rawRunningData + adjustedRidingData)
 
@bot.event
async def on_ready():
    print("[✅] Logged in as |" + str(bot.user.name) + "| with the ID: " + str(bot.user.id))


@bot.command()
async def list(ctx):
    
    try:
        print("[👏] !list was executed by: " + ctx.message.author.name + " in " + ctx.message.guild.name)
    except:
        pass

    if isinstance(ctx.channel, discord.channel.DMChannel):
        print("[⚠] " + ctx.message.author.name + "#" + ctx.message.author.discriminator + " has tried to use !list through DMs")
        await ctx.send("Only server admins can exectue this command")
    elif ctx.message.author.guild_permissions.administrator:
            
        with open(codesFile, 'r', encoding="utf8") as f:
            codeData = json.load(f)

        for i in codeData["codes"]:
            cursoJ = str(i["curso"])
            clubJ = str(i["codigo"])

            try:
                stravaData(cursoJ, clubJ)
                print("[✔] " + cursoJ + " data was sent correctly. " + local_time)
                
                embed=discord.Embed(title=cursoJ + " Stats", color=0x00d900)
                embed.set_thumbnail(url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
                embed.add_field(name="Walking", value=str(rawWalkingData) + "km", inline=True)
                embed.add_field(name="Running", value=str(rawRunningData) + "km", inline=True)
                embed.add_field(name="Cycling", value=str(rawRidingData) + "km", inline=True)
                embed.add_field(name="Total", value=str(round(totalDistance)) + "km", inline=True)
                embed.set_footer(text="Strava Stats", icon_url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
                await ctx.send(embed=embed)

            except:
                embed=discord.Embed(title=cursoJ + " Stats", color=0xff282e)
                embed.add_field(name="Error", value=str(r.status_code), inline=True)
                embed.set_footer(text="Strava Stats", icon_url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
                await ctx.send(embed=embed)

                print(str(r.status_code) + " [❌] " + cursoJ + " data was not sent correctly. " + local_time)
                pass

    else:
        print("check !list func, something went wrong!")


@bot.command()
async def strava(ctx, clsd):
    
    with open(codesFile, 'r', encoding="utf8") as f:
        codeData = json.load(f)

    clubID = codeData[str(clsd)]

    try:
        stravaData(clsd, clubID)
        print("[✔] " + clsd + " data was sent correctly. " + local_time)
        
        embed=discord.Embed(title=clasd + " Stats", color=0xff8000)
        embed.set_thumbnail(url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
        embed.add_field(name="Walking", value=str(rawWalkingData) + "km", inline=True)
        embed.add_field(name="Running", value=str(rawRunningData) + "km", inline=True)
        embed.add_field(name="Cycling", value=str(rawRidingData) + "km", inline=True)
        embed.add_field(name="Total", value=str(round(totalDistance)) + "km", inline=True)
        embed.set_footer(text="Strava Stats", icon_url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title=clasd + " Stats", color=0xff282e)
        embed.add_field(name="Error", value=str(r.status_code), inline=True)
        embed.set_footer(text="Strava Stats", icon_url="https://i.ibb.co/cbSMsfL/b5537c13e65d4110c4d3282f25a83799.png")
        await ctx.send(embed=embed)

        print(str(r.status_code) + " [❌] " + clsd + " data was not sent correctly. " + local_time)
        pass
    
bot.run(str(os.environ.get('discord-api', None)))