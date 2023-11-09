from io import BytesIO
import random
import discord
from discord.ext import commands

from PIL import Image, ImageFilter

#'https://media.discordapp.net/attachments/876676785859874898/971033802904317952/image0-4.gif'


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #@commands.Cog.listener()
    #async def on_message(self, ctx):
    #if ctx.author.id == 931000601263878174 or ctx.author.id == 259808943138668545:
    #await ctx.channel.send(
    #'https://media.discordapp.net/attachments/876676785859874898/971033802904317952/image0-4.gif'
    #)

# ---------------------------------------- Echo Command ----------------------------------------
# Repeats the message typed by the author.

    @commands.command(aliases=['e'])
    async def echo(self, ctx, *args):
        input = [*args]
        if bool(input):
            await ctx.reply(" ".join(args), mention_author=False)
            print("Echo command used. Echoed message typed: [", *args, "]")
        else:
            embed = discord.Embed(title="",
                                  description="No message typed!",
                                  color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
            print("Echo command used, but no message was typed.")

# ---------------------------------------- 8ball Command ----------------------------------------
# Randomizes response.

    @commands.command(aliases=['8', 'ball', '8ball'])
    async def eightball(self, ctx, *args):
        input = [*args]
        random_response = [
            "I don't fucking know", "Of course, dumbass.", "No?"
        ]
        if bool(input):
            await ctx.reply(f"{random.choice(random_response)}",
                            mention_author=False)
            print("8ball command used. 8ball message typed: [", *args, "]")
        else:
            embed = discord.Embed(title="",
                                  description="No message typed!",
                                  color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
            print("8ball command used, but no message was typed.")

    #@commands.command(aliases=['rd'])
    #async def randomc(self, ctx):
    #random_response = ["entry1", "entry2", "entry3"]
    #await ctx.send(f"{random.choice(random_response)}")

# ---------------------------------------- Deep Fry Command ----------------------------------------
# Deep fries an image attached to the message.
    '''
    @commands.command(aliases=['df', 'deep fry', 'deepfryimage'])
    async def deepfry(self, ctx):
        # Get the attachment from the message
        attachment = ctx.message.attachments[0]
        # Download the attachment and open it using Pillow
        image_bytes = await attachment.read()
        image = Image.open(BytesIO(image_bytes))
        # Apply the deepfry filter
        image = image.convert('RGB')
        image = image.filter(ImageFilter.SMOOTH)
        image = image.filter(ImageFilter.SHARPEN)
        # Save the image and send it back to the user
        image.save('deepfry.jpg')
        with open('deepfry.jpg', 'rb') as f:
            file = discord.File(f)
            await ctx.reply(file=file, mention_author=False)
        print("Deep Fry command used, generating image...")
    '''
    @commands.command(aliases=['df', 'deep fry', 'deepfryimage'])
    async def deepfry(self, ctx):
        # get the user's attached image
        if ctx.guild is not None:
            image = ctx.guild.icon_url_as(size=1024)
        else:
            image = ctx.author.avatar_url_as(size=1024)

        response = await self.client.http.get(str(image))
        image_bytes = await response.read()
        img = Image.open(BytesIO(image_bytes))

        # deep fry the image
        img = img.convert('RGB')
        img = img.filter(ImageFilter.SMOOTH)
        img = img.filter(ImageFilter.SHARPEN)
        img = img.filter(ImageFilter.SMOOTH)
        img = img.filter(ImageFilter.SHARPEN)

        # save the deep fried image to a buffer
        buffer = BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)

        # send the deep fried image back to the user
        await ctx.send(file=discord.File(buffer, "deep_fried.jpg"))


# ---------------------------------------- Test Image Command (REMOVE) ----------------------------------------
# Repeats an image sent by the author.

    @commands.command(aliases=['testimage'])
    async def testi(self, ctx):
        # Get the attachment from the message
        attachment = ctx.message.attachments[0]
        # Download the attachment and open it using Pillow
        image_bytes = await attachment.read()
        image = Image.open(BytesIO(image_bytes))
        # Save the image and send it back to the user
        image.save('test.jpg')
        with open('deepfry.jpg', 'rb') as f:
            file = discord.File(f)
            await ctx.reply(file=file, mention_author=False)
        print("Test Image command used, repeating image...")


async def setup(client):
    await client.add_cog(fun(client))
