# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""🤖 𝘏𝘢𝘭𝘰 𝙎𝙤𝙗𝙖𝙩! 𝘚𝘢𝘺𝘢 𝘢𝘥𝘢𝘢𝘩 𝘣𝘰𝘵 𝘮𝘶𝘴𝘪𝘤 𝘺𝘢𝘯𝘨 𝘥𝘪 𝘳𝘢𝘯𝘤𝘢𝘯𝘨 𝘶𝘯𝘵𝘶𝘬 𝘮𝘦𝘯𝘨𝘩𝘪𝘣𝘶𝘳 𝘸𝘢𝘳𝘨𝘢 𝘵𝘦𝘭𝘦𝘨𝘳𝘢𝘮 𝘥𝘦𝘯𝘨𝘢𝘯 𝘝𝘊𝘎.\n\n⚔ 𝘈𝘯𝘥𝘢 𝘢𝘬𝘢𝘯 𝘣𝘦𝘳𝘱𝘦𝘳𝘢𝘯𝘨 𝘝𝘊𝘎 𝘣𝘦𝘳𝘴𝘢𝘮𝘢 𝘴𝘢𝘺𝘢 😼 , 𝘒𝘭𝘪𝘬 \'⚡️ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ⚡️\' 𝘈𝘵𝘢𝘶 𝘬𝘭𝘪𝘬 𝘵𝘰𝘮𝘣𝘰𝘭 𝘶𝘳𝘭 𝘥𝘪 𝘣𝘢𝘸𝘢𝘩 𝘪𝘯𝘪.\n\n⛑ Tambahkan [⚡️𝘼𝙨𝙨𝙞𝙨𝙩𝙖𝙣𝙩 𝙈𝙪𝙨𝙞𝙘 𝙆𝙞𝙣𝙜⚡️](https://t.me/X_Newbie_Error_404) 𝘬𝘦 𝘨𝘳𝘶𝘱 𝘢𝘯𝘥𝘢 𝘫𝘪𝘬𝘢 𝘪𝘯𝘨𝘪𝘯 𝘮𝘶𝘴𝘪𝘤 𝘪𝘵𝘶 𝘈𝘬𝘵𝘪𝘧!.\n\n𝙈𝙖𝙨𝙩𝙚𝙧 𝙗𝙮 [⚡️𝙆𝙞𝙣𝙜 𝘼𝙥𝙞𝙨⚡️](https://t.me/PacarFerdilla)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡️ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ⚡️", url="https://t.me/Projectc0ding")
                  ],[
                    InlineKeyboardButton(
                        "𝙂𝙧𝙤𝙪𝙥 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝", url="https://telegra.ph/𝖢𝖺𝗋𝖺-𝖯𝖺𝗄𝖺𝗂-04-24"
                
                    ),
                    InlineKeyboardButton(
                        "🎁 𝘿𝙤𝙣𝙖𝙨𝙞 🎁", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙂𝙧𝙤𝙪𝙥 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "𝙈𝙖𝙨𝙩𝙚𝙧", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙂𝙧𝙤𝙪𝙥 𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "𝙈𝙖𝙨𝙩𝙚𝙧", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        )
   )
