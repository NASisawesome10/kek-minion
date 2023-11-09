import discord
from discord.ext import commands
#import os


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

# ---------------------------------------- Info Command ----------------------------------------
# Shows information about a particular user or a list of information of available options.

    @commands.command(aliases=[
        'i',
        'information',
        'contact',
        'contacts',
    ])
    @commands.has_any_role(765010827899437129, 702328225971568661,
                           723728937171288099)
    async def info(self, ctx, *, username=None):
        otherNames = [[
            "kek", "kek_incorporated", "kek incorporated", "server", "discord"
        ]]
        usernames = [
            [
                "<@244553215134138369>", "ben", "benjamin", "realben0416",
                "ben0416, tetris"
            ],  #index 0 | Ben
            [
                "<@181442835420151808>", "nick", "nicholas", "nasisawesome10",
                "nas", "nickel_pickle", "nickelpickle", "nickel pickle",
                "nickel", "pickle"
            ],  #index 1 | Nick
            [
                "<@520542674726551562>", "ian", "polaris", "noice",
                "darkphaz0n", "darkphazon"
            ],  #index 2 | Ian
            ["<@294477835626610698>", "adam", "Ædam", "solaire",
             "tracy"],  #index 3 | Adam
            [
                "<@378294978490925056>", "jay", "jayden", "bluejay",
                "blue jay", "ceo of horny"
            ],  #index 4 | Jayden
            [
                "<@209781510453067776>", "gage", "mazi", "mazikif",
                "catalystiv", "smurk"
            ],  #index 5 | Gage
            [
                "<@931000601263878174>", "<@259808943138668545>", "mikal",
                "zaideth", "ggzaideth"
            ],  #index 6 | Mikal
            [
                "<@245681120040058890>", "omar", "ot", "omies", "omies_ha",
                "omies ha", "omiesha"
            ],  #index 7 | Omar
            [
                "<@294917953764196352>", "andrew", "cosmicstarsans",
                "cosmicsans", "cosmic sans", "cosmic", "sans"
            ],  #index 8 | Andrew
            [
                "<@182614730119184385>", "jet", "fearlessjet", "fearless jet",
                "fearjet", "fear jet"
            ],  #index 9 | Jet
            [
                "<@489534499797991426>", "isaac", "driftvvood", "drift",
                "driftwood", "driftvvood🍀             ", "sizzler"
            ],  #index 10 | Isaac
            [
                "<@232709211841232896>",
                "hunter",
                "diamond",
                "diamondboy",
                "howdydiamond",
                "brawldiamond"  #index 11 | Hunter
            ],
            [
                "<@643614756699373612>",
                "harleen",
                "moth",
                "epic swag!!",
                "epic swag!",
                "epic swag",
                "the",
                "aradia"  #index 12 | Harleen
            ],
            [
                "<@234072335009710080>",
                "cooper",
                "cooperterryt",
                "cooperterry",
                "cooper terry",
                "coop",
                "coops",
                "oops"  #index 13 | Cooper
            ],
            [
                "<@358650473055780864>",
                "liam",
                "white lord",
                "foxxxx",
                "fox"  #index 14 | Liam
            ]
        ]

        if username is None:  #Nothing
            embed = discord.Embed(
                title="List of Valid Names:",
                description=
                f"Please enter a valid name from below: \n \n **People** \n  # `Nick` | <@181442835420151808> \n # `Adam` | <@294477835626610698> \n # `Ian` | <@520542674726551562> \n # `Ben` | <@244553215134138369> \n # `Jayden` | <@378294978490925056> \n # `Gage` | <@209781510453067776> \n # `Mikal` | <@931000601263878174> \n # `Omar` | <@245681120040058890> \n # `Andrew` | <@294917953764196352> \n # `Jet` | <@182614730119184385> \n # `Isaac` | <@489534499797991426> \n # `Hunter` | <@232709211841232896> \n # `Harleen` | <@643614756699373612> \n # `Cooper` | <@234072335009710080> \n # `Liam` | <@358650473055780864> \n \n **Other Names** \n # `KeK Incorporated` \n \n If you want to be added feel free to ping <@181442835420151808>.",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print(
                "Info command used, no username typed. Displaying list of names..."
            )
        if (username.lower() in otherNames[0]):  #KeK Incorporated
            embed = discord.Embed(
                title="",
                description=
                "This server's goal is to be a place where all our friends and friend groups can chill and stay in touch, without needing to create a bunch of group chats for everything.",
                color=0x44ff44)
            embed.set_image(
                url=
                "https://cdn.discordapp.com/splashes/702323977561047090/3590b2a47dc8b3e04773a94dc90d1d15.jpg?size=3072"
            )
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/icons/702323977561047090/a_9bf60afd5eb7659e54d84c7067b9e3fd.gif?size=100"
            )
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif (username.lower() in usernames[0]):  #Ben
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@244553215134138369> \n # YouTube | [`RealBen0416`](https://www.youtube.com/@user-mm8el9eg8j) \n # Twitch | [`RealBen0416`](https://www.twitch.tv/realben0416) \n # Twitter | [`@RealBen0416`](https://twitter.com/RealBen0416) \n \n **Games** \n # Steam | [`Ben0416`](https://steamcommunity.com/id/Ben0416/) \n # Battle.net | `Tetris#11843` \n # Minecraft | `Ben0416` \n # Nintendo Friend Code | `SW-7839-5863-1482` \n ---------------------- \n **Schedule** \n __Tuesday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n __Wednesday__ \n # Physics Lecture | <t:1677346200:t>-<t:1677351000:t> \n # Physics Lab | <t:1677369600:t>-<t:1677376500:t> \n __Thursday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n # Physics Lecture | <t:1677357000:t>-<t:1677361800:t>",
                color=0x44ff44)
            user = await self.client.fetch_user(244553215134138369)
            pfp = user.avatar
            embed.set_author(name="Ben", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")

        elif username.lower() in usernames[1]:  #Nick
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@181442835420151808> \n # YouTube | [`NASisawesome10`](https://www.youtube.com/user/NASisawesome10) \n # Twitch | [`NASisawesome10`](https://www.twitch.tv/nasisawesome10) \n # Twitter | [`NASisawesome10`](https://twitter.com/NASisawesome10) \n # Reddit | [`NASisawesome10`](https://www.reddit.com/user/NASisawesome10/) \n # Tumblr | [`NASisawesome10`](https://www.tumblr.com/settings/blog/nasisawesome10) \n # Newgrounds | [`NASisawesome10`](https://nasisawesome10.newgrounds.com/) \n # GitHub | [`NASisawesome10`](https://github.com/NASisawesome10) \n # spacehey | [`NASisawesome10`](https://spacehey.com/nasisawesome10) \n # Spotify | [`NASisawesome10`](https://open.spotify.com/user/qnss7z57396mkqtjfws2mb1fu) \n \n **Games** \n # Steam | [`NASisawesome10`](https://steamcommunity.com/id/NASisawesome10/) \n # Battle.net | `NickelPickle#11689` \n # Epic Games | `NASisawesome10` \n # Riot Games | `NASisawesome10#8569` \n # Xbox | `NASisawesome10` \n # PlayStation Network | `NASisawesome10` \n # Minecraft | `NASisawesome10` \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1678399200:t>-<t:1677376800:t> \n __Thursday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Friday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Saturday__ \n # Work | <t:1677331800:t>-<t:1677358800:t> \n __Sunday__ \n # Work | <t:1677331800:t>-<t:1677358800:t>",
                color=0x44ff44)
            user = await self.client.fetch_user(181442835420151808)
            pfp = user.avatar
            embed.set_author(name="Nick", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[2]:  #Ian
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@520542674726551562> \n # YouTube | [`ポラリス`](https://www.youtube.com/@noice8911) \n \n **Games** \n # Steam | [`Noice`](https://steamcommunity.com/id/sansth3sk3l3ton/) \n # Minecraft | `Darkphaz0n` \n # Friend Code | `SW-2540-0616-1817` \n ---------------------- \n **Schedule** \n __Monday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Wednesday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Thursday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Saturday__ \n # Work | <t:1677362400:t>-<t:1677387600:t> \n __Sunday__ \n # Work | <t:1677362400:t>-<t:1677384000:t>",
                color=0x44ff44)
            user = await self.client.fetch_user(520542674726551562)
            pfp = user.avatar
            embed.set_author(name="Ian", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[3]:  #Adam
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@294477835626610698> \n \n **Games**\n # Steam | [`Hunter of Thugs`](https://steamcommunity.com/id/do_you_ever_just/) \n # Minecraft | `BusterofNuts` \n # Nintendo Friend Code | `SW-2151-0277-8918`",
                color=0x44ff44)
            user = await self.client.fetch_user(294477835626610698)
            pfp = user.avatar
            embed.set_author(name="Adam", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[4]:  #Jayden
            embed = discord.Embed(
                title="Jayden",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@378294978490925056> \n # YouTube | [`TheOfficialBlueJay`](https://www.youtube.com/@TheOfficialBlueJay) \n # Twitch | [`TheOfficialBlueJay`](https://www.twitch.tv/theofficialbluejay) \n \n **Games** \n # Steam | [`Jayhalkio826`](https://steamcommunity.com/profiles/76561198159506442/) \n # Playstation Network | `Official-BlueJay` \n # Battle.net | `BlueJay22#1686` \n # Minecraft | `BlueJay826`",
                color=0x44ff44)
            user = await self.client.fetch_user(378294978490925056)
            pfp = user.avatar
            embed.set_author(name="Jayden", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
        elif username.lower() in usernames[5]:  #Gage
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@209781510453067776> \n # YouTube | [`Mazi`](https://www.youtube.com/@mazi48) \n # Instagram | [`mazikif`](https://www.instagram.com/mazikif/) \n \n **Games** \n # Steam | [`Mazi`](https://steamcommunity.com/id/mazikif/) \n # Battle.net | `Lulzboat#1392` \n # Riot Games | `Mazi#TXE` \n # VALORANT | [`TSU Mazi #TXE`](https://tracker.gg/valorant/profile/riot/TSU%20Mazi%23TXE/overview) \n # Minecraft | `mazikif`",
                color=0x44ff44)
            user = await self.client.fetch_user(209781510453067776)
            pfp = user.avatar
            embed.set_author(name="Gage", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[6]:  #Mikal
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@931000601263878174> \n # Discord (Alt) | <@259808943138668545> \n # YouTube | [`Zaideth`](https://www.youtube.com/@zaideth4717) \n # Twitch | [`GGZaideth`](https://www.twitch.tv/ggzaideth) \n # Spotify | [`zaideth`](https://open.spotify.com/user/22ss446rjfgnflu3zstplkhni) \n \n **Games** \n # Steam | [`ggzaideth`](https://steamcommunity.com/profiles/76561199245355998) \n # Battle.net | `Zaideth#11128` \n # Minecraft | `_zaideth_` \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Thursday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Friday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Saturday__ \n # Work | <t:1677589200:t>-<t:1678746600:t>",
                color=0x44ff44)
            user = await self.client.fetch_user(931000601263878174)
            pfp = user.avatar
            embed.set_author(name="Mikal", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[7]:  #Omar
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@245681120040058890> \n # Twitch | [`OT2003`](https://www.twitch.tv/ot2003) \n \n **Games** \n # Steam | [`Omies`](https://steamcommunity.com/profiles/76561198198643482) \n # Xbox | `OT2003` \n # Epic | `Omies Ha` \n # Battle.net | `Omies#11918` \n # Minecraft | `Omies_Ha` \n # Nintendo Friend Code | `SW-7113-1712-5337`",
                color=0x44ff44)
            user = await self.client.fetch_user(245681120040058890)
            pfp = user.avatar
            embed.set_author(name="Omar", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[8]:  #Andrew
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@294917953764196352> \n # YouTube | [`CosmicSugarSans`](https://www.youtube.com/@cosmicsugarsans884) \n # Twitch | [`CosmicStarSans22`](https://www.twitch.tv/cosmicstarsans22) \n \n **Games** \n # Steam | [`CosmicStarSans`](https://steamcommunity.com/profiles/76561198156798995/) \n # Battle.net | `CosmicSans22#1498` \n # Minecraft | `CosmicStarSans`",
                color=0x44ff44)
            user = await self.client.fetch_user(294917953764196352)
            pfp = user.avatar
            embed.set_author(name="Andrew", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[9]:  #Jet
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Illinois \n \n **Socials** \n # Discord | <@182614730119184385> \n # Carrd.co | [`Fearlessjet`](https://fearlessjet.carrd.co/) \n # YouTube | [`Fearlessjet`](https://www.youtube.com/@fearlessjet8372) \n # Twitch [`Fearlessjet`](https://www.twitch.tv/fearlessjet) \n # Twitter [`@Fearlessjet`](https://twitter.com/Fearlessjet) \n # Newgrounds [`Fearlessjet`](https://fearlessjet.newgrounds.com/) \n # TOYHOU.SE [`Fearlessjet`](https://toyhou.se/Fearlessjet) \n # Picarto.tv [`Fearlessjet`](https://picarto.tv/Fearlessjet) \n \n **Games** \n # Steam | [`Fearlessjet`](https://steamcommunity.com/id/fearlessjet/) \n # Battle.net | `Fearlessjet#1492` \n # Minecraft | `Fearlessjet`",
                color=0x44ff44)
            user = await self.client.fetch_user(182614730119184385)
            pfp = user.avatar
            embed.set_author(name="Jet", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[10]:  #Isaac
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@489534499797991426> \n # YouTube | [`Driftvvood`](https://www.youtube.com/@driftvvood0803) \n # Twitter | [`@SizZler183`](https://twitter.com/SizZler183) \n # Reddit | [`SizZler183`](https://www.reddit.com/user/SizZler183/) \n # Spotify | [`Driftsy`](https://open.spotify.com/user/su95vkqrestr1pfhmt2pflm99) \n \n **Games** \n # Xbox | `Driftvvood` \n # Battle.net | `Driftvvood#11398`",
                color=0x44ff44)
            user = await self.client.fetch_user(489534499797991426)
            pfp = user.avatar
            embed.set_author(name="Isaac", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[11]:  #Hunter
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@232709211841232896> \n # Twitch | [`brawldiamond`](https://www.twitch.tv/brawldiamond) \n # Twitter | [`@HowdyDiamond`](https://twitter.com/HowdyDiamond) \n \n **Games** \n # Xbox | `HelloDiamond953` \n # Steam [`HelloDiamond`](https://steamcommunity.com/id/HelloDiamond/) \n # Battle.net | `Diamond#12261`",
                color=0x44ff44)
            user = await self.client.fetch_user(232709211841232896)
            pfp = user.avatar
            embed.set_author(name="Hunter", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[12]:  #Harleen
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: Texas \n \n **Socials** \n # Discord | <@643614756699373612> \n # spacehey | [`Aradia`](https://spacehey.com/apocalyptic) \n # Spotify | [`EPIC SWAG!!`](https://open.spotify.com/user/31oznl6c7cqmizu6u6e4qpzh7dzm) \n \n **Games** \n # Xbox | `RoVERLETHAL`\n # Minecraft | `RoVERLETHAL` \n # Roblox | `mayumi_oni` \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Thursday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Friday__ \n # Work | <t:1677589200:t>-<t:1678746600:t> \n __Saturday__ \n # Work | <t:1677589200:t>-<t:1678746600:t>",
                color=0x44ff44)
            user = await self.client.fetch_user(643614756699373612)
            pfp = user.avatar
            embed.set_author(name="Harleen", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[13]:  #Cooper
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: North Carolina \n \n **Socials** \n # Discord | <@234072335009710080> \n \n **Games** \n # Steam | [`cooperterryt`](https://steamcommunity.com/profiles/76561199205098780) \n # Minecraft | CooperTerryT",
                color=0x44ff44)
            user = await self.client.fetch_user(234072335009710080)
            pfp = user.avatar
            embed.set_author(name="Cooper", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        elif username.lower() in usernames[14]:  #Liam
            embed = discord.Embed(
                title="",
                description=
                f"**Location**: New Jersey \n \n **Socials** \n # Discord | <@358650473055780864>",
                color=0x44ff44)
            user = await self.client.fetch_user(358650473055780864)
            pfp = user.avatar
            embed.set_author(name="Liam", url="", icon_url=pfp)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, username typed: [ " + username + " ]")
        else:
            embed = discord.Embed(
                title="Invalid Name!",
                description=
                f"Please enter a valid name from below: \n \n **People** \n  # `Nick` | <@181442835420151808> \n # `Adam` | <@294477835626610698> \n # `Ian` | <@520542674726551562> \n # `Ben` | <@244553215134138369> \n # `Jayden` | <@378294978490925056> \n # `Gage` | <@209781510453067776> \n # `Mikal` | <@931000601263878174> \n # `Omar` | <@245681120040058890> \n # `Andrew` | <@294917953764196352> \n # `Jet` | <@182614730119184385> \n # `Isaac` | <@489534499797991426> \n # `Hunter` | <@232709211841232896> \n # `Harleen` | <@643614756699373612> \n # `Cooper` | <@234072335009710080> \n # `Liam` | <@358650473055780864> \n \n **Other Names** \n # `KeK Incorporated` \n \n If you want to be added feel free to ping <@181442835420151808>.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
            print("Info command used, invalid username typed: [ " + username +
                  " ]")

# ---------------------------------------- IP Command ----------------------------------------
# Shows the IPs or a list of IPs of Minecraft servers we have.

    @commands.command(aliases=['ips', 'minecraft', 'address'])
    async def ip(self, ctx, server=None):
        ips = [["kek", "kek incorporated"], ["kexxit"]]

        if server is None:
            embed = discord.Embed(
                title="List of servers",
                description=
                f"Please enter a valid ip from below: \n \n # **KeK Incorporated** \n `KeK_Incorporated.aternos.me` \n \n # **Kexxit** \n `142.44.135.69:25582`",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("IP command used, no IP typed.")
        elif server.lower() in ips[0]:
            embed = discord.Embed(title="KeK Incorporated Minecraft IP",
                                  description=f"`KeK_Incorporated.aternos.me`",
                                  color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
        elif server.lower() in ips[1]:
            embed = discord.Embed(title="Kexxit Minecraft IP",
                                  description=f"`142.44.135.69:25582`",
                                  color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(
                title="Invalid Server!",
                description=
                f"Please enter a valid ip from below: \n \n # **KeK Incorporated** \n `KeK_Incorporated.aternos.me` \n \n # **Kexxit** \n `142.44.135.69:25582`",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)


# ---------------------------------------- Game Command ----------------------------------------
# Shows information about a particular game user play in KeK or a list of information of played games.

    @commands.command(aliases=['g', 'games', 'gg'])
    @commands.has_any_role(765010827899437129, 702328225971568661,
                           723728937171288099)
    async def game(self, ctx, *, playedGame=None):
        playedGames = [[
            "fortnite", "fort", "nite", "fn", "fortnight", "forkknife", "fork",
            "knife", "fartnut", "fart", "fartnite", "fortnut", "nut",
            "fartknife", "forknut", "fortknife"
        ],
                       [
                           "overwatch", "ow", "over", "watch", "overwatch 2",
                           "overwatch two", "ow2", "ow 2", "winton"
                       ],
                       ["valorant", "val", "val or ant", "csgo2lmao", "ant"],
                       ["gtfo", "get the fuck out", "get the fuck out!"],
                       [
                           "pokemon", "pokémon", "poke", "poké",
                           "scarlet and violet", "s/v", "sv", "pokeman",
                           "pokéman"
                       ],
                       [
                           "btd", "btd6", "bloons td 6", "bloons td battles 2",
                           "battles 2", "btdb", "btdb2", "bloons battles 2",
                           "battles", "bloons", "bloon", "blons", "blon",
                           "boons", "balloons", "balloons",
                           "bloons tower defense", "monkey", "moke", "monke"
                       ],
                       [
                           "sketchful.io, sketchful", "sketch", "drawful",
                           "draw", "drawing", "drawings", "sketchfulio"
                       ]]
        if (playedGame is None):
            embed = discord.Embed(
                title="Games Played:",
                description=
                f"Please enter a played game from below: \n \n # **Bloons** | <@&710611504826941515>, <@&915634948759769168> \n # **Fortnite** | <@&708500637997858828> \n # **GTFO** | <@&1085008845312630864> \n # **Overwatch 2** | <@&791434198535634984> \n # **Pokémon** | <@&1046810254811349076> \n # **Sketchful.io** | <@&901572758142611477> \n # **Valorant** | <@&706578597443403797> \n \n More games will be added and if you want one to be added feel free to ping <@181442835420151808>.",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print(
                "Game command used, no played game typed. Displaying list of games..."
            )
        if (playedGame.lower() in playedGames[0]):
            embed = discord.Embed(
                title="Fortnite",
                description=
                f"Chat: <#814973593623986197> \n \n Users who play <@&708500637997858828>: \n<@378294978490925056>\n<@232709211841232896>\n<@294917953764196352>\n<@489534499797991426>\n<@245681120040058890>\n<@244553215134138369>\n<@263434391034920960>\n<@471677619688177685>\n<@358650473055780864>",
                color=0x44ff44)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
            await ctx.reply(embed=embed, mention_author=False)
        elif (playedGame.lower() in playedGames[1]):
            embed = discord.Embed(
                title="Overwatch 2",
                description=
                f"Chat: <#1031798953886367854> \n \n Users who play <@&791434198535634984>: \n<@354724106727587841>\n<@378294978490925056>\n<@182614730119184385>\n<@294917953764196352>\n<@489534499797991426>\n<@372169550093090816>\n<@209781510453067776>\n<@456910239409897472>\n<@245681120040058890>\n<@704117662841831504>\n<@358650473055780864>\n<@244553215134138369>\n<@420678086581944330>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        elif (playedGame.lower() in playedGames[2]):
            embed = discord.Embed(
                title="Valorant",
                description=
                f"Chat: <#1083810615790948383> \n \n Users who play <@&706578597443403797>: \n<@244553215134138369>\n<@209781510453067776> [`TSU Mazi #TXE`](https://tracker.gg/valorant/profile/riot/TSU%20Mazi%23TXE/overview) \n<@294917953764196352>\n<@358650473055780864>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        elif (playedGame.lower() in playedGames[3]):
            embed = discord.Embed(
                title="GTFO",
                description=
                f"Chat: `None` \n \n Users who play <@&1085008845312630864>: \n<@294917953764196352>\n<@245681120040058890>\n<@244553215134138369>\n<@263434391034920960>\n<@358650473055780864>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        elif (playedGame.lower() in playedGames[4]):
            embed = discord.Embed(
                title="Pokémon",
                description=
                f"Chat: <#991331914613018726> \n \n Users who play <@&1046810254811349076>: \n<@234072335009710080>\n<@294917953764196352>\n<@643614756699373612>\n<@245681120040058890>\n<@244553215134138369>\n<@520542674726551562>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        elif (playedGame.lower() in playedGames[5]):
            embed = discord.Embed(
                title="Bloons Tower Defense",
                description=
                f"Chat: <#877421319187234866> \n \n Users who play <@&710611504826941515>: \n<@265532764873293835>\n<@181442835420151808>\n<@244553215134138369>\n<@420678086581944330> \n \n User who play <@&915634948759769168>: \n<@181442835420151808>\n<@244553215134138369>\n<@420678086581944330>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        elif (playedGame.lower() in playedGames[6]):
            embed = discord.Embed(
                title="Sketchful.io",
                description=
                f"Chat: <#888238563462885396> \n \n Users who play <@&901572758142611477>: \n<@378294978490925056>\n<@182614730119184385>\n<@234072335009710080>\n<@294917953764196352>\n<@181442835420151808>\n<@245681120040058890>\n<@244553215134138369>\n<@358650473055780864>",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, played game typed: [ " + playedGame +
                  " ]")
        else:
            embed = discord.Embed(
                title="Not played in KeK!",
                description=
                f"Please enter a played game from below: \n \n # **Bloons** | <@&710611504826941515>, <@&915634948759769168> \n # **Fortnite** | <@&708500637997858828> \n # **GTFO** | <@&1085008845312630864> \n # **Overwatch 2** | <@&791434198535634984> \n # **Pokémon** | <@&1046810254811349076> \n # **Sketchful.io** | <@&901572758142611477> \n # **Valorant** | <@&706578597443403797> \n \n More games will be added and if you want one to be added feel free to ping <@181442835420151808>.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
            print("Game command used, invalid played game typed: [ " +
                  playedGame + " ]")


async def setup(client):
    await client.add_cog(info(client))
