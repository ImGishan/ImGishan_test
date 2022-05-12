import logging

from pyrogram import Client, idle


logging.getLogger("pyrogram").setLevel(logging.INFO)

PmBot = Client(
    "Pm Bot",
    api_id=8838171,
    api_hash="0587408d4f7d9301f5295840b0f3b494",
    bot_token="5182594480:AAHDgiv3wRIP9FaePW320_veW0hBBKMzELQ",
    plugins=dict(root="plugins"),
)

PmBot.start()
uname = (PmBot.get_me()).username
print(f"""
╭━━╮╱╱╱╭━━━┳╮
╰┫┣╯╱╱╱┃╭━╮┃┃
╱┃┃╭╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┃┃╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
{uname} has been deployed!
➖➖➖➖➖➖➖➖➖➖
Support: @ImGishan
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

idle()
