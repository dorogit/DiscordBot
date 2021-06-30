import discord
import os
import random

client = discord.Client()
guild = client.get_guild(692625157369495582)
                         
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    msg = ""
    user = message.author
    user1 = None
    myid = None
    spam = ""
    list = []
    a = None
    discord.utils.get
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
      a= random.randint(1, 2)
      if a == 1:
        await message.channel.send('I will try to roast or have fun with you depending on what you type so grow a pair and dont get offended uwu. Dm <@681151593064038494> if you want something added, or type +commands.')
      if a == 2:
        await message.channel.send("no")
    if message.content.startswith('+who'):
        await message.channel.send('ahobot at your service!')
    if message.content.startswith('+owo'):
        await message.channel.send('uwu')
    if message.content.startswith('+flip'):
        await message.channel.send('(╯°□°）╯︵ ┻━┻')
    if message.content.startswith('+aho'):
        await message.channel.send('whomst has summoned the almighty one')
    if message.content.startswith('+food'):
        a = random.randint(1,5)
        if a == 1:
          msg = 'no food for {} hmph!'.format(message.author)
          
        if a == 2:
          msg = '{} indulges in the luscious taste of air'.format(message.author)
          
        if a == 3:
          msg = '{} I dropped the pizza gomennasai >^<'.format(message.author)
         
        if a == 4:
          msg = 'food is not something you acquire for free. You must for for it and earn it from your own blood and sweat. tatakae'
          
        if a == 5:
          msg = 'I will eat you'
        await message.channel.send(msg)
    if message.content.startswith('+gae'):
        msg = '{} u gae'.format(message.author)
        await message.channel.send(msg[5:msg.length()])
    if message.content.startswith('+commands'):
        await message.channel.send('only these commands are available :')
        await message.channel.send('+hello,+qt,+tensai (this one is really cool),+ID,+wisdom,+help,+who,+owo,+unfunne,+food,+gae,+commands,+spam @user,+qtmode,+aho, +recipe, +sin,+loli,+flip,+ .... YET')
    if message.content.startswith('+qtmode'):
        await message.channel.send('qt mode activated uwu >.<')
    if message.content.startswith('+wisdom'):
      a = random.randint(1,5)
      if a == 1:
        await message.channel.send('लूट सके तो लूट ले, राम नाम की लूट । पाछे फिर पछ्ताओगे, प्राण जाही जब छूट ।।')
      if a == 2:
        await message.channel.send('जाति न पूछो साधु की, पूछ लीजिये ज्ञान, मोल करो तलवार का, पड़ा रहन दो म्यान।')
      if a == 3:
        await message.channel.send('धीरे-धीरे रे मना, धीरे सब कुछ होय, माली सींचे सौ घड़ा, ॠतु आए फल होय।')
      if a == 4:
        await message.channel.send('तिनका कबहुँ ना निन्दिये, जो पाँवन तर होय, कबहुँ उड़ी आँखीन पड़े, तो पिर घनेरि होय।')
      if a == 5:
        await message.channel.send('काल करे सो आज कर, आज करे सो अब । पल में प्रलय होएगी, बहुरी करेगा कब ।।')
    if message.content.startswith('+recipe'):
        await message.channel.send("Biryani: A mild, rice-based dish cooked with meat and/or vegetables and served with yoghurty sauce Chaat: Savoury snacks, often made with potato or chick peas Dahl: A lentil curry similar to thick lentil soup Elaichi: Cardamom Firni: Rice pudding with saffron and nuts Gosht: Meat, usually lamb Hari Mirch: Green chilli Idli: A savoury lentil cake Jalfrezi: A spicy dish cooked with ginger and chilli Kachori: Crisp pastry rounds with spiced mung dahl or pea filling Lassi: A yoghurt drink, ordered with salt or sugar, sometimes with fruit. Ideal to cool a fiery palate Murgh: Chicken Naan: Flatbreads cooked in a large tandoor oven Onion bhaji: Crispy deep-fried onion balls Peshwari: Bread or dish with sweet dry fruit and nuts Quinoa Pilaf: A spicy Indian preparation of the seed Rasmalai: A traditional dessert of sweet cottage cheese dumplings, topped with saffron Saslik: Anything grilled Tandoori: Baked in a clay/mud oven Udrak: Ginger Vindaloo: Hot curry, often with potato. Xacuti: A Goan dish made with lamb or chicken, coconut and a complex mix of roasted then ground spices Yakhini: Soup or gravy Zeera: Cumin")
    if message.content.startswith('+loli'):
        await message.channel.send("{} likes little schoolgirls >:(".format(message.author))
    if message.content.startswith('+spam'):
      msg = message.content
      for num in range(10):
        await message.channel.send(msg[5:len(msg)])
    if message.content.startswith('+unfunne'):
      a = random.randint(1,15)
      if a == 1:
        await message.content.send('Why dont they show vaginas in anime? Because it would be a plot hole')
      if a == 2:
        await message.content.send('Where do anime girls live? Ohio')
      if a == 3:
        await message.content.send('How many tickles will turn on an Anime girl? Tentacles')
      if a == 4:
        await message.content.send('What character do you get when you cross a Sailor with a Cow? Sailor Moo')
      if a == 5:
        await message.content.send(' Why did Saitama get fired from his job when working in the railways as a conductor? Because he had to punch a ticket')
      if a == 6:
        await message.content.send('What does MonkeyD. Luffy say when you want another piece of the pie? You can only have One piece')
      if a == 7:
        await message.content.send('Why does Miso not like the world anymore? Because there is no Light')
      if a == 8:
        await message.content.send('what do you call a titan who cant swim? a titanic')
      if a == 9:
        await message.content.send('How many Dragon Ball Z characters does it take to screw in a lightbulb? Just one, but it’ll take six episodes')
      if a == 10:
        await message.content.send('What do Saiyans wear to the beach? Trunks.')
      if a == 11:
        await message.content.send('Where did Vegeta go after death? Into the frieza')
      if a == 12:
        await message.content.send('What type of novels does L like? Light Novel')
      if a == 13:
        await message.content.send('Why did Goku get into another fight with Vegeta? Because he was Saiyan bad jokes')
      if a == 14:
        await message.content.send('. What do you call a factory that makes okay products? A satisfactory')
      if a == 15:
        await message.content.send('sorry I am unfunne ;-;')
        
    if message.content.startswith('+sin'):
        await message.channel.send('aapko apne paapon ka pashchatap karna chahiye| vah tumhe nasht kar denge|aap koi mauka nahi khade hai| tum usko haath par bhuktoge| pachtana|')
        
client.run("ODU3NDY3MjIyODM3NTU5Mjk2.YNQAlA.N8wDKWubrCDivSnZemT_08nPujA")
