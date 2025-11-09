# Welcome to the SmashBot repo!

## SmashBot is currently on version 0.0! (currently in beta)
_Features added this update:_ Initial version

## About
This discord bot is for managing Super Smash Ultimate matches how tournaments would.

### Features
- Blind character selection
- Stage striking
- Reporting results
  - Players have to agree on who won
### Small details
- Stage list:
  - Battlefield
  - Small Battlefield,
  - Pokémon Stadium 2
  - Smashville
  - Town & City
  - Final Destination
  - Kalos Pokémon League
  - Hollow Bastion
- Bot will DM you at certain points

## If you are planning on using this bot...
### You need to make your own bot. (A public bot is in progress but open source is great)
#### To-Do list:
- Go to the [Discord Developer Portal](https://discord.com/developers)
  - Set up a bot (look up a tutorial if needed)
  - Go to the Bot tab
  - Enable all intents
  - Tick the boxes that correspond to the intents in line 13-18 in [main.py](https://github.com/sp163r/smashbot-public/blob/master/main.py)
- Generate a token
- Replace "INSERT_TOKEN_HERE" with your token in [.env](https://github.com/sp163r/smashbot-public/blob/master/.env)
- **OPTIONAL:** make custom emojis for stages and replace `emoji=none` in [main.py](https://github.com/sp163r/smashbot-public/blob/master/main.py) with your emojis
  - You have to get the id of the emoji by inputting your emoji and putting `\` before it to get the id. Should look something like this: `\:INSERT_EMOJI_HERE:`
  - Then copy + paste it. Should look something like this: `emoji=<EMOJI_NAME:EMOJI_ID>`
- Just realized this is probably the hard way there is an emojis tab in the dev pool.

## Any issues?
There is an issues tab I will look at it probably

## Q/A
### Q:
Can I collab?
### A:
No.
