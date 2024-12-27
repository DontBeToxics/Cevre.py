import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True  


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Yardıma hazırım')  


@bot.command()
async def çevre(ctx):
    Önerme = [
        " Çevre konusunda bilgi edinin",
        "Kirliliğe engel olun. Yerlere çöp atmayın. Bu alışkanlığı çocuklarınıza edindirin.",
        "Tek kullanımlık plastiklerden kaçınarak sürdürülebilir alışveriş torbaları kullanın.",
        "Atıklarınızı ayrıştırın, geri dönüşüme katkı sağlayın.",
        "Naylon poşet kullanımını azaltın. Alışverişlerinizde bez çanta kullanın" ,
        "Kâğıt havlu kullanımını azaltın.",
        "Dişinizi fırçalarken, banyo yaparken ve mutfakta çeşmeyi açık bırakmayın.",
        "Enerji tasarruflu ampuller kullanın",
        "Atık pilleri çöpe değil, atık pil kutusuna atın",
        "Bitkisel atık yağları, çöpe ya da lavaboya dökmeyin. En yakın atık yağ toplama bidonuna atın",
        "Yazışmalarınızda çıktı almamaya dikkat edin, e-posta kullanın",
        "Tek kullanımlık tabak, bardak yerine, seramik tabaklar ve metal aletler kullanın.",
        "Kişisel matara kullanarak, pet şişe kullanımını azaltın.",
        "İşyerinizde kendinize ait kupa edinin.",
        "Pikniğe gittiğinizde atıklarınızı biriktirerek eve dönüşte geri dönüşüm kutularına atın.",
        "Yerel besinleri kullanmaya özen gösterin",
        "Bilinçli tüketin, tasarruflu davranın, çevre dostu olun.",
        "Sık kullanılan cihazlar için şarj edilebilir piller satın alın.",

    ]
    await ctx.send("Bugünün tavsiyeler:\n" + "\n".join(Önerme))


@bot.command()
async def atik_gorevi(ctx):
    İşler= [
        "Bugün Yemeğini israf etme",
        "Ailene sigaranın insana ve çevreye zararlarını anlat",
        "Naylon poşet yerine geri dönüştürülebilir karton poşet kullan"
    ]
    Çalışma = random.choice(İşler)
    await ctx.send(f"Bugün bunu yapıcaksın yapmayı unutma : {Çalışma}")

bot.run("token")
