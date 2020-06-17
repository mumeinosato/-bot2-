import discord

TOKEN = NzIxNjk2MjA3ODg1NDM0OTEw.Xund1g.gJO5UvhHePi3fPFm-IY0o34rcyE


client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
