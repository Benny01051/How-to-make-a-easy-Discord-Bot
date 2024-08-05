import discord
from discord.ext import commands




intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.tree.command(name='membercount', description='show how many members')
async def member_count(interaction: discord.Interaction):
    guild = interaction.guild
    member_count = guild.member_count

    embed = discord.Embed(title="Server Member Count", color=discord.Color.red())
    embed.add_field(name="Members", value=member_count, inline=False)

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='delete_messages')
async def clear_messages(ctx, channel: discord.TextChannel):
    embed = discord.Embed(title="Alert", description="im deleting messages now", color=discord.Color.red())
    embed_message = await ctx.channel.send(embed=embed)

    async for message in channel.history(limit=None):
        try:
            await message.delete()
        except:
            pass

    await embed_message.delete()

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")
    await member.add_roles(role)


bot.run("YOUR BOT TOKEN")
