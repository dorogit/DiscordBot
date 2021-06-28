import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = ""
    if message.author == client.user:
        return

    if message.content.startswith('+hello'):
        await message.channel.send('hi!')
    if message.content.startswith('+qt'):
        await message.channel.send('qt XDXD')
    if message.content.startswith('+tensai'):
        await message.channel.send('loli master tensai!')
    if message.content.startswith('+ID'):
        await message.channel.send(message.author)
    if message.content.startswith('+help'):
        await message.channel.send('bot with text commands which returns mildly funny stuff. Made by @dororo#9523 if you want something added, or type +commdands.')
    if message.content.startswith('+who'):
        await message.channel.send('ahobot at your service!')
    if message.content.startswith('+owo'):
        await message.channel.send('uwu')
    if message.content.startswith('+flip'):
        await message.channel.send('(╯°□°）╯︵ ┻━┻')
    if message.content.startswith('+aho'):
        await message.channel.send('whomst has summoned the almighty one')
    if message.content.startswith('+food'):
        msg = 'no food for {} hmph!'.format(message.author)
        await message.channel.send(msg)
    if message.content.startswith('+gae'):
        msg = '{} u gae'.format(message.author)
        await message.channel.send(msg)
    if message.content.startswith('+commands'):
        await message.channel.send('only these commands are available :')
        await message.channel.send('+hello,+qt,+tensai (this one is really cool),+ID,+help,+who,+owo,+food,+gae,+commands,+qtmode,+aho, +recipe, +sin,+loli,+flip,+ .... YET')
    if message.content.startswith('+qtmode'):
        await message.channel.send('qt mode activated uwu >.<')
    if message.content.startswith('+recipe'):
        await message.channel.send("Biryani: A mild, rice-based dish cooked with meat and/or vegetables and served with yoghurty sauce Chaat: Savoury snacks, often made with potato or chick peas Dahl: A lentil curry similar to thick lentil soup Elaichi: Cardamom Firni: Rice pudding with saffron and nuts Gosht: Meat, usually lamb Hari Mirch: Green chilli Idli: A savoury lentil cake Jalfrezi: A spicy dish cooked with ginger and chilli Kachori: Crisp pastry rounds with spiced mung dahl or pea filling Lassi: A yoghurt drink, ordered with salt or sugar, sometimes with fruit. Ideal to cool a fiery palate Murgh: Chicken Naan: Flatbreads cooked in a large tandoor oven Onion bhaji: Crispy deep-fried onion balls Peshwari: Bread or dish with sweet dry fruit and nuts Quinoa Pilaf: A spicy Indian preparation of the seed Rasmalai: A traditional dessert of sweet cottage cheese dumplings, topped with saffron Saslik: Anything grilled Tandoori: Baked in a clay/mud oven Udrak: Ginger Vindaloo: Hot curry, often with potato. Xacuti: A Goan dish made with lamb or chicken, coconut and a complex mix of roasted then ground spices Yakhini: Soup or gravy Zeera: Cumin")
    if message.content.startswith('+loli'):
        await message.channel.send("{} likes little schoolgirls >:(".format(message.author))
    if message.content.startswith('+sin'):
        await message.channel.send('aapko apne paapon ka pashchatap karna chahiye| vah tumhe nasht kar denge|aap koi mauka nahi khade hai| tum usko haath par bhuktoge| pachtana|')
client.run("ODU3NDY3MjIyODM3NTU5Mjk2.YNQAlA.N8wDKWubrCDivSnZemT_08nPujA")
