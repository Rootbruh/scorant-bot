import discord
from authority import Authority
from discord.ext import commands

client = commands.Bot(command_prefix="V-")
client.remove_command("help")


@client.command()
async def help(msg):
    await msg.send("""
    `                                                                                                  
    =========================================HELP MENU==============================================   
    |                                                                                              |   
    | Bot Commands:                                                                                |   
    |                                                                                              |   
    | V-cross: to get crosshair advice.                                                            |   
    | V-twitch: to get your twitch channel data.(login required.)                                  |   
    | V-compare: compares your stats to another valorant streamer of similar popularity.           |   
    | V-wallpaper: to get any wallpaper about valorant.                                            |   
    | V-music: listen to music on audio channel.(sources: youtube, spotify, soundcloud, funkwhale) |   
    | V-social: our social media addresses (github, mastodon, odysee, gitlab, reddit)              |   
    ================================================================================================   
   
    IMPORTANT:You are using nightly version now so you can see some bugs. If you see any bug please report to our wiki

    `                                                                
    
    
                                                                                                                                
    """)


@client.event
async def on_ready():
    print("I am ready to f*ck any server!")


if __name__ == '__main__':
    client.load_extension("authority")
    client.load_extension("listener")

    client.run('TOKEN IS HERE')
