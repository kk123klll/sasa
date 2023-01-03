from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from YukkiMusic import app


@Client.on_message(~filters.edited & filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not YAFA_CHANNEL:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(sspaa, msg.from_user.id)
        except UserNotParticipant:
            if YAFA_CHANNEL.isalpha():
                link = u"https://t.me/sspaa"
            else:
                chat_info = await bot.get_chat(sspaa)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ عزيزي ↫ {message.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة البـوت اولآ\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(u"Emma 𝟸𝟶𝟸𝟹 🎄", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"عليك رفع البوت آدمن في القناة أولاً ؟؟ : @sspaa !")
