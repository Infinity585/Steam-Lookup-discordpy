import requests , json , discord , os , re , datetime
from discord import app_commands
from discord.ext import commands
from embed import newEmbed


class steamSearch(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.steamKey = os.getenv("STEAM_API_KEY")

    

    '''
    Creates an embed of the steam profile of the user with the given steam identifier (steam 64, hex, or vanity id)
    @param interaction : discord.Interaction the interaction object of the user who called the command
    @param steamid : str the steam identifier of the user
    '''
    @app_commands.command(name = "steam", description = "Command to search for a steam profile")
    @app_commands.describe(steamid = "The steam 64, hex or vanity id of the user you want to search for")
    async def steamlookup(self, interaction : discord.Interaction, steamid : str):
        id = self.getID(steamid) #Gets the steam 64 ID
        if id == None: #If the ID is invalid, return an error message
            await interaction.response.send_message(f"Invalid or Unknown Steam Id ({steamid})", ephemeral=True)
            return
        
        #requests the userdata and bans infomation from steam
        userRequest = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.steamKey}&steamids={id}")
        bansRequest = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={self.steamKey}&steamids={id}")
        
        #check the status code of the requests, if they are not 200 (sucessful), return an error message
        if userRequest.status_code != 200 or bansRequest.status_code != 200:
            await interaction.response.send_message("Error with steam API", ephemeral=True)
            return
        
        #loads the json data from the requests
        bansdata = json.loads(bansRequest.text)['players'][0]
        userdata = json.loads(userRequest.text)["response"]['players'][0]

        #creates a discord embed containing the infomation from the requests using the newEmbed method from embed.py
        fm = newEmbed(title=f"Steam Profile Look Up",  #embed title 
        fields={  #embed fields
            "Steam Name": userdata['personaname'],
            "Steam Hex":"Steam:"+(hex(int(id))[2:]),
            "Steam ID":userdata['steamid'],
            "realname":userdata['realname'] or "Unknown",
            "Country":userdata['loccountrycode'] or "Unknown",
            "VAC Bans":bansdata['NumberOfVACBans'],
            "Game Bans":bansdata['NumberOfGameBans'],
            "Days Since Last Ban" : bansdata['DaysSinceLastBan'],
            "Account Creation Date (M-D-Y)": datetime.datetime.fromtimestamp(int(userdata["timecreated"])).strftime('%m-%d-%Y') or "Unknown", #time of account create or Unknown if they have a private profile profile
            "Profile URL": f"[Click Here]({userdata['profileurl']})",
        },
        embedUrl=userdata['avatarfull'] #the profile picture of the user
        )

        await interaction.response.send_message(embed=fm, ephemeral=True) # sends the embed that was created to the user who requested the search

        
        

    '''
    Method to return the 64 bit steam id of the user or None if it is invalid
    @param steamid : str the steam identifier of the user
    @return steamid : int steam 64 id of the user or None if the steam id is invalid
    '''
    def getID(self, steamid):
        if re.match(r'^\d{17}$', steamid):
            return int(steamid)
        elif re.match(r'^steam:[A-Fa-f0-9]{15}$', steamid):
            id = (steamid[6:])
            return int(id,16)
        elif re.match(r'^[A-Za-z0-9_]+$', steamid):
            id = self.getVanityURl(steamid)
            if id != None: return id
            id = self.getVanityURl(steamid[30:])
            return id
        return None
    
    
    '''
    Method to check if the vanity id is valid and get the steam 64 id of the user
    @param steamid : str the vanity id of the user
    @return steamid : int steam 64 id of the user or None if the vanity id is invalid
    '''
    def getVanityURl(self, steamid):
        res = requests.get(f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={self.steamKey}&vanityurl={steamid}")
        vanitydata = json.loads(res.text)["response"]
        if vanitydata["success"] == 1:
            return vanitydata["steamid"]
        else:
            return None
    

            
async def setup(bot : commands.Bot):
    bot.add_cog(steamSearch(bot))