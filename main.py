import asyncio
import logging
import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.messages = True
intents.members = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# stage list so that i can reference them in messages
stages = [
    "Battlefield",
    "Small Battlefield",
    "Pokémon Stadium 2",
    "Smashville",
    "Town & City",
    "Final Destination",
    "Kalos Pokémon League",
    "Hollow Bastion"
]


# Stage strike view with counterpicks
class StageStrikeC(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.strike1 = None
        self.strike2 = None
        self.user = None

    @discord.ui.select(
        min_values=2,
        max_values=2,
        placeholder="Strike a stage...",
        options=[
            discord.SelectOption(
                label="Battlefield",
                emoji=None,
                value=0
            ),
            discord.SelectOption(
                label="Small Battlefield",
                emoji=None,
                value=1
            ),
            discord.SelectOption(
                label="Pokémon Stadium 2",
                emoji=None,
                value=2
            ),
            discord.SelectOption(
                label="Smashville",
                emoji=None,
                value=3
            ),
            discord.SelectOption(
                label="Town & City",
                emoji=None,
                value=4
            ),
            discord.SelectOption(
                label="Final Destination",
                emoji=None,
                value=5
            ),
            discord.SelectOption(
                label="Kalos Pokémon League",
                emoji=None,
                value=6
            ),
            discord.SelectOption(
                label="Hollow Bastion",
                emoji=None,
                value=7
            )
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.strike1 = select.values[0]
        self.strike2 = select.values[1]
        self.user = interaction.user
        select.disabled = True
        await interaction.response.defer(thinking=False)  # make it so that it doesn't say ! This interaction failed
        self.stop()


# Stage strike view without counterpicks
class StageStrikeN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.strike1 = None
        self.strike2 = None
        self.user = None

    @discord.ui.select(
        min_values=2,
        max_values=2,
        placeholder="Strike a stage...",
        options=[
            discord.SelectOption(
                label="Battlefield",
                emoji=None,
                value=0
            ),
            discord.SelectOption(
                label="Small Battlefield",
                emoji=None,
                value=1
            ),
            discord.SelectOption(
                label="Pokémon Stadium 2",
                emoji=None,
                value=2
            ),
            discord.SelectOption(
                label="Smashville",
                emoji=None,
                value=3
            ),
            discord.SelectOption(
                label="Town & City",
                emoji=None,
                value=4
            )
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.strike1 = select.values[0]
        self.strike2 = select.values[1]
        self.user = interaction.user
        select.disabled = True
        await interaction.response.defer(thinking=False)
        self.stop()


# Stage strike view without counterpicks, only 1 strike
class StageStrikeN1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.strike1 = None
        self.user = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Strike a stage...",
        options=[
            discord.SelectOption(
                label="Battlefield",
                emoji=None,
                value=0
            ),
            discord.SelectOption(
                label="Small Battlefield",
                emoji=None,
                value=1
            ),
            discord.SelectOption(
                label="Pokémon Stadium 2",
                emoji=None,
                value=2
            ),
            discord.SelectOption(
                label="Smashville",
                emoji=None,
                value=3
            ),
            discord.SelectOption(
                label="Town & City",
                emoji=None,
                value=4
            )
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.strike1 = select.values[0]
        self.user = interaction.user
        select.disabled = True
        await interaction.response.defer(thinking=False)
        self.stop()


# choose a stage with counterpicks
class StageChooseC(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.choice = None
        self.user = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Strike a stage...",
        options=[
            discord.SelectOption(
                label="Battlefield",
                emoji=None,
                value=0
            ),
            discord.SelectOption(
                label="Small Battlefield",
                emoji=None,
                value=1
            ),
            discord.SelectOption(
                label="Pokémon Stadium 2",
                emoji=None,
                value=2
            ),
            discord.SelectOption(
                label="Smashville",
                emoji=None,
                value=3
            ),
            discord.SelectOption(
                label="Town & City",
                emoji=None,
                value=4
            ),
            discord.SelectOption(
                label="Final Destination",
                emoji=None,
                value=5
            ),
            discord.SelectOption(
                label="Kalos Pokémon League",
                emoji=None,
                value=6
            ),
            discord.SelectOption(
                label="Hollow Bastion",
                emoji=None,
                value=7
            )
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.choice = select.values[0]
        self.user = interaction.user
        select.disabled = True
        await interaction.response.defer(thinking=False)
        self.stop()


# choose a stage without counterpicks
class StageChooseN(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.choice = None
        self.user = None

    @discord.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Strike a stage...",
        options=[
            discord.SelectOption(
                label="Battlefield",
                emoji=None,
                value=0
            ),
            discord.SelectOption(
                label="Small Battlefield",
                emoji=None,
                value=1
            ),
            discord.SelectOption(
                label="Pokémon Stadium 2",
                emoji=None,
                value=2
            ),
            discord.SelectOption(
                label="Smashville",
                emoji=None,
                value=3
            ),
            discord.SelectOption(
                label="Town & City",
                emoji=None,
                value=4
            )
        ]
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self.choice = select.values[0]
        self.user = interaction.user
        select.disabled = True
        await interaction.response.defer(thinking=False)
        self.stop()


# select players
class PlayerSelect(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)
        self.p1 = None
        self.p2 = None

    @discord.ui.button(
        label="Player 1",
        style=discord.ButtonStyle.blurple
    )
    async def callback1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.p1 = interaction.user
        await interaction.channel.send(f'Player 1 is selected as {self.p1.display_name}')
        button.disabled = True
        await interaction.response.edit_message(view=self)
        if self.p1 and self.p2:
            self.stop()

    @discord.ui.button(
        label="Player 2",
        style=discord.ButtonStyle.red
    )
    async def callback2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.p2 = interaction.user
        await interaction.channel.send(f'Player 2 is selected as {self.p2.display_name}')
        button.disabled = True
        await interaction.response.edit_message(view=self)
        if self.p1 and self.p2:
            self.stop()


# select who won
class WinSelect(discord.ui.View):
    def __init__(self, p1, p2):
        super().__init__(timeout=999999999999)
        self.choice = None
        self.pl1 = p1
        self.pl2 = p2

    @discord.ui.button(
        label="Player 1",
        style=discord.ButtonStyle.blurple
    )
    async def callback1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.choice = self.pl1
        await interaction.response.defer(thinking=False)
        self.stop()

    @discord.ui.button(
        label=f"Player 2",
        style=discord.ButtonStyle.red
    )
    async def callback2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.choice = self.pl2
        await interaction.response.defer(thinking=False)
        self.stop()


# button to report results
class ReportResults(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Done!",
        style=discord.ButtonStyle.green
    )
    async def callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.defer(thinking=False)
        self.stop()


# tell when the bot will actually start working (it being online does not mean anything)
@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready.')


# init a match
@bot.command()
async def match(ctx, *, msg):
    # character selection

    # check matchtype
    if msg == "1":  # or msg == "2":  TODO: matchtype 2
        matchtype = msg
    else:  # errors if matchtype is not valid
        embed = discord.Embed(title=f'Error! Match type cannot be {msg}.',
                              description="1: Single match \n2: Best of 3 ***(NOT FUNCTIONAL YET)***",
                              color=discord.Color.red())
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(title="Who is playing?", description="Press the button corresponding to what player you are.",
                          color=discord.Color.yellow())
    playerView = PlayerSelect()
    await ctx.send(embed=embed, view=playerView)  # ask who is playing

    await playerView.wait()  # wait until both buttons are pressed

    p1 = playerView.p1  # set players
    p2 = playerView.p2

    ch = ctx.channel  # shorter channel var and for passing into funcs

    embed = discord.Embed(title="Who are you playing?",
                          description="Message me the character you are playing.\n-# You have 5 minutes to respond or else you will forfeit.",
                          color=discord.Color.yellow())
    await p1.send(embed=embed)  # ask p1 who is playing
    c1 = await dmPlayerC(p1, ch)  # get response
    if c1 is None:
        return # dont continue if forfeit

    embed = discord.Embed(title="Who are you playing?",
                          description="Message me the character you are playing.\n-# You have 5 minutes to respond or else you will forfeit.",
                          color=discord.Color.yellow())
    await p2.send(embed=embed)  # ask p2 who is playing
    c2 = await dmPlayerC(p2, ch)  # get response
    if c2 is None:
        return # dont continue if forfeit

    await ch.send(f'{p1.mention}{p2.mention}')
    embed = discord.Embed(title=f'__{p1.display_name} VS. {p2.display_name}__',
                          description=f'{p1.display_name} will be playing {c1}.\n{p2.display_name} will be playing {c2}.')
    await ch.send(embed=embed)  # declare characters

    # stage striking
    strikes = [None, None, None]  # strike array

    embed = discord.Embed(title="Match Selection", description="Player 1 is striking...", color=discord.Color.yellow())
    view = StageStrikeN1()
    await ctx.send(embed=embed, view=view)  # p1 strikes 1 stage
    await view.wait()
    await ctx.send(f"{view.user.display_name} has striken {stages[int(view.strike1)]}.")  # show what was striken
    strikes[0] = view.strike1  # set strike

    embed = discord.Embed(title="Match Selection", description="Player 2 is striking...", color=discord.Color.yellow())
    view = StageStrikeN()
    await ctx.send(embed=embed, view=view)  # p2 strikes 2 stages
    await view.wait()
    await ctx.send(
        f"{view.user.display_name} has striken {stages[int(view.strike1)]} and {stages[int(view.strike2)]}.")  # show what was striken
    strikes[1] = view.strike1
    strikes[2] = view.strike2  # set strikes

    isDone = False
    while not isDone:
        embed = discord.Embed(title="Match Selection", description="Player 1 is choosing...",
                              color=discord.Color.yellow())
        view = StageChooseN()
        await ctx.send(embed=embed, view=view)  # choose a stage
        await view.wait()

        if view.choice == strikes[0] or view.choice == strikes[1] or view.choice == strikes[
            2]:  # deny if a stage was striken
            await ctx.send(f'{view.user.mention} that stage is struck. Pick another')
        else:
            isDone = True  # finish

    await ctx.send(f"{view.user.display_name} has chosen {stages[int(view.choice)]}.")  # show what was chosen

    await ch.send(f'{p1.mention}{p2.mention}')  # @ the users
    embed = discord.Embed(title=f'__{p1.display_name} VS. {p2.display_name}__',
                          description=f'{p1.display_name} will be playing {c1}.\n{p2.display_name} will be playing {c2}.\nThey will be playing on {stages[int(view.choice)]}.')
    await ch.send(embed=embed) # declare match details

    # report results
    embed = discord.Embed(title=f'Report results',
                          description=f'When you are done, press the button.')
    view = ReportResults()
    await ctx.send(embed=embed, view=view) # after you press the button it will start reporting results phase
    await view.wait()

    isDone = False
    while not isDone:

        embed = discord.Embed(title="Who won?",
                              description=f"Player 1: {p1.display_name}\nPlayer 2: {p2.display_name}",
                              color=discord.Color.yellow())
        view = WinSelect(p1=p1, p2=p2)
        await p1.send(embed=embed, view=view) # ask p1 who won
        await view.wait()
        p1selection = view.choice # save selection
        await p1.send(f"Great! You selected {p1selection.display_name}. Go back to the server.") # confirm what they chose

        view = WinSelect(p1=p1, p2=p2)
        await p2.send(embed=embed, view=view) # ask p2 who won
        await view.wait()
        p2selection = view.choice # save selection
        await p2.send(f"Great! You selected {p2selection.display_name}. Go back to the server.") # confirm

        if p1selection == p2selection: # do they agree?
            isDone = True
        else:
            await ctx.send(f'{p1.mention}{p2.mention}\n### Both players do not agree. Trying again.')

    await ctx.send(f'{p1.mention}{p2.mention}\n{p1selection.mention} wins!') # declare winner


async def dmPlayerC(user, ch): # get player message
    try:
        char = await bot.wait_for('message', check=lambda x: x.channel == user.dm_channel and x.author == user, timeout=300) # wait for a message for 5 min
    except asyncio.TimeoutError: # check for timeout
        await user.send("Timed out :(")
        await ch.send(f'{user.display_name} forfeited due to timeout.') # forfeit player
        return None
    else:
        await user.send("Great! Go back to the server.")

        return char.content

bot.run(token, log_handler=handler, log_level=logging.DEBUG) # start up bot