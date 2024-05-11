import discord

'''
Method used to make embeds 
@param title : str title of the embed
@param fields : dict key is the title of the field, value is the value of the field
@param embedUrl : str url of the thumbnail
@return em : discord.Embed with the given title and fields.
'''
def newEmbed(title=None, fields=None, embedUrl = None , **kwargs):
    em = discord.Embed(title=f"{title}", color=0x00b7ff) #Creates the discord embed with the title and color
    if embedUrl: #if there is a url, set the thumbnail to the url
        em.set_thumbnail(url= embedUrl)
    
    for key in fields: #for each key in the fields, add a field to the embed with its value
        em.add_field(name=key, value=fields[key], inline=False)
    em.set_footer(text="Infinitys Steam API Search") #sets the footer of the embed
    return em # returns the embed