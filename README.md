
# Steam Player Lookup Discord.py

Steam player lookup is a Discord bot built using discord.py that allows users to search for Steam player data and returns it as an embed.


## Features

- Searching steam profiles with Steam 64 id
- Searching steam profiles with vanity URLs
- Searching steam profiles with Steam Hex


## Installation

Install the dependnecies

```bash
pip install -r requirements.txt
```

then setup the Environment Variables


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file or use .env file found within the repository

`APPLICATION_ID`

`TOKEN`

`STEAM_API_KEY`
## Usage

1. Invite the bot to your Discord server using the invite link generated from the Discord Developer Portal.

2. Start the bot by running:
```bash
python3 main.py
 ```
3. Use the following slash command /steam
 
 ```diff
 /steam steamid:Infinity_585
 ```
 ```diff
 /steam steamid:Steam:11000011656271c
 ```
 ```diff
 /steam steamid:76561198335010588
 ```


## Example

![Example image](https://imgur.com/Io7GOQP.png)


## Contributing

Contributions are always welcome! If you'd like to contribute feel free to open a pull request.


