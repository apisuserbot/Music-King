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
        f"""š¤ šš¢š­š° šš¤ššš©! šš¢šŗš¢ š¢š„š¢š¢š© š£š°šµ š®š¶š“šŖš¤ šŗš¢šÆšØ š„šŖ š³š¢šÆš¤š¢šÆšØ š¶šÆšµš¶š¬ š®š¦šÆšØš©šŖš£š¶š³ šøš¢š³šØš¢ šµš¦š­š¦šØš³š¢š® š„š¦šÆšØš¢šÆ ššš.\n\nā ššÆš„š¢ š¢š¬š¢šÆ š£š¦š³š±š¦š³š¢šÆšØ ššš š£š¦š³š“š¢š®š¢ š“š¢šŗš¢ š¼ , šš­šŖš¬ \'ā”ļø š¾ššš£š£šš” ššŖš„š„š¤š§š© ā”ļø\' ššµš¢š¶ š¬š­šŖš¬ šµš°š®š£š°š­ š¶š³š­ š„šŖ š£š¢šøš¢š© šŖšÆšŖ.\n\nā Tambahkan [ā”ļøš¼šØšØššØš©šš£š© ššŖšØšš ššš£šā”ļø](https://t.me/X_Newbie_Error_404) š¬š¦ šØš³š¶š± š¢šÆš„š¢ š«šŖš¬š¢ šŖšÆšØšŖšÆ š®š¶š“šŖš¤ šŖšµš¶ šš¬šµšŖš§!.\n\nšššØš©šš§ šš® [ā”ļøššš£š š¼š„ššØā”ļø](https://t.me/PacarFerdilla)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "ā”ļø š¾ššš£š£šš” ššŖš„š„š¤š§š© ā”ļø", url="https://t.me/Projectc0ding")
                  ],[
                    InlineKeyboardButton(
                        "šš§š¤šŖš„ ššŖš„š„š¤š§š©", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "ššš§šš£š©šš", url="https://telegra.ph/š¢šŗššŗ-šÆšŗššŗš-04-24"
                    ),
                    InlineKeyboardButton(
                        "š šæš¤š£ššØš š", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""ā **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šš§š¤šŖš„ ššŖš„š„š¤š§š©", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "šššØš©šš§", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""ā **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šš§š¤šŖš„ ššŖš„š„š¤š§š©", url="https://t.me/KingUserbotSupport"
                    ),
                    InlineKeyboardButton(
                        "šššØš©šš§", url="https://t.me/PacarFerdilla"
                    )
                ]
            ]
        )
   )
